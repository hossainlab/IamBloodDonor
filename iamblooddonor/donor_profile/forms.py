from django import forms
from .models import Profile
from django.contrib.auth.models import User

class RegisterDonorForm(forms.ModelForm):
    # DonorProfileForm
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

# DonorLoginForm
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

# DonorSignUpForm
class UserSignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget = forms.PasswordInput)
    confirm_password = forms.CharField(widget = forms.PasswordInput)
