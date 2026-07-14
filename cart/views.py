from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication

from .models import CartItem, Product, UserCartItem
from .serializers import CartItemSerializer

from django.contrib import messages
from .forms import ProductForm


class CartItemViewSet(viewsets.ModelViewSet):
    # Telling Django which database table/query to fetch the data from
    queryset = CartItem.objects.all()

    # Telling Django which serializer to use for data conversion
    serializer_class = CartItemSerializer

    # Authentication methods
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]

    # Only authenticated users can access this API
    permission_classes = [IsAuthenticated]


# Frontend Views to render UI Screens
@ensure_csrf_cookie
@login_required(login_url='/signin/')
def cart_list_screen(request):
    """Renders the Cart List UI Page"""
    return render(request, 'cart/cart_list.html')


@ensure_csrf_cookie
@login_required(login_url='/signin/')
def add_item_screen(request):
    """Renders the Add Item Form UI Page"""
    return render(request, 'cart/add_item.html')


@login_required(login_url='/signin/')
def admin_dashboard_view(request):
    # Show dashboard only for staff/admin users
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
def product_list_view(request):
    # Show available products only for regular logged-in users
    if request.user.is_staff:
        return redirect('admin-dashboard')

    products = Product.objects.filter(stock__gt=0).order_by('-created_at')

    return render(request, 'cart/product_list.html', {
        'products': products
    })


@login_required(login_url='/signin/')
def admin_product_list_view(request):
    # Show product list only for staff/admin users
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to access the product management page.")

    products = Product.objects.all().order_by('-created_at')

    return render(request, 'cart/admin_product_list.html', {
        'products': products
    })


@login_required(login_url='/signin/')
def admin_product_add_view(request):
    # Allow only staff/admin users to add products
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to add products.")

    # If admin submits the form
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, "Product added successfully.")
            return redirect('admin-products')

    # If admin opens the form page normally
    else:
        form = ProductForm()

    return render(request, 'cart/admin_product_add.html', {
        'form': form
    })

@login_required(login_url='/signin/')
def add_to_cart_view(request, product_id):
    # Allow only regular users to add products to cart
    if request.user.is_staff:
        return redirect('admin-dashboard')

    product = get_object_or_404(Product, id=product_id)

    # Check product stock before adding
    if product.stock <= 0:
        messages.error(request, "This product is out of stock.")
        return redirect('products')

    cart_item, created = UserCartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    # If product already exists in cart, increase quantity
    if not created:
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, "Product quantity updated in your cart.")
        else:
            messages.error(request, "You cannot add more than available stock.")
    else:
        messages.success(request, "Product added to your cart.")

    return redirect('products')


@login_required(login_url='/signin/')
def my_cart_view(request):
    # Show cart items only for regular users
    if request.user.is_staff:
        return redirect('admin-dashboard')

    cart_items = UserCartItem.objects.filter(
        user=request.user
    ).select_related('product')

    cart_data = []
    grand_total = 0

    # Calculate item total and grand total
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
def remove_from_cart_view(request, item_id):
    # Allow only regular users to remove cart items
    if request.user.is_staff:
        return redirect('admin-dashboard')

    cart_item = get_object_or_404(
        UserCartItem,
        id=item_id,
        user=request.user
    )

    if request.method == 'POST':
        cart_item.delete()
        messages.success(request, "Item removed from your cart.")

    return redirect('my-cart')

@login_required(login_url='/signin/')
def increase_cart_quantity_view(request, item_id):
    # Allow only regular users to increase cart quantity
    if request.user.is_staff:
        return redirect('admin-dashboard')

    cart_item = get_object_or_404(
        UserCartItem,
        id=item_id,
        user=request.user
    )

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
    # Allow only regular users to decrease cart quantity
    if request.user.is_staff:
        return redirect('admin-dashboard')

    cart_item = get_object_or_404(
        UserCartItem,
        id=item_id,
        user=request.user
    )

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
def checkout_view(request):
    # Allow only regular users to checkout
    if request.user.is_staff:
        return redirect('admin-dashboard')

    cart_items = UserCartItem.objects.filter(
        user=request.user
    ).select_related('product')

    if not cart_items.exists():
        messages.error(request, "Your cart is empty. Please add products before checkout.")
        return redirect('my-cart')

    # Process checkout only when user submits checkout request
    if request.method == 'POST':
        for item in cart_items:
            product = item.product

            # Check stock before checkout
            if item.quantity > product.stock:
                messages.error(
                    request,
                    f"Not enough stock for {product.name}. Available stock: {product.stock}."
                )
                return redirect('my-cart')

        # Reduce product stock after successful stock check
        for item in cart_items:
            product = item.product
            product.stock -= item.quantity
            product.save()

        # Clear user's cart after checkout
        cart_items.delete()

        messages.success(request, "Checkout completed successfully.")
        return redirect('products')

    return render(request, 'cart/checkout.html', {
        'cart_items': cart_items
    })


@login_required(login_url='/signin/')
def admin_product_edit_view(request, product_id):
    # Allow only staff/admin users to edit products
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to edit products.")

    product = get_object_or_404(Product, id=product_id)

    # If admin submits the edit form
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully.")
            return redirect('admin-products')

    # If admin opens the edit page normally
    else:
        form = ProductForm(instance=product)

    return render(request, 'cart/admin_product_edit.html', {
        'form': form,
        'product': product
    })


@login_required(login_url='/signin/')
def admin_product_delete_view(request, product_id):
    # Allow only staff/admin users to delete products
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to delete products.")

    product = get_object_or_404(Product, id=product_id)

    # Delete only when POST request is submitted
    if request.method == 'POST':
        product_name = product.name
        product.delete()

        messages.success(request, f"Product '{product_name}' deleted successfully.")
        return redirect('admin-products')

    return redirect('admin-products')