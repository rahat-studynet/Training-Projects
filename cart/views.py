from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication

from .models import CartItem
from .serializers import CartItemSerializer


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