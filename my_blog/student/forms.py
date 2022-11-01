from django import forms

from student.models import Student

class StudentForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre del estudiante",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "student-name",
                "placeholder": "Nombre del estudiante",
                "required": "True",
            }
        ),
    )
    last_name = forms.CharField(
        label="Apellido del estudiante",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "student-last-name",
                "placeholder": "Apellido del estudiante",
                "required": "True",
            }
        ),
    )
    email = forms.EmailField(
        label="Email:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "student-email",
                "placeholder": "email",
                "required": "True",
            }
        ),
    )

    class Meta:
        model = Student
        fields = ["name", "last_name", "email"]
