"""noirlab_comanage_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import (
    home_view,
    login_view,
    info_view,
    )
from macaddrs.views import (
    registration_view,
    )



#
# General plan of URLs:
# Plain old slash welcomes users.
# /login/ uses the Django-supplied authentication mechanism
# /info/ is where the users put in their MAC addresses
# /register receives the POST response from the button on /info/,
# records the data into a macaddrs object (which in turn saves in
# sqllite3 or the database of your choosing), and politely thanks
# the visitors.
# 

urlpatterns = [
    path("", home_view),
    path("info/", info_view),
    path("login/", login_view),
    path("login/<str:id>", login_view),
    path("register/", registration_view),
    path('admin/', admin.site.urls),
]
