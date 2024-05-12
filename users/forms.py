from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from users.models import User


class UseerRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()

