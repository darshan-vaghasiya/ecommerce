from rest_framework import viewsets, mixins, permissions, status
from rest_framework.authentication import TokenAuthentication
from order.models import Order
from order.serializer import OrderSerializer, AddOrderSerializer
from rest_framework.response import Response


class OrderViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    model = Order
    queryset = model.objects.filter(is_delete=False, is_active=True)
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return AddOrderSerializer
        return OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user_id=self.request.user, is_active=True, is_delete=False).order_by('-id')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        order = OrderSerializer(serializer)
        return Response("Order Successfully Place.", status=status.HTTP_201_CREATED)
