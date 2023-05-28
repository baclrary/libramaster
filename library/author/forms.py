from django import forms
from .models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter author name',
                'required': True,
                'class': 'py-2 px-4 focus:ring-indigo-500 focus:border-indigo-500 block shadow-sm sm:text-sm border-gray-300 rounded-md',
            }),
            'surname': forms.TextInput(attrs={
                'placeholder': 'Enter author surname',
                'required': True,
                'class': 'py-2 px-4 focus:ring-indigo-500 focus:border-indigo-500 block shadow-sm sm:text-sm border-gray-300 rounded-md',
            }),
            'patronymic': forms.TextInput(attrs={
                'placeholder': 'Enter author patronymic',
                'class': 'py-2 px-4 focus:ring-indigo-500 focus:border-indigo-500 block shadow-sm sm:text-sm border-gray-300 rounded-md',
            }),
        }
