from django import forms
from .models import Book
from author.models import Author


class BookForm(forms.ModelForm):
    author_ids = forms.CharField(
        label='Author(s)',
        required=True,
        widget=forms.TextInput(attrs={
            'class': "py-2 px-4 focus:ring-indigo-500 focus:border-indigo-500 block shadow-sm sm:text-sm border-gray-300 rounded-md"
        }),
    )

    class Meta:
        model = Book
        fields = ['name', 'description', 'count', 'cover_image']
        labels = {
            'name': 'Title',
            'description': 'Description',
            'count': 'Count',
            'cover_image': 'Cover',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'py-2 px-4 focus:ring-indigo-500 focus:border-indigo-500 block shadow-sm sm:text-sm border-gray-300 rounded-md',
            }),
            'description': forms.Textarea(attrs={
                'class': 'py-2 px-4 focus:ring-indigo-500 focus:border-indigo-500 block shadow-sm sm:text-sm border-gray-300 rounded-md',
                'rows': 3,
            }),
            'count': forms.NumberInput(attrs={
                'class': 'py-2 px-4 focus:ring-indigo-500 focus:border-indigo-500 block shadow-sm sm:text-sm border-gray-300 rounded-md',
            }),
            'cover_image': forms.ClearableFileInput(attrs={
                'class': 'mb-4 block w-full border border-gray-200 shadow-sm rounded-md text-sm focus:z-10 focus:border-blue-500 focus:ring-blue-500 dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 file:bg-transparent file:border-0 file:bg-gray-100 file:mr-4 file:py-3 file:px-4 dark:file:bg-gray-700 dark:file:text-gray-400',
            }),
        }

    # def __init__(self, *args, **kwargs):
    #     super(BookForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].required = True
    #     self.fields['description'].required = True
    #     self.fields['count'].required = True
    #
    #     # Reorder the form fields
    #     self.fields = self.order_fields(['name', 'author_ids', 'description', 'count', 'cover_image'])