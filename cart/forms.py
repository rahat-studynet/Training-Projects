from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    # Form for admin to create or update products
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'price', 'stock']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter product name',
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter product description',
                'class': 'form-control',
                'rows': 4
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Enter product price',
                'class': 'form-control',
                'step': '0.01',
                'min': '0.01'
            }),
            'stock': forms.NumberInput(attrs={
                'placeholder': 'Enter stock quantity',
                'class': 'form-control',
                'min': '0'
            }),
        }

    def clean_price(self):
        # Validate product price
        price = self.cleaned_data.get('price')

        if price <= 0:
            raise forms.ValidationError("Price must be greater than 0.")

        return price

    def clean_stock(self):
        # Validate product stock
        stock = self.cleaned_data.get('stock')

        if stock < 0:
            raise forms.ValidationError("Stock cannot be negative.")

        return stock