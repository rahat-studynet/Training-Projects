from django.db import models

class CartItem(models.Model): #Inherit 
    product_id = models.IntegerField(unique=True)
    product_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} - {self.quantity} pcs"