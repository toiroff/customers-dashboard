from django import forms
from .models import Order,Customer

#REGISTER FORM
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'product', 'status','note']


class CreationUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

   