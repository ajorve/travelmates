"""Capstone_TWF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from rest_framework import routers
from accounts.views import GroupViewSet, MemberViewSet
from places.views import LocationViewSet, ZoneViewSet, GeotagViewSet
from events.views import JourneyViewSet, CheckInViewSet
from accounts.views import login, registration, app

router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'users', MemberViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'zones', ZoneViewSet)
router.register(r'geotags', GeotagViewSet)
router.register(r'journeys', JourneyViewSet)
router.register(r'check_ins', CheckInViewSet)

urlpatterns = [

                  url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
                  url(r'^admin/', admin.site.urls),  # TODO: Django honeypot?
                  url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
                  url(r'^app/', app, name='app'),

                  # Auth
                  url(r'^login/', login, name='login'),
                  url(r'register/', registration, name='register'),

                  # Wire up our API using automatic URL routing.
                  # Additionally, we include login URLs for the browsable API.

                  # DRF
                  url(r'^api/', include(router.urls)),
                  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
