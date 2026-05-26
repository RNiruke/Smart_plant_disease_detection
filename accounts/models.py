"""
Custom User model — extends Django's AbstractUser.
Adds profile_picture, phone_number, and created_at fields.

IMPORTANT: AUTH_USER_MODEL = 'accounts.CustomUser' must be set in settings.py
BEFORE the first migration. Never change this after data exists.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Drop-in replacement for Django's default User.
    All standard fields (username, email, password, first_name, last_name,
    is_staff, is_active, date_joined, last_login) are inherited.
    """

    # Optional profile photo
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True,
        help_text='Upload a profile photo (optional)',
    )

    # Optional contact number
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        help_text='e.g. +91 9876543210',
    )

    # Auto-set timestamp when account is created
    created_at = models.DateTimeField(auto_now_add=True)

    # Tell Django which field to use as the display label in admin
    def __str__(self):
        return self.get_full_name() or self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created_at']
