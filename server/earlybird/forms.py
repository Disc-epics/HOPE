from .models import User
from .models import Client
from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignupForm(forms.ModelForm):
    email = forms.CharField(
        label="Email", widget=forms.EmailInput(attrs={'class': 'in'}))
    first_name = forms.CharField(
        label="First Name", widget=forms.TextInput(attrs={'class': 'in'}))
    last_name = forms.CharField(
        label="Last Name", widget=forms.TextInput(attrs={'class': 'in'}))
    phone_number = forms.CharField(
        label="Phone Number", widget=forms.TextInput(attrs={'class': 'in'}))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_number')


class AddClient(forms.ModelForm):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    middle_name = forms.CharField(label="Middle Name", required=False)

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'middle_name')
