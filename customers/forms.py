from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Review,Order

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ["stars","comment"]

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ["state",'city','postal_code']