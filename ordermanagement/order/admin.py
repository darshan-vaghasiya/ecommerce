from django.contrib import admin
from order.models import Order, OrderDetails


class OrderDetailsInline(admin.TabularInline):
    model = OrderDetails
    readonly_fields = ('id', 'get_product_name', 'price', 'qty')

    def get_product_name(self, obj):
        return obj.product.name

    get_product_name.short_description = 'product name'


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user', 'total_price', 'total_qty', 'placed', 'payment_type')
    search_fields = ('user', 'placed')
    inlines = (OrderDetailsInline,)

    def get_user(self, obj):
        return obj.user

    get_user.short_description = 'user'


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetails)