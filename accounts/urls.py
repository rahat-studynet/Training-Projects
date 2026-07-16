from django.urls import path
from . import views


urlpatterns = [
    # Home page
    path('', views.home_view, name='accounts-home'),

    # User authentication pages
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('logout/', views.logout_view, name='logout'),
]