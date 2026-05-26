"""
Run this script once to create a superuser for the admin panel.
Usage: python create_superuser.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plantdisease.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = 'admin'
password = 'Admin@1234'
email = 'admin@plantai.com'

if not User.objects.filter(username=username).exists():
    user = User.objects.create_superuser(username=username, email=email, password=password)
    print(f"[OK] Superuser '{username}' created successfully.")
    print(f"   Password: {password}")
    print(f"   Login at: http://127.0.0.1:8000/admin/")
else:
    print(f"[INFO] Superuser '{username}' already exists.")
