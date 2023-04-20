from django.contrib import admin
from .models import Product, Order, Cart
# Register your models here.

admin.site.register(Product)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product', 'status', 'quantity', 'total']

    @admin.display(ordering='total')
    def total(self, value):
        product_1 = Product.objects.get(name= value.product)
        return float(product_1.price)*float(value.quantity)


admin.site.register(Order, OrderAdmin)
admin.site.register(Cart)