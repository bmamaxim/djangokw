from django import forms

from client.models import Client
from letter.models import Letter


class StyleFormMixin:
    """
    Класс примесь стилей форм
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class LettersForm(StyleFormMixin, forms.ModelForm):

    class Meta:

        model = Letter
        fields = ('subject', 'body')
