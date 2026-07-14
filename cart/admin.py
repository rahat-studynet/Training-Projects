from django.contrib import admin
from .models import Product, CartItem, UserCartItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Show product information in admin list
    list_display = ('name', 'price', 'stock', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    # Show cart item information in admin list
    list_display = ('product_name', 'product_id', 'quantity', 'price', 'created_at')
    search_fields = ('product_name',)

@admin.register(UserCartItem)
class UserCartItemAdmin(admin.ModelAdmin):
    # Show regular user cart items in admin panel
    list_display = ('user', 'product', 'quantity', 'added_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('added_at',)