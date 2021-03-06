# from django.conf import settings
# from django.contrib.auth import SESSION_KEY, BACKEND_SESSION_KEY
from django.contrib.auth.models import AnonymousUser

# from django.utils.importlib import import_module


def request_factory_login(factory, user=None, method="request", **kwargs):
    """Based on this gist: https://gist.github.com/964472"""
    # engine = import_module(settings.SESSION_ENGINE)
    request = getattr(factory, method)(**kwargs)
    # request.session = engine.SessionStore()
    # request.session[SESSION_KEY] = user.pk
    request.user = user or AnonymousUser()
    return request
