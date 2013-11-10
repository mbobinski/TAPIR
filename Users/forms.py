from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from Users.models import JadeBusemUser
from django.forms import ModelForm
from django import forms

class RegisterForm(ModelForm):
    class Meta:
        model = JadeBusemUser
        fields = ['email', 'password', 'name', 'message']


class JadeBusemUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(JadeBusemUserCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = JadeBusemUser
        fields = ("email",)


class JadeBusemUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(JadeBusemUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = JadeBusemUser


class SignInForm(forms.Form):
    email = forms.EmailField(label='Your e-mail address')
    password = forms.CharField(widget=forms.PasswordInput())

