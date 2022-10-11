from django.http import HttpResponse
from django.template import loader

from course.models import Course


def create_course(request, name: str = "course", code: int = 0):

    template = loader.get_template("template_course.html")

    course = Course(name=name, code=code)
    course.save()  # save into the DB

    context_dict = {"course": course}
    render = template.render(context_dict)
    return HttpResponse(render)
