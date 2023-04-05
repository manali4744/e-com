from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class CreateUserforms(UserCreationForm):
    # phone = forms.CharField(max_length=10)
    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'password1', 'password2']