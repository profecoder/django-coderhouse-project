from django import forms


class ProfesorForm(forms.Form):
    name = forms.CharField(
        label="Nombre del profesor",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "profesor-name",
                "placeholder": "Nombre de profesor",
                "required": "True",
            }
        ),
    )
    last_name = forms.CharField(
        label="Apellido del profesor",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "profesor-las-name",
                "placeholder": "Apellido de profesor",
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
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "profesor-profession",
                "placeholder": "Profesión",
                "required": "True",
            }
        ),
    )
