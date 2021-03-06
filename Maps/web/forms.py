from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta: #2
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)