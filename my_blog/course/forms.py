from ckeditor.widgets import CKEditorWidget
from django import forms

from course.models import Course
from course.models import Homework


class CourseForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre del curso",
        max_length=40,
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
        widget=CKEditorWidget(),
    )

    class Meta:
        model = Course
        fields = ["name", "code", "description"]


class HomeworkForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre del entregable",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "homework-name",
                "placeholder": "Nombre del entregable",
                "required": "True",
            }
        ),
    )

    due_date = forms.DateField(
        label="Vencimiento de la entrega:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "homework-code",
                "placeholder": "Fecha yyyy-mm-dd",
                "required": "True",
            }
        ),
    )

    is_delivered = forms.BooleanField(
        label="Entregado:",
        required=False,
    )

    class Meta:
        model = Homework
        fields = ["name", "due_date", "is_delivered"]
