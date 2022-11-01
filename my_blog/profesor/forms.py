from django import forms

from profesor.models import Profesor

class ProfesorForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre del profesor",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "profesor-name",
                "placeholder": "Nombre del profesor",
                "required": "True",
            }
        ),
    )
    last_name = forms.CharField(
        label="Apellido del profesor",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "profesor-last-name",
                "placeholder": "Apellido del profesor",
                "required": "True",
            }
        ),
    )
    email = forms.EmailField(
        label="Email:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "profesor-email",
                "placeholder": "email",
                "required": "True",
            }
        ),
    )
    profession = forms.CharField(
        label="Profesión:",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "profesor-profession",
                "placeholder": "Profesión",
                "required": "True",
            }
        ),
    )

    class Meta:
        model = Profesor
        fields = ["name", "last_name", "email", "profession"]
