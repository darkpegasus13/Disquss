from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter Username'
        }))
    first_name = forms.CharField(required=True,widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter First Name'
        }))
    last_name = forms.CharField(required=True,widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter Last Name'
        }))
    email = forms.EmailField(required=True,widget=forms.TextInput(
        attrs={
            'placeholder': 'Example abc@xyz.com'
        }))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
                'placeholder':"Your password must contain at least 8 character and cannot be entirely numeric."
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': "Enter the same password as before, for verification."
        }
    ))
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user


class Loginform(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput
    (attrs={
        'class': 'form-control',
        'placeholder': "Enter Username"
    }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
    attrs={
        'class': 'form-control',
       'placeholder': "Enter Password"
    }
    ))


