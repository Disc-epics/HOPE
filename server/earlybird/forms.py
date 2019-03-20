from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignupForm(forms.ModelForm):
    email = forms.CharField(label="Email", widget=forms.EmailInput)
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')
