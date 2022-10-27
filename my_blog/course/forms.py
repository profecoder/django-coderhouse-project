from ckeditor.widgets import CKEditorWidget
from django import forms

from course.models import Course


class CourseForm(forms.ModelForm):
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

    description = forms.CharField(
        label="Descripción:",
        required=False,
        widget=CKEditorWidget(
            attrs={
                "class": "course-description",
                "placeholder": "Descripcion del curso",
                "required": "True",
            }
        ),
    )

    class Meta:
        model = Course
        fields = ["name", "code", "description"]
