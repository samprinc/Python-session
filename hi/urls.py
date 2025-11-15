from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SermonViewSet, EventViewSet, MinistryViewSet,
    HomepageContentViewSet, LivestreamViewSet
)

router = DefaultRouter()
router.register('sermons', SermonViewSet)
router.register('events', EventViewSet)
router.register('ministries', MinistryViewSet)
router.register('homepage', HomepageContentViewSet)
router.register('livestreams', LivestreamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
# This file defines the URL routing for the hi app, linking the viewsets to their respective endpoints.
# It uses Django REST Framework's DefaultRouter to automatically generate the URL patterns for the viewsets