from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    """Admin panel for CustomUser — extends Django's built-in UserAdmin."""

    # Columns shown in the user list view
    list_display  = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'created_at']
    list_filter   = ['is_staff', 'is_superuser', 'is_active']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'phone_number']
    ordering      = ['-created_at']

    # Add our custom fields to the detail/edit form
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Extra Info', {
            'fields': ('profile_picture', 'phone_number', 'created_at'),
        }),
    )
    readonly_fields = ['created_at']

    # Add our fields to the "Add User" form
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Extra Info', {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'phone_number', 'profile_picture'),
        }),
    )
