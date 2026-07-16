from rest_framework import serializers
from .models import Product, CartItem

class ProductSerializer(serializers.ModelSerializer):
    # Full image URL for API response
    image_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image', 'image_url', 'price', 'stock', 'created_at' ]

        read_only_fields = ['id', 'image_url', 'created_at' ]

    def get_image_url(self, obj):
        # Return full image URL for Postman response
        request = self.context.get('request')

        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)

        if obj.image:
            return obj.image.url

        return None

    def validate_name(self, value):
        # Product name cannot be empty
        if not value.strip():
            raise serializers.ValidationError("Product name cannot be empty.")

        return value

    def validate_price(self, value):
        # Price must be greater than zero
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")

        return value

    def validate_stock(self, value):
        # Stock cannot be negative
        if value < 0:
            raise serializers.ValidationError("Stock cannot be negative.")

        return value



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