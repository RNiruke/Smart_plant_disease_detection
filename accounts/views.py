"""
Accounts views — signup, login, logout, and user profile management.

Security practices applied:
  - CSRF via {% csrf_token %} in all forms
  - @login_required guard on protected pages
  - Redirect guard prevents authenticated users re-visiting login/signup
  - Safe ?next= redirect (only allows internal URLs)
  - Password hashing handled entirely by Django's auth system
  - Flash messages on every action
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from .forms import SignupForm, LoginForm, ProfileUpdateForm


# ─────────────────────────────────────────────────────────────────────────────
# SIGNUP
# ─────────────────────────────────────────────────────────────────────────────
def signup_view(request):
    """
    Register a new user.
    - GET  → show blank signup form
    - POST → validate, save user, auto-login, redirect to dashboard
    """
    if request.user.is_authenticated:
        return redirect('dashboard:home')

    form = SignupForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request,
                f'Welcome to PlantAI, {user.first_name or user.username}! '
                f'Your account has been created successfully.'
            )
            return redirect('dashboard:home')
        else:
            messages.error(request, 'Please correct the errors highlighted below.')

    return render(request, 'accounts/signup.html', {
        'form': form,
        'title': 'Create Account',
    })


# ─────────────────────────────────────────────────────────────────────────────
# LOGIN
# ─────────────────────────────────────────────────────────────────────────────
def login_view(request):
    """
    Authenticate and log in an existing user.
    - GET  → show blank login form
    - POST → validate credentials, login, redirect to ?next or dashboard
    """
    if request.user.is_authenticated:
        return redirect('dashboard:home')

    form = LoginForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(
                request,
                f'Welcome back, {user.first_name or user.username}!'
            )
            next_url = request.GET.get('next', '').strip()
            if next_url and next_url.startswith('/') and ' ' not in next_url:
                return redirect(next_url)
            return redirect('dashboard:home')
        else:
            messages.error(request, 'Incorrect username or password. Please try again.')

    return render(request, 'accounts/login.html', {
        'form': form,
        'title': 'Sign In',
    })


# ─────────────────────────────────────────────────────────────────────────────
# LOGOUT
# ─────────────────────────────────────────────────────────────────────────────
def logout_view(request):
    """
    Log out the current user.
    """
    username = request.user.username
    logout(request)
    messages.info(request, f'You have been logged out, {username}. See you soon!')
    return redirect('landing')


# ─────────────────────────────────────────────────────────────────────────────
# USER PROFILE
# ─────────────────────────────────────────────────────────────────────────────
@login_required
def profile_view(request):
    """
    Manage user profile and security.
    Allows updating personal details and changing passwords in tabbed panel.
    """
    user = request.user
    active_tab = 'info'

    # Initialize forms
    profile_form = ProfileUpdateForm(instance=user)
    password_form = PasswordChangeForm(user=user)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'update_profile':
            profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=user)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Your profile details have been updated successfully.')
                return redirect('accounts:profile')
            else:
                messages.error(request, 'Please correct the errors in the profile form.')

        elif action == 'change_password':
            active_tab = 'security'
            password_form = PasswordChangeForm(user=user, data=request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Prevents logout
                messages.success(request, 'Your password was successfully updated!')
                return redirect('accounts:profile')
            else:
                messages.error(request, 'Please correct the password errors below.')

    return render(request, 'accounts/profile.html', {
        'title': 'My Profile',
        'profile_form': profile_form,
        'password_form': password_form,
        'active_tab': active_tab,
    })
