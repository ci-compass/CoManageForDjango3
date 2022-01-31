from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from macaddrs.models import MacAddr

def home_view(request, *args, **kwargs):
    context = { }
    HTML_STRING = render_to_string("home-view.html", context=context)
    return HttpResponse(HTML_STRING)


def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        print (username, password)
        user = authenticate(request,username=username, password=password)
        if user is None:
            context = {"error": "Invalid username or password. Or both."}
            return render(request, "login.html", context)
        login(request,user)
        return redirect('/info')
    return render(request, "login.html", {} )


def info_view(request, *args, **kwargs):
    context = { }
    HTML_STRING = render_to_string("info-view.html", context=context)
    return HttpResponse(HTML_STRING)

