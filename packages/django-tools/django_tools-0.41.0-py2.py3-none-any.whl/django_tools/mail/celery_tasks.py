# coding: utf-8

"""
    mail util
    ~~~~~~~~~

    :copyleft: 2017-2018 by the django-tools team, see AUTHORS for more details.
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""

from __future__ import unicode_literals, absolute_import, print_function

import logging

from django.conf import settings
from django.core.mail import send_mail as do_send_mail


log = logging.getLogger(__name__)


try:
    from celery import shared_task
except ImportError as err:
    CELERY_IMPORT_ERROR = err

    from functools import wraps

    def shared_task(*task_args, **task_kwargs):
        def task_decorator(func):
            @wraps(func)
            def func_wrapper(*args, **kwargs):
                log.error(
                    "celery not available: %s",
                    CELERY_IMPORT_ERROR
                )
                return func(*args, **kwargs)
            return func_wrapper
        return task_decorator


@shared_task(name='mail:send_mail')
def send_mail(subject, message, from_email, recipient_list):
    do_send_mail(subject, message, from_email, recipient_list)


@shared_task(name=settings.SEND_MAIL_CELERY_TASK_NAME)
def send_mail_celery_task(msg):
    return msg.send()
