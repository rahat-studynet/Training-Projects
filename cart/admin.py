from django.contrib import admin
from .models import Product, UserCartItem, CartItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Admin product list display
    list_display = ('name', 'price', 'stock', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(UserCartItem)
class UserCartItemAdmin(admin.ModelAdmin):
    # Regular user cart items
    list_display = ('user', 'product', 'quantity', 'added_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('added_at',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    # API cart items for Postman testing
    list_display = ('product_name', 'product_id', 'quantity', 'price', 'created_at')
    search_fields = ('product_name',)