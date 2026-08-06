from django.forms import forms
from .models import Order

class OrderForm(forms.Form):
    class Meta():
        modle = Order

