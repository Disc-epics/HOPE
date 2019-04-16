from .models import User
from .models import Client
from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignupForm(forms.ModelForm):
    email = forms.CharField(
        label="Email")
    first_name = forms.CharField(
        label="First Name")
    last_name = forms.CharField(
        label="Last Name")
    phone_number = forms.CharField(
        label="Phone Number")

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


class ChangePassword(forms.Form):
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput())

    class Meta:
        fields = ('password', 'password2')


class ForgotPassword(forms.Form):
    email = forms.CharField(
        label="Email", widget=forms.EmailInput(attrs={'class': 'in'}))

    class Meta:
        fields = ('email')
