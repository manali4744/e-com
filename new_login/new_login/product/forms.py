from django.forms import ModelForm
from .models import Order
from django import forms
import re
from django.core.exceptions import ValidationError

class OrderForm(ModelForm):
    customer = forms.CharField(max_length= 255)
    product = forms.CharField(max_length= 255)
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Quantity'}))
    class Meta:
        model = Order
        fields = ['customer', 'product', 'quantity']

        