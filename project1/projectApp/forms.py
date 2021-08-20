from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter User Name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
    class Meta():
        model = User
        fields = ['username', 'email', 'password']

