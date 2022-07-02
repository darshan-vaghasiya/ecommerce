from django.urls import path, include
from rest_framework import routers

from order import api

router = routers.SimpleRouter()
router.register('', api.OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]