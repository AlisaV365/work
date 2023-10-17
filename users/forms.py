from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import EmailField

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)
        field_classes = {'email': EmailField}


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('surname', 'email', 'phone', 'chat_id')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
