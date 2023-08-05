from datetime import timedelta
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib.auth.views import logout
from django.http import HttpResponseForbidden
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from auth_lockout.models import Attempt


class SecureLogin(MiddlewareMixin):  # pylint: disable=too-few-public-methods
    def __init__(self, *args, **kwargs):
        super(SecureLogin, self).__init__(*args, **kwargs)
        auth_views.LoginView.dispatch = monitor(auth_views.LoginView.dispatch)


FORBIDDEN_MESSAGE = getattr(settings, 'FORBIDDEN_MESSAGE', 'Too many attempts to login from IP "%s" , '
                                                           'account will be locked for a given period. '
                                                           'Please try again later.')
LOCKOUT_PERIOD = timedelta(minutes=getattr(settings, 'LOCKOUT_PERIOD', 3))
CLEAROUT_PERIOD = timedelta(minutes=getattr(settings, 'LOCKOUT_PERIOD', 3) * 1.01)
MAX_FAILURES = getattr(settings, 'MAX_FAILURES', 3)


def formatdict(items):
    params = []
    for key, value in items:
        if key != 'password':
            params.append(u'%s=%s' % (key, value))
    return '\n'.join(params)


def attempts(request):
    ipaddress = request.META.get('REMOTE_ADDR', '')
    username = request.POST.get('username', None)
    all_attempts = Attempt.objects.filter(ipaddress=ipaddress, username=username)
    for attempt in all_attempts:
        if attempt.created + LOCKOUT_PERIOD < timezone.now():
            attempt.delete()
    return all_attempts


def monitor(func):
    def decorated_login(view, request, *args, **kwargs):
        if locked(request):
            return HttpResponseForbidden(FORBIDDEN_MESSAGE % request.META.get('REMOTE_ADDR', '<unknown>'))
        response = func(view, request, *args, **kwargs)
        if func.__name__ == 'decorated_login':
            return response
        if request.method == 'POST':
            login_failed = (response and not response.has_header('location') and response.status_code != 302)
            if handle_request(request, login_failed):
                return response
            return HttpResponseForbidden(FORBIDDEN_MESSAGE % request.META.get('REMOTE_ADDR', '<unknown>'))
        return response

    return decorated_login


def locked(request):
    if attempts(request).count() >= MAX_FAILURES:
        return True
    return False


def clear_older():
    older_attempts = timezone.now() - CLEAROUT_PERIOD
    Attempt.objects.filter(created__lte=older_attempts).delete()


def handle_request(request, login_failed):
    clear_older()
    all_attempts = attempts(request)
    if login_failed and request.POST.get('username', None):
        attempt = Attempt()
        attempt.username = request.POST.get('username')
        attempt.useragent = request.META.get('HTTP_USER_AGENT', '<unknown>')
        attempt.ipaddress = request.META.get('REMOTE_ADDR', '<unknown>')
        attempt.get_data = formatdict(request.GET.items())
        attempt.post_data = formatdict(request.POST.items())
        attempt.http_accept = request.META.get('HTTP_ACCEPT', '<unknown>')
        attempt.path_info = request.META.get('PATH_INFO', '<unknown>')
        attempt.save()
    else:
        for attempt in all_attempts:
            attempt.delete()
    if all_attempts.count() >= MAX_FAILURES:
        logout(request)
        return False
    return True
