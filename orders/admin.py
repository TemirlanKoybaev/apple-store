from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'email', 
                    'address', 'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated', 'city']
    inlines = [OrderItemInline]
    search_fields = ['first_name', 'last_name', 'email', 'address']
    list_editable = ['paid']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'price', 'quantity']
    list_filter = ['order__paid']