from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'bg-gray-200 border rounded text-xs font-medium leading-none placeholder-gray-800 text-gray-800 py-3 w-full pl-3 mt-2',
        'placeholder': 'e.g: john@gmail.com'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'bg-gray-200 border rounded text-xs font-medium leading-none text-gray-800 py-3 w-full pl-3 mt-2',
    }))

    error_messages = {
        'invalid_login': 'Invalid email or password',
    }


class RegisterForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'email',
            'type': 'email',
            'class': 'bg-gray-200 border rounded text-xs font-medium leading-none placeholder-gray-800 text-gray-800 py-3 w-full pl-3 mt-2',
            'placeholder': 'e.g: john@gmail.com'
        })
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'id': 'myInput',
            'class': 'bg-gray-200 border rounded text-xs font-medium leading-none text-gray-800 py-3 w-full pl-3 mt-2',
        })
    )
    first_name = forms.CharField(
        required=True,
        label='First name',
        widget=forms.TextInput(attrs={
            'id': 'first_name',
            'class': 'bg-gray-200 border rounded text-xs font-medium leading-none placeholder-gray-800 text-gray-800 py-3 w-full pl-3 mt-2',
            'placeholder': 'e.g: Tommy'
        })
    )
    middle_name = forms.CharField(
        required=False,
        label='Middle name',
        widget=forms.TextInput(attrs={
            'id': 'middle_name',
            'class': 'bg-gray-200 border rounded text-xs font-medium leading-none placeholder-gray-800 text-gray-800 py-3 w-full pl-3 mt-2',
            'placeholder': 'e.g: Donald'
        })
    )
    last_name = forms.CharField(
        required=True,
        label='Last name',
        widget=forms.TextInput(attrs={
            'id': 'last_name',
            'class': 'bg-gray-200 border rounded text-xs font-medium leading-none placeholder-gray-800 text-gray-800 py-3 w-full pl-3 mt-2',
            'placeholder': 'e.g: Reuben'
        })
    )
    role = forms.ChoiceField(
        required=True,
        choices=(
            ('0', 'Visitor'),
            ('1', 'Librarian')
        ),
        widget=forms.Select(attrs={
            'class': 'bg-gray-200 border rounded text-xs font-medium leading-none placeholder-gray-800 text-gray-800 py-3 w-full pl-3 mt-2',
        })
    )