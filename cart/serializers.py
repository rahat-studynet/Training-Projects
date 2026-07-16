from rest_framework import serializers
from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    # Serializer for API CartItem model
    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'product_name', 'quantity', 'price', 'created_at']

    def validate_product_id(self, value):
        # Prevent duplicate product_id
        cart_items = CartItem.objects.filter(product_id=value)

        if self.instance:
            cart_items = cart_items.exclude(id=self.instance.id)

        if cart_items.exists():
            raise serializers.ValidationError(
                "This product already exists in your cart. Try updating its quantity instead."
            )

        return value

    def validate_product_name(self, value):
        # Product name cannot be empty
        if not value.strip():
            raise serializers.ValidationError("Product name cannot be empty.")

        return value

    def validate_quantity(self, value):
        # Quantity must be at least 1
        if value < 1:
            raise serializers.ValidationError("Quantity must be at least 1.")

        return value

    def validate_price(self, value):
        # Price must be greater than 0
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")

        return value