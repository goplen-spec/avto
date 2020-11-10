from django import forms
from django.core.validators import validate_email
from django.contrib.auth.models import User


class ValidateLoginForm(forms.ModelForm):
    email = forms.EmailField(required=True, validators=[validate_email],
                             label='Email', widget=forms.EmailInput(attrs={'class': 'form_tel'}))
    password = forms.CharField(label='password',
                               widget=forms.PasswordInput(attrs={'class': 'form_tel'}))

    class Meta:
        model = User
        fields = ('email', 'password')
