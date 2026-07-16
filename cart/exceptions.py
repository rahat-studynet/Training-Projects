from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import (
    ValidationError,
    NotFound,
    AuthenticationFailed,
    NotAuthenticated,
    PermissionDenied,
    MethodNotAllowed,
    ParseError,
)


def custom_api_exception_handler(exc, context):
    # First, let DRF handle the error normally
    response = exception_handler(exc, context)

    # If DRF cannot handle the error
    if response is None:
        return Response({
            "success": False,
            "error": "Internal Server Error.",
            "details": str(exc),
            "suggestion": "Please contact the backend developer."
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Item not found
    if isinstance(exc, NotFound):
        return Response({
            "success": False,
            "error": "Cart item not found.",
            "details": response.data,
            "suggestion": "The requested item ID does not exist in the database."
        }, status=status.HTTP_404_NOT_FOUND)

    # Invalid input data
    if isinstance(exc, ValidationError):
        return Response({
            "success": False,
            "error": "Validation Error.",
            "details": response.data,
            "suggestion": "Please check product_id, product_name, quantity, and price."
        }, status=status.HTTP_400_BAD_REQUEST)

    # Login/token problem
    if isinstance(exc, (AuthenticationFailed, NotAuthenticated)):
        return Response({
            "success": False,
            "error": "Authentication Error.",
            "details": response.data,
            "suggestion": "Please login or provide a valid authentication token."
        }, status=response.status_code)

    # User is logged in but not allowed
    if isinstance(exc, PermissionDenied):
        return Response({
            "success": False,
            "error": "Permission Denied.",
            "details": response.data,
            "suggestion": "You do not have permission to perform this action."
        }, status=status.HTTP_403_FORBIDDEN)

    # Wrong HTTP method
    if isinstance(exc, MethodNotAllowed):
        return Response({
            "success": False,
            "error": "Method Not Allowed.",
            "details": response.data,
            "suggestion": "Please use the correct HTTP method: GET, POST, PUT, PATCH, or DELETE."
        }, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # Invalid JSON body
    if isinstance(exc, ParseError):
        return Response({
            "success": False,
            "error": "Invalid JSON Format.",
            "details": response.data,
            "suggestion": "Please check your request body JSON syntax."
        }, status=status.HTTP_400_BAD_REQUEST)

    # Other DRF errors
    return Response({
        "success": False,
        "error": "API Execution Error.",
        "details": response.data,
        "suggestion": "Please review your request URL, credentials, headers, or field data."
    }, status=response.status_code)