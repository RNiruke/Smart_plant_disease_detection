"""
Accounts forms — SignupForm, LoginForm, and ProfileUpdateForm.
Uses CustomUser model and Bootstrap 5 styled widgets.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


# ─────────────────────────────────────────────────────────────────────────────
# SIGNUP FORM
# ─────────────────────────────────────────────────────────────────────────────
class SignupForm(UserCreationForm):
    """
    Registration form.
    Fields: first_name, last_name, username, email, phone_number,
            profile_picture, password1, password2.
    """

    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name',
            'autofocus': True,
        }),
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name',
        }),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email Address',
        }),
    )
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+91 9876543210 (optional)',
        }),
    )
    profile_picture = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*',
        }),
    )

    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'username',
            'email', 'phone_number', 'profile_picture',
            'password1', 'password2',
        ]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Choose a username',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password (min 8 characters)',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm Password',
        })
        for field in self.fields.values():
            field.help_text = None

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'An account with this email address already exists.'
            )
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username', '').strip()
        if CustomUser.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('This username is already taken.')
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email        = self.cleaned_data['email']
        user.first_name   = self.cleaned_data['first_name']
        user.last_name    = self.cleaned_data['last_name']
        user.phone_number = self.cleaned_data.get('phone_number', '')
        if self.cleaned_data.get('profile_picture'):
            user.profile_picture = self.cleaned_data['profile_picture']
        if commit:
            user.save()
        return user


# ─────────────────────────────────────────────────────────────────────────────
# LOGIN FORM
# ─────────────────────────────────────────────────────────────────────────────
class LoginForm(AuthenticationForm):
    """
    Login form — wraps Django's AuthenticationForm with styled widgets.
    Supports login by username.
    """

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'autofocus': True,
        }),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
        }),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password'].help_text = None

    error_messages = {
        'invalid_login': 'Incorrect username or password. Please try again.',
        'inactive': 'This account has been deactivated.',
    }


# ─────────────────────────────────────────────────────────────────────────────
# PROFILE UPDATE FORM
# ─────────────────────────────────────────────────────────────────────────────
class ProfileUpdateForm(forms.ModelForm):
    """
    Form to update user profile information.
    """
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'profile_picture']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }
