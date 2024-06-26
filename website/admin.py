from django.contrib import admin
from .models import Product, Order, OrderItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'description')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'customer_name', 'address', 'phone_number', 'created_at', 'order_delivery_date','payment_status', 'delivery_status')
    search_fields = ('customer_name', 'email', 'phone_number')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'unit_price', )
    search_fields = ('order__customer_name', 'product__name')