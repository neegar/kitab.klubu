from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    last_name = forms.CharField(max_length = 50, label = "Soyadınız ")
    first_name = forms.CharField(max_length = 50, label = "Adınız " )
    username = forms.CharField(max_length = 50, label = "E-mail adresiniz")

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2'
        )

class UserLoginForm(UserCreationForm):
    username = forms.CharField(max_length = 50, label = "E-mail adresinizi daxil edin")

    class Meta:
        model = User
        fields = (
            'username',
            'password1'
        )
