from django.urls import path, include
from rest_framework import routers

from custom_auth import api

router = routers.SimpleRouter()
router.register('', api.UserViewSet, basename='auth')

urlpatterns = [
    path('', include(router.urls)),
]