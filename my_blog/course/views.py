from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from course.models import Course


def create_course(request, name: str, code: int):

    template = loader.get_template("template_course.html")

    course = Course(name=name, code=code)
    course.save()  # save into the DB

    context_dict = {"course": course}
    render = template.render(context_dict)
    return HttpResponse(render)


def courses(request):
    courses = Course.objects.all()

    context_dict = {"courses": courses}

    return render(
        request=request,
        context=context_dict,
        template_name="course/course_list.html",
    )
