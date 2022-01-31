from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect

from macaddrs.models import MacAddr

def info_view(request, *args, **kwargs):
    context = { }
    HTML_STRING = render_to_string("info-view.html", context=context)
    return HttpResponse(HTML_STRING)
