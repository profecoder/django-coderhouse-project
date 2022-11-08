from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from home.models import Avatar

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label="username", min_length=3)
    first_name = forms.CharField(label="Nombre", min_length=3)
    last_name = forms.CharField(label="Apellido", min_length=3)
    email = forms.EmailField(label="Correo electrónico")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class UserUpdateForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
        ]
        widgets = {
            "email": forms.TextInput(attrs={"readonly": "readonly"}),
        }


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ("image", )
        