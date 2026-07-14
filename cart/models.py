from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    # Product information created by admin
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Show product name in admin panel
        return self.name
    
class UserCartItem(models.Model):
    # Cart item for regular users
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevent same user from having duplicate cart rows for the same product
        unique_together = ('user', 'product')

    def __str__(self):
        # Show cart item information in admin panel
        return f"{self.user.username} - {self.product.name} - {self.quantity}"


class CartItem(models.Model): #Inherit 
    product_id = models.IntegerField(unique=True)
    product_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} - {self.quantity} pcs"