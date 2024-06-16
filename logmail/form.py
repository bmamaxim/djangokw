from django import forms

from logmail.models import LogMail


class LogMailForm(forms.ModelForm):

    class Meta:
        model = LogMail
        fields = '__all__'
