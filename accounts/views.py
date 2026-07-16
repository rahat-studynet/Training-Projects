from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout as auth_logout
from django.db.models import Q

from .forms import SignUpForm, SignInForm


def home_view(request):
    # Show home page
    return render(request, 'accounts/home.html')


def signup_view(request):
    # Handle new user registration
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please wait for admin approval.")
            return redirect('signin')

    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})


def signin_view(request):
    # Handle user login
    if request.method == 'POST':
        form = SignInForm(request.POST)

        if form.is_valid():
            username_or_email = form.cleaned_data.get('username_or_email')
            password = form.cleaned_data.get('password')

            # Find user using username or email
            user = User.objects.filter(
                Q(username=username_or_email) | Q(email=username_or_email)
            ).first()

            if user is None:
                messages.error(request, "No account found with this username or email.")
                return redirect('signin')

            # Check password
            if not user.check_password(password):
                messages.error(request, "Incorrect password.")
                return redirect('signin')

            # Check admin approval
            if not user.is_active:
                messages.error(request, "Your account is not approved by admin yet.")
                return redirect('signin')

            # Login approved user
            login(request, user)

            # Role-based redirect
            if user.is_staff:
                return redirect('admin-dashboard')

            return redirect('products')

    else:
        form = SignInForm()

    return render(request, 'accounts/signin.html', {'form': form})


def logout_view(request):
    # Logout user and return to home page
    auth_logout(request)
    messages.success(request, "You have logged out successfully.")
    return redirect('accounts-home')