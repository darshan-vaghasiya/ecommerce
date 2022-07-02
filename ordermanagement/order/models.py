from django.db import models
from product.models import BaseModel
from custom_auth.models import User
from product.models import Product


class Order(BaseModel):
    """This model is used for store order data"""
    payment_type = (
        ('Card', 'Card'),
        ('Cash', 'Cash'),
        ('Wallet', 'Wallet')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    total_price = models.IntegerField(null=True, blank=True, default=0)
    total_qty = models.IntegerField(null=True, blank=True, default=0)
    placed = models.BooleanField(default=True)
    payment_type = models.CharField(choices=payment_type, default="Cash", max_length=8)

    class Meta:
        db_table = "Order"


class OrderDetails(BaseModel):
    """This model is used for store order details"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
    price = models.IntegerField()
    qty = models.SmallIntegerField()

    class Meta:
        db_table = "Order details"
