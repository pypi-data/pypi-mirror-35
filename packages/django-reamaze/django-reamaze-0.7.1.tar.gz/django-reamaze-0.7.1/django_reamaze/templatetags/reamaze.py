# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import six
from django.conf import settings
from django.template import Library
register = Library()


def user_is_authenticated(user):
    if callable(user.is_authenticated):
        return user.is_authenticated()
    return user.is_authenticated


@register.inclusion_tag('django_reamaze/templatetags/reamaze.html', takes_context=True)
def add_reamaze_script(context):
    import hmac
    import hashlib
    try:
        anonymous_mode = getattr(settings, 'REAMAZE_OK_FOR_ANONYMOUS', False)
        prefix_for_user_id = getattr(settings, 'REAMAZE_PREFIX_USER_ID', None)
        request = context['request']
        reamaze_context = {'display_reamaze': False, 'reamaze_auth_key': None}
        user_id = reamaze_context["user_id"] = request.user.id
        if prefix_for_user_id:
            user_id = prefix_for_user_id + str(request.user.id)
        reamaze_context["user_id"] = user_id
        if user_is_authenticated(request.user) or anonymous_mode:
            reamaze_context.update({'display_reamaze': True,
                                    'reamaze_js_url': getattr(settings, 'REAMAZE_JS_URL', ""),
                                    'reamaze_account': getattr(settings, 'REAMAZE_ACCOUNT', ""),
                                    'user_agent': request.META['HTTP_USER_AGENT'],
                                    'http_referer': request.META.get('HTTP_REFERER', ""),
                                    'reamaze_channel': getattr(settings, 'REAMAZE_CHANNEL', None)})

        if user_is_authenticated(request.user):
            reamaze_secret_key = getattr(settings, 'REAMAZE_SECRET_KEY', b"")
            reamaze_auth_key = hmac.new(reamaze_secret_key,
                                        six.b(str(user_id)) + b":" + six.b(request.user.email),
                                        hashlib.sha256).hexdigest()
            reamaze_context['reamaze_auth_key'] = reamaze_auth_key

        context.update(reamaze_context)
        return context
    except KeyError:
        return context
