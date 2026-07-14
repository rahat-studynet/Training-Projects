from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.Form):
    # Form fields for user registration
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        # Check if username already exists
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username already exists.")

        return username

    def clean_email(self):
        # Check if email already exists
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")

        return email

    def clean(self):
        # Validate password and confirm password together
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Password and confirm password do not match.")

            if len(password) < 8:
                raise forms.ValidationError("Password must be at least 8 characters long.")

            if not any(char.isupper() for char in password):
                raise forms.ValidationError("Password must contain at least one capital letter.")

            if not any(char.isdigit() for char in password):
                raise forms.ValidationError("Password must contain at least one number.")

            special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

            if not any(char in special_characters for char in password):
                raise forms.ValidationError("Password must contain at least one special character.")

        return cleaned_data

    def save(self):
        # Create inactive user and wait for admin approval
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = User(
            username=username,
            email=email,
            is_active=False
        )

        # Save encrypted password, not plain text
        user.set_password(password)
        user.save()

        return user
    
class SignInForm(forms.Form):
    # Form fields for user login
    username_or_email = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)