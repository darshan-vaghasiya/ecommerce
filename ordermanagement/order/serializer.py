from rest_framework import serializers
from order.models import Order, OrderDetails

from product.serializer import ProductSerializer


class OrderDetailsSerializer(serializers.ModelSerializer):
    """
    This serializer showing the order details data
    """
    category = serializers.ReadOnlyField(source='product.category.name')
    brand = serializers.ReadOnlyField(source='product.brand_name')
    name = serializers.ReadOnlyField(source='product.name')
    img_url = serializers.ReadOnlyField(source='product.image.url')

    class Meta:
        model = OrderDetails
        fields = ['id', 'category', 'brand', 'name', 'price', 'qty', 'img_url']


class OrderSerializer(serializers.ModelSerializer):
    """
    This serializer showing the product data
    """
    order = OrderDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'create_time', 'placed', 'total_price', 'total_qty', 'payment_type', 'order']


class AddOrderSerializer(serializers.ModelSerializer):
    """
    This serializer adding order
    """
    products = serializers.ListField(child=serializers.JSONField(), required=True,
                                     error_messages={'required': "Please enter product data",
                                                     'blank': "Please enter product data"},
                                     write_only=True)

    class Meta:
        model = Order
        fields = ['id', 'products', 'payment_type']
        extra_kwargs = {
            'payment_type': {'required': True,
                             'error_messages': {'required': "Please enter payment type (Cash,Wallet,Card).",
                                                'blank': 'Please enter payment type (Cash,Wallet,Card).'}},
        }

    def create(self, validated_data):
        user_data = self.context['request'].user.id
        validated_data['user_id'] = user_data
        products = validated_data.pop('products', None)
        order = super().create(validated_data)
        for product in products:
            order_details = OrderDetails.objects.create(order=order, product_id=product['id'], price=product['price'],
                                                        qty=product['qty'])
            if order_details is not None:
                order.total_price += product['price']
                order.total_qty += product['qty']
                order.save()
        return order
