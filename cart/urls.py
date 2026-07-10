from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartItemViewSet, cart_list_screen, add_item_screen

# Creating a router and registering our ViewSet
router = DefaultRouter()
router.register(r'items', CartItemViewSet, basename='cartitem')

# Mapping the URLs to the registered router routes
urlpatterns = [
    path('', include(router.urls)),

    # UI/Frontend Screens Routes
    path('view/', cart_list_screen, name='cart-list-ui'),
    path('add/', add_item_screen, name='add-item-ui'),
]