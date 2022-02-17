from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class user_register_form(UserCreationForm):
    email = forms.EmailField()   # email field addition

    class Meta:      # nested namespace for configs
        model = User   # model to be affected
        fields = ['username', 'email', 'password1', 'password2']   # fields in order

class user_update_form(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class profile_update_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
