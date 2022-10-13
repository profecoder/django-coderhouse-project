from django.http import HttpResponse
from django.template import loader

from student.models import Student


def create_student(request, name: str, last_name: str, email: str):

    template = loader.get_template("template_student.html")

    student = Student(name=name, last_name=last_name, email=email)
    student.save()  # save into the DB

    context_dict = {"student": student}
    render = template.render(context_dict)
    return HttpResponse(render)
