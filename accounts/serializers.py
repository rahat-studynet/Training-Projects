from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import serializers


class UserSignUpAPISerializer(serializers.Serializer):
    # API signup fields
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate_username(self, value):
        # Check duplicate username
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username already exists.")

        return value

    def validate_email(self, value):
        # Check duplicate email
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already registered.")

        return value

    def validate(self, data):
        # Check password and confirm password
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError("Password and confirm password do not match.")

        if len(password) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")

        if not any(char.isupper() for char in password):
            raise serializers.ValidationError("Password must contain at least one capital letter.")

        if not any(char.isdigit() for char in password):
            raise serializers.ValidationError("Password must contain at least one number.")

        special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

        if not any(char in special_characters for char in password):
            raise serializers.ValidationError("Password must contain at least one special character.")

        return data

    def create(self, validated_data):
        # Remove confirm_password because it is not saved in database
        validated_data.pop('confirm_password')

        password = validated_data.pop('password')

        # Create inactive user for admin approval
        user = User(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            is_active=False
        )

        # Save encrypted password
        user.set_password(password)
        user.save()

        return user


class UserLoginAPISerializer(serializers.Serializer):
    # API login fields
    username_or_email = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username_or_email = data.get('username_or_email')
        password = data.get('password')

        # Find user by username or email
        user = User.objects.filter(
            Q(username=username_or_email) | Q(email=username_or_email)
        ).first()

        if user is None:
            raise serializers.ValidationError("No account found with this username or email.")

        if not user.check_password(password):
            raise serializers.ValidationError("Incorrect password.")

        if not user.is_active:
            raise serializers.ValidationError("Your account is not approved by admin yet.")

        # Store user for API view
        data['user'] = user

        return data