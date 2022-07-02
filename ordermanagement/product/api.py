from rest_framework import viewsets, mixins, permissions
from rest_framework.authentication import TokenAuthentication
from product.models import Category, Product
from product.serializer import ProductSerializer


class ProductViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    model = Product
    queryset = model.objects.filter(is_delete=False, is_active=True)
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]