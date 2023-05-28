from django import forms
from order.models import Order
from authentication.models import CustomUser
from book.models import Book


class OrderForm(forms.ModelForm):
    date = forms.DateField(required=False, widget=forms.TextInput(attrs={
        'type': 'date',
        'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'}))
    time = forms.TimeField(required=False, widget=forms.TextInput(attrs={
        'type': 'time',
        'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'}))

    class Meta:
        model = Order
        fields = ['book']
        widgets = {
            'book': forms.Select(attrs={
                'class': 'py-2 px-4 focus:ring-indigo-500 focus:border-indigo-500 block shadow-sm sm:text-sm border-gray-300 rounded-md'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.all()