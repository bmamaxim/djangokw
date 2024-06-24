from django import forms

from letter.models import Letter


class LettersForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:

        model = Letter
        fields = ('subject', 'body')
