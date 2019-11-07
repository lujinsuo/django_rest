"""django_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from api01 import views
from django.urls import path
from django.conf.urls import url,include
from rest_framework import routers
from api01.models import Event,Guest
from rest_framework.urlpatterns import format_suffix_patterns

router=routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'groups',views.GroupViewSet)
# router.register(r'Events',views.EventViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',include(router.urls)),
    url(r'api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    url(r'Events/$',views.event_list),
	url(r'Events/(?P<pk>[0-9]+)/$',views.event_deail),
]
# urlpatterns=format_suffix_patterns(urlpatterns)