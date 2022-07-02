from django.urls import path, include
from rest_framework import routers

from product import api

router = routers.SimpleRouter()
router.register('', api.ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]