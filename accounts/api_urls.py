from django.urls import path
from .api_views import UserSignUpAPIView, UserLoginAPIView


urlpatterns = [
    path('signup/', UserSignUpAPIView.as_view(), name='api-signup'),
    path('login/', UserLoginAPIView.as_view(), name='api-login'),
]