from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

inputClass = """w-full py-2 px-4 mb-1 bg-gray-300 text-gray-700 leading-tight rounded border-2
    border-gray-300 appearance-none focus:outline-none focus:bg-white focus:border-indigo-700"""


class UserSignupForm(UserCreationForm):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : inputClass}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : inputClass}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : inputClass}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class' : inputClass}),
        }


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={'class': inputClass}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': inputClass}))
