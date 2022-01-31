from django.contrib import admin
from django.urls import path, include
from .views import (
    info_view,
    )
from macaddrs.views import (
    registration_view,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oidc/', include('mozilla_django_oidc.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('info/', info_view),
    path('register/', registration_view),
    path('', include('comanage.urls')),
]
