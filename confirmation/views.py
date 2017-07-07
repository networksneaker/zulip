# -*- coding: utf-8 -*-

# Copyright: (c) 2008, Jarek Zgoda <jarek.zgoda@gmail.com>

__revision__ = '$Id: views.py 21 2008-12-05 09:21:03Z jarek.zgoda $'


from django.shortcuts import render
from django.template import RequestContext
from django.conf import settings
from django.http import HttpRequest, HttpResponse

from confirmation.models import Confirmation
from zerver.models import PreregistrationUser

from typing import Any, Dict

# This is currently only used for confirming PreregistrationUser.
# Do not add other confirmation paths here.
def confirm(request, confirmation_key):
    # type: (HttpRequest, str) -> HttpResponse
    confirmation_key = confirmation_key.lower()
    obj = Confirmation.objects.confirm(confirmation_key)
    ctx = {'confirmed': False}  # type: Dict[str, Any]
    templates = [
        'confirmation/confirm.html',
    ]
    if obj:
        ctx = {
            'key': confirmation_key,
            'full_name': request.GET.get("full_name", None),
        }
        templates = ['confirmation/confirm_preregistrationuser.html']
    return render(request, templates, context=ctx)
