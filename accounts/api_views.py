from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.authtoken.models import Token

from .serializers import UserSignUpAPISerializer, UserLoginAPISerializer


class UserSignUpAPIView(APIView):
    # Public API for user signup
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSignUpAPISerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            return Response({
                "success": True,
                "message": "Account created successfully. Please wait for admin approval.",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "is_active": user.is_active,
                    "is_staff": user.is_staff
                }
            }, status=status.HTTP_201_CREATED)

        return Response({
            "success": False,
            "error": "Validation Error.",
            "details": serializer.errors,
            "suggestion": "Please check username, email, password, and confirm password."
        }, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    # Public API for user login
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginAPISerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data.get('user')

            # Create or get existing token
            token, created = Token.objects.get_or_create(user=user)

            # Role-based redirect URL
            if user.is_staff:
                redirect_url = "/admin-dashboard/"
            else:
                redirect_url = "/products/"

            return Response({
                "success": True,
                "message": "Login successful.",
                "token": token.key,
                "redirect_url": redirect_url,
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "is_active": user.is_active,
                    "is_staff": user.is_staff,
                    "is_superuser": user.is_superuser
                }
            }, status=status.HTTP_200_OK)

        return Response({
            "success": False,
            "error": "Login Failed.",
            "details": serializer.errors,
            "suggestion": "Please check username/email, password, and admin approval status."
        }, status=status.HTTP_400_BAD_REQUEST)