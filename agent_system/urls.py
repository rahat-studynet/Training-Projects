# Main project URL routing with global path exception handling
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status


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
    path('', include('Navpage.urls')),
    path('api/cart/', include('cart.urls')),

    # Catching any broken URL pattern that does not match above paths
    re_path(r'^.*$', universal_url_error_handler),
]
