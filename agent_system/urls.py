# Main project URL routing with global path exception handling
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from cart import views as cart_views
from django.conf import settings
from django.conf.urls.static import static


# Custom fallback function when a user hits an invalid URL or misses a slash
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([AllowAny])
def universal_url_error_handler(request, exception=None):
    return Response({
        "success": False,
        "error": "URL Syntax Error or Missing Trailing Slash.",
        "details": f"The path '{request.path}' does not match any valid endpoint.",
        "suggestion": "Please verify your endpoint path and make sure it ends with slash (/). Example: /api/cart/items/5/"
    }, status=status.HTTP_400_BAD_REQUEST)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('accounts.urls')),

    path('admin-dashboard/', cart_views.admin_dashboard_view, name='admin-dashboard'),
    path('admin-products/', cart_views.admin_product_list_view, name='admin-products'),
    path('admin-products/add/', cart_views.admin_product_add_view, name='admin-product-add'),
    path('admin-products/edit/<int:product_id>/', cart_views.admin_product_edit_view, name='admin-product-edit'),
    path('admin-products/delete/<int:product_id>/', cart_views.admin_product_delete_view, name='admin-product-delete'),

    path('products/', cart_views.product_list_view, name='products'),
    path('add-to-cart/<int:product_id>/', cart_views.add_to_cart_view, name='add-to-cart'),
    path('my-cart/', cart_views.my_cart_view, name='my-cart'),
    path('remove-from-cart/<int:item_id>/', cart_views.remove_from_cart_view, name='remove-from-cart'),
    path('increase-cart/<int:item_id>/', cart_views.increase_cart_quantity_view, name='increase-cart'),
    path('decrease-cart/<int:item_id>/', cart_views.decrease_cart_quantity_view, name='decrease-cart'),
    path('checkout/', cart_views.checkout_view, name='checkout'),

    path('api/cart/', include('cart.urls')),

]


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Catching any broken URL pattern that does not match above paths
# Catching any broken URL pattern must stay at the very bottom
urlpatterns += [
    re_path(r'^.*$', universal_url_error_handler),
]