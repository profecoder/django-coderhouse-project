from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from course.forms import CourseForm
from course.models import Course
from course.models import Homework


def get_courses(request):
    courses = Course.objects.all()
    paginator = Paginator(courses, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)


def create_course(request):
    if request.method == "POST":
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            data = course_form.cleaned_data
            actual_objects = Course.objects.filter(
                name=data["name"], code=data["code"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El curso {data['name']} - {data['code']} ya está creado",
                )
            else:
                course = Course(name=data["name"], code=data["code"])
                course.save()
                messages.success(
                    request,
                    f"Curso {data['name']} - {data['code']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"courses": get_courses(request)},
                template_name="course/course_list.html",
            )

    course_form = CourseForm(request.POST)
    context_dict = {"form": course_form}
    return render(
        request=request,
        context=context_dict,
        template_name="course/course_form.html",
    )


def create_homework(request, name: str, due_date: str):

    template = loader.get_template("template_homework.html")
    due_date = datetime.strptime(due_date, "%Y-%m-%d")
    homework = Homework(name=name, due_date=due_date, is_delivered=False)
    homework.save()  # save into the DB

    context_dict = {"homework": homework}
    render = template.render(context_dict)
    return HttpResponse(render)


def courses(request):
    return render(
        request=request,
        context={"courses": get_courses(request)},
        template_name="course/course_list.html",
    )


def homeworks(request):
    homeworks = Homework.objects.all()

    context_dict = {"homeworks": homeworks}

    return render(
        request=request,
        context=context_dict,
        template_name="course/homework_list.html",
    )
