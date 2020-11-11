from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ScriptSpinnerUser

class ScriptSpinnerUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = ScriptSpinnerUser
        fields = ('email',)

class ScriptSpinnerUserChangeForm(UserChangeForm):
    class Meta:
        model = ScriptSpinnerUser
        fields = ('email',)

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    
    class Meta:
        model = ScriptSpinnerUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, help_text='Email Address')
    password = forms.CharField(max_length=100, help_text='Password', widget=forms.PasswordInput)