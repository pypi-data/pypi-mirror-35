# -*- coding: utf-8 -*-
"""CAS login/logout replacement views"""
import logging
from six.moves.urllib_parse import urlencode
from six.moves import urllib_parse as urlparse

from operator import itemgetter

from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from .utils import _redirect_url, _get_session, _logout_url, is_authenticated

__all__ = ['login', 'logout']
logger = logging.getLogger('cas')


def is_secure(request):
    return getattr(settings, 'IS_SECURE', request.is_secure())


def _service_url(request, redirect_to=None, gateway=False):
    """Generates application service URL for CAS"""
    protocol = ('http://', 'https://')[is_secure(request)]
    host = request.get_host()
    service = protocol + host + request.path
    if redirect_to:
        if '?' in service:
            service += '&'
        else:
            service += '?'
        if gateway:
            """ If gateway, capture params and reencode them before returning a url """
            gateway_params = [(REDIRECT_FIELD_NAME, redirect_to), ('gatewayed',
                                                                   'true')]
            query_dict = request.GET.copy()
            try:
                del query_dict['ticket']
            except Exception:
                pass
            query_list = query_dict.items()

            # remove duplicate params
            for item in query_list:
                for index, item2 in enumerate(gateway_params):
                    if item[0] == item2[0]:
                        gateway_params.pop(index)
            extra_params = gateway_params + query_list

            # Sort params by key name so they are always in the same order.
            sorted_params = sorted(extra_params, key=itemgetter(0))
            service += urlencode(sorted_params)
        else:
            service += urlencode({REDIRECT_FIELD_NAME: redirect_to})
    return service


def _login_url(service, ticket='ST', gateway=False, cas_url=''):
    """Generates CAS login URL"""
    LOGINS = {'ST': 'login', 'PT': 'proxyValidate'}
    if gateway:
        params = {'service': service, 'gateway': True}
    else:
        params = {'service': service}
    if settings.CAS_EXTRA_LOGIN_PARAMS:
        params.update(settings.CAS_EXTRA_LOGIN_PARAMS)
    if not ticket:
        ticket = 'ST'
    login = LOGINS.get(ticket[:2], 'login')

    return urlparse.urljoin(cas_url,
                            login) + '?' + urlencode(params)


def login(request, next_page=None, required=False, gateway=False):
    """Forwards to CAS login URL or verifies CAS ticket"""

    if not next_page:
        next_page = _redirect_url(request)
    if is_authenticated(request.user):
        return HttpResponseRedirect(next_page)
    ticket = request.GET.get('ticket')
    cas_url = request.domain.auth.url + '/cas/'
    service = _service_url(request, next_page, False)

    if ticket:
        user = auth.authenticate(
            ticket=ticket, service=service, cas_url=cas_url)
        if user is not None:
            # Has ticket, logs in fine
            auth.login(request, user)
            return HttpResponseRedirect(next_page)
        elif settings.CAS_RETRY_LOGIN or required:
            # Has ticket,
            return HttpResponseRedirect(_login_url(service, ticket, False, cas_url))
        else:
            logger.warning(
                'User has a valid ticket but not a valid session, ticket is %s, service is %s, url is %s'
                % (ticket, service, cas_url))
            error = "<h1>Forbidden</h1><p>Login failed.</p>"
            return HttpResponseForbidden(error)
    else:
        if gateway:
            return HttpResponseRedirect(_login_url(service, ticket, True, cas_url=cas_url))
        else:
            return HttpResponseRedirect(_login_url(service, ticket, False, cas_url=cas_url))


def logout(request, next_page=None):
    """Redirects to CAS logout page"""
    cas_logout_request = request.POST.get('logoutRequest', '')
    if cas_logout_request:
        session = _get_session(cas_logout_request)
        request.session = session
    auth.logout(request)

    if not next_page:
        next_page = _redirect_url(request)
    if settings.CAS_LOGOUT_COMPLETELY:
        return HttpResponseRedirect(_logout_url(request, next_page))
    else:
        return HttpResponseRedirect(next_page)
