from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.sites import NotRegistered


# Unregister default User admin first
try:
    admin.site.unregister(User)
except NotRegistered:
    pass


# Admin action to approve selected users
@admin.action(description="Approve selected users")
def approve_users(modeladmin, request, queryset):
    # Set selected users as active/verified
    queryset.update(is_active=True)


# Admin action to mark selected users as not verified
@admin.action(description="Mark selected users as not verified")
def mark_users_not_verified(modeladmin, request, queryset):
    # Do not deactivate superusers for safety
    queryset.exclude(is_superuser=True).update(is_active=False)


class CustomUserAdmin(UserAdmin):
    # Show extra verification status in user list
    list_display = (
        'username',
        'email',
        'verification_status',
        'is_staff',
        'is_superuser',
    )

    # Add filter options on the right side
    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
    )

    # Add admin actions
    actions = [
        approve_users,
        mark_users_not_verified,
    ]

    def verification_status(self, obj):
        # Show readable verification text instead of only icon
        if obj.is_active:
            return "Verified"
        return "Not Verified"

    verification_status.short_description = "Verification Status"


# Register User model with custom admin
admin.site.register(User, CustomUserAdmin)