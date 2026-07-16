from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .forms import ProductForm
from .models import Product, UserCartItem, CartItem
from .serializers import CartItemSerializer


# ==================================================
# ADMIN CMS VIEWS
# ==================================================

@login_required(login_url='/signin/')
def admin_dashboard_view(request):
    # Show dashboard only for admin/staff users
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to access the admin dashboard.")

    total_products = Product.objects.count()
    total_stock = sum(product.stock for product in Product.objects.all())
    total_cart_items = UserCartItem.objects.count()

    return render(request, 'cart/admin_dashboard.html', {
        'total_products': total_products,
        'total_stock': total_stock,
        'total_cart_items': total_cart_items
    })


@login_required(login_url='/signin/')
def admin_product_list_view(request):
    # Show all products only to admin/staff users
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to access the product management page.")

    products = Product.objects.all().order_by('-created_at')

    return render(request, 'cart/admin_product_list.html', {
        'products': products
    })


@login_required(login_url='/signin/')
def admin_product_add_view(request):
    # Allow only admin/staff users to add products
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to add products.")

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully.")
            return redirect('admin-products')

    else:
        form = ProductForm()

    return render(request, 'cart/admin_product_add.html', {
        'form': form
    })


@login_required(login_url='/signin/')
def admin_product_edit_view(request, product_id):
    # Allow only admin/staff users to edit products
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to edit products.")

    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully.")
            return redirect('admin-products')

    else:
        form = ProductForm(instance=product)

    return render(request, 'cart/admin_product_edit.html', {
        'form': form,
        'product': product
    })


@login_required(login_url='/signin/')
def admin_product_delete_view(request, product_id):
    # Allow only admin/staff users to delete products
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to delete products.")

    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product_name = product.name
        product.delete()

        messages.success(request, f"Product '{product_name}' deleted successfully.")
        return redirect('admin-products')

    return redirect('admin-products')


# ==================================================
# REGULAR USER PRODUCT AND CART VIEWS
# ==================================================

@login_required(login_url='/signin/')
def product_list_view(request):
    # Show available products only for regular users
    if request.user.is_staff:
        return redirect('admin-dashboard')

    products = Product.objects.filter(stock__gt=0).order_by('-created_at')

    return render(request, 'cart/product_list.html', {
        'products': products
    })


@login_required(login_url='/signin/')
def add_to_cart_view(request, product_id):
    # Add selected product to current user's cart
    if request.user.is_staff:
        return redirect('admin-dashboard')

    product = get_object_or_404(Product, id=product_id)

    if product.stock <= 0:
        messages.error(request, "This product is out of stock.")
        return redirect('products')

    cart_item, created = UserCartItem.objects.get_or_create(user=request.user, product=product)

    if created:
        messages.success(request, "Product added to your cart.")

    else:
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, "Product quantity updated in your cart.")
        else:
            messages.error(request, "You cannot add more than available stock.")

    return redirect('products')


@login_required(login_url='/signin/')
def my_cart_view(request):
    # Show current user's cart with item total and grand total
    if request.user.is_staff:
        return redirect('admin-dashboard')

    cart_items = UserCartItem.objects.filter(user=request.user).select_related('product')

    cart_data = []
    grand_total = 0

    for item in cart_items:
        item_total = item.product.price * item.quantity
        grand_total += item_total

        cart_data.append({
            'item': item,
            'item_total': item_total
        })

    return render(request, 'cart/my_cart.html', {
        'cart_data': cart_data,
        'grand_total': grand_total
    })


@login_required(login_url='/signin/')
def increase_cart_quantity_view(request, item_id):
    # Increase quantity if stock is available
    if request.user.is_staff:
        return redirect('admin-dashboard')

    cart_item = get_object_or_404(UserCartItem, id=item_id, user=request.user)

    if request.method == 'POST':
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, "Cart quantity increased.")
        else:
            messages.error(request, "You cannot add more than available stock.")

    return redirect('my-cart')


@login_required(login_url='/signin/')
def decrease_cart_quantity_view(request, item_id):
    # Decrease quantity or remove item if quantity becomes zero
    if request.user.is_staff:
        return redirect('admin-dashboard')

    cart_item = get_object_or_404(UserCartItem, id=item_id, user=request.user)

    if request.method == 'POST':
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
            messages.success(request, "Cart quantity decreased.")
        else:
            cart_item.delete()
            messages.success(request, "Item removed from your cart.")

    return redirect('my-cart')


@login_required(login_url='/signin/')
def remove_from_cart_view(request, item_id):
    # Remove selected item from current user's cart
    if request.user.is_staff:
        return redirect('admin-dashboard')

    cart_item = get_object_or_404(UserCartItem, id=item_id, user=request.user)

    if request.method == 'POST':
        cart_item.delete()
        messages.success(request, "Item removed from your cart.")

    return redirect('my-cart')


@login_required(login_url='/signin/')
def checkout_view(request):
    # Checkout current user's cart
    if request.user.is_staff:
        return redirect('admin-dashboard')

    cart_items = UserCartItem.objects.filter(user=request.user).select_related('product')

    if not cart_items.exists():
        messages.error(request, "Your cart is empty. Please add products before checkout.")
        return redirect('my-cart')

    if request.method == 'POST':
        for item in cart_items:
            product = item.product

            if item.quantity > product.stock:
                messages.error(request, f"Not enough stock for {product.name}. Available stock: {product.stock}.")
                return redirect('my-cart')

        for item in cart_items:
            product = item.product
            product.stock -= item.quantity
            product.save()

        cart_items.delete()

        messages.success(request, "Checkout completed successfully.")
        return redirect('products')

    return render(request, 'cart/checkout.html', {
        'cart_items': cart_items
    })


# ==================================================
# DRF API VIEW FOR POSTMAN
# ==================================================

class CartItemViewSet(viewsets.ModelViewSet):
    # API viewset for Postman testing
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]