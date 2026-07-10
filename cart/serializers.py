from rest_framework import serializers
from .models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta: # To configure or give order/instructions to CartItemSerializer
        model = CartItem # Work on CartItem Data
        fields = ['id', 'product_id', 'product_name', 'quantity', 'price', 'created_at'] # Covert this to JSON

    def validate_product_id(self, value):
        qs = CartItem.objects.filter(product_id=value)

        if self.instance:
            qs = qs.exclude(id=self.instance.id)

        if qs.exists():
            raise serializers.ValidationError(
                "This product already exists in your cart. Try updating its quantity instead."
            )

        return value

    def validate_product_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Product name cannot be empty.")
        return value

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Quantity must be at least 1.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value