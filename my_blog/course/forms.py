from django import forms


class CourseForm(forms.Form):
    name = forms.CharField(
        label="Nombre del curso",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "course-name",
                "placeholder": "Nombre de curso",
                "required": "True",
            }
        ),
    )
    code = forms.IntegerField(
        label="Código:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "course-code",
                "placeholder": "Código del curso",
                "required": "True",
            }
        ),
    )
