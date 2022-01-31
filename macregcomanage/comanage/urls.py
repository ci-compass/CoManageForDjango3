from django.urls import path

from . import views

urlpatterns = [
    path('', views.ldap_attributes, name='login'),
]
