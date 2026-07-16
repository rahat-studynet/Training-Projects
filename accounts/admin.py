from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.sites import NotRegistered


# Remove default User admin before adding custom User admin
try:
    admin.site.unregister(User)
except NotRegistered:
    pass


@admin.action(description="Approve selected users")
def approve_users(modeladmin, request, queryset):
    # Mark selected users as verified
    queryset.update(is_active=True)


@admin.action(description="Mark selected users as not verified")
def mark_users_not_verified(modeladmin, request, queryset):
    # Keep superusers active for safety
    queryset.exclude(is_superuser=True).update(is_active=False)


class CustomUserAdmin(UserAdmin):
    # Show user verification status in admin list
    list_display = (
        'username',
        'email',
        'verification_status',
        'is_staff',
        'is_superuser',
    )

    # Filter users by status and role
    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
    )

    # Custom admin actions
    actions = [
        approve_users,
        mark_users_not_verified,
    ]

    def verification_status(self, obj):
        # Show clear text instead of only active/inactive icon
        if obj.is_active:
            return "Verified"

        return "Not Verified"

    verification_status.short_description = "Verification Status"


admin.site.register(User, CustomUserAdmin)