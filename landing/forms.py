from django import forms
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Div

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """Форма обратной связи"""
    
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full', 'placeholder': _('Ваше имя')}),
            'email': forms.EmailInput(attrs={'class': 'w-full', 'placeholder': _('Email')}),
            'phone': forms.TextInput(attrs={'class': 'w-full', 'placeholder': _('Телефон')}),
            'message': forms.Textarea(attrs={'class': 'w-full', 'rows': 4, 'placeholder': _('Сообщение')}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'space-y-4'
        self.helper.layout = Layout(
            Div(
                Field('name', css_class='rounded-lg p-3 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500'),
                css_class='mb-4'
            ),
            Div(
                Field('email', css_class='rounded-lg p-3 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500'),
                css_class='mb-4'
            ),
            Div(
                Field('phone', css_class='rounded-lg p-3 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500'),
                css_class='mb-4'
            ),
            Div(
                Field('message', css_class='rounded-lg p-3 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500'),
                css_class='mb-6'
            ),
            Div(
                Submit('submit', _('Отправить'), css_class='w-full py-3 px-4 bg-blue-600 hover:bg-blue-700 text-white font-bold rounded-lg transition duration-200'),
                css_class='text-center'
            ),
        )