from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Form to register a user
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Email is a required field
    first_name = forms.CharField()          # First name field
    last_name = forms.CharField()           # Last name field
    
    class Meta:
        model = User  # This form is associated with the User model
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']  # Fields in the form

# Form to update the user's email and username
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']  # Only allow updating username and email

# Form to update the user's profile picture
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']  # Allow updating the profile picture