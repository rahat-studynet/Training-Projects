from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CartItemViewSet


# Router for DRF API endpoints
router = DefaultRouter()
router.register(r'items', CartItemViewSet, basename='cartitem')


urlpatterns = [
    # Postman / DRF API routes
    path('', include(router.urls)),
]