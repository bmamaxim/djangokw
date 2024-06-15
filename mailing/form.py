from django import forms

from client.models import Client
from letter.models import Letter
from mailing.models import MailingLetters


class MailingLettersForm(forms.ModelForm):
    """
    Форма рассылки.
    """

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['clients'].queryset = Client.objects.filter(owner=user)
            self.fields['message'].queryset = Letter.objects.filter(writer=user)

    class Meta:
        model = MailingLetters
        exclude = ('owner',)
