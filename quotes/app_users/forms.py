from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import CharField, TextInput, PasswordInput


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput())

    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = CharField(max_length=16,
                         min_length=3,
                         required=True,
                         widget=TextInput(attrs={"class": "form-control"}))
    password = CharField(required=True,
                         widget=PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'password')