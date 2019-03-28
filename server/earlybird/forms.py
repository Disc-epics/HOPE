from .models import User
from .models import Client
from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignupForm(forms.ModelForm):
    email = forms.CharField(label="Email", widget=forms.EmailInput)
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

class AddClient(forms.ModelForm):
	first_name = forms.CharField(label="First Name")
	last_name = forms.CharField(label="Last Name")
	middle_name = forms.CharField(label="Middle Name")

	class Meta:
	    model = Client
	    fields = ('first_name', 'last_name', 'middle_name')
