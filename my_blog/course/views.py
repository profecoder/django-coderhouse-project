from django.contrib import messages
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.shortcuts import render

from course.forms import CourseForm
from course.models import Course
from course.models import Homework


def get_courses(request):
    courses = Course.objects.all()
    paginator = Paginator(courses, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)


def courses(request):
    return render(
        request=request,
        context={"course_list": get_courses(request)},
        template_name="course/course_list.html",
    )


def course_create(request):
    if request.method == "POST":
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            data = course_form.cleaned_data
            actual_objects = Course.objects.filter(
                name=data["name"], code=data["code"]
            ).count()
            print("actual_objects", actual_objects)
            if not actual_objects:
                course = Course(
                    name=data["name"],
                    code=data["code"],
                    description=data["description"],
                )
                course.save()
                messages.success(
                    request,
                    f"Curso {data['name']} - {data['code']} creado exitosamente!",
                )
                return render(
                    request=request,
                    context={"course_list": get_courses(request)},
                    template_name="course/course_list.html",
                )
            else:
                messages.error(
                    request,
                    f"El curso {data['name']} - {data['code']} ya está creado",
                )

    course_form = CourseForm(request.POST)
    context_dict = {"form": course_form}
    return render(
        request=request,
        context=context_dict,
        template_name="course/course_form.html",
    )


def course_detail(request, pk: int):
    return render(
        request=request,
        context={"course": Course.objects.get(pk=pk)},
        template_name="course/course_detail.html",
    )


def course_update(request, pk: int):
    course = Course.objects.get(pk=pk)

    if request.method == "POST":
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            data = course_form.cleaned_data
            course.name = data["name"]
            course.code = data["code"]
            course.description = data["description"]
            course.save()

            return render(
                request=request,
                context={"course": course},
                template_name="course/course_detail.html",
            )

    course_form = CourseForm(model_to_dict(course))
    context_dict = {
        "course": course,
        "form": course_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name="course/course_form.html",
    )


def course_delete(request, pk: int):
    course = Course.objects.get(pk=pk)
    if request.method == "POST":
        course.delete()

        courses = Course.objects.all()
        context_dict = {"course_list": courses}
        return render(
            request=request,
            context=context_dict,
            template_name="course/course_list.html",
        )

    context_dict = {
        "course": course,
    }
    return render(
        request=request,
        context=context_dict,
        template_name="course/course_confirm_delete.html",
    )


def homeworks(request):
    homeworks = Homework.objects.all()

    context_dict = {"homeworks": homeworks}

    return render(
        request=request,
        context=context_dict,
        template_name="course/homework_list.html",
    )


from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from course.models import Course


class CourseListView(ListView):
    model = Course
    paginate_by = 3


class CourseDetailView(DetailView):
    model = Course
    fields = ["name", "code", "description"]


class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy("course:course-list")

    form_class = CourseForm
    # fields = ["name", "code", "description"]

    def form_valid(self, form):
        """Filter to avoid duplicate courses"""
        data = form.cleaned_data
        actual_objects = Course.objects.filter(
            name=data["name"], code=data["code"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El curso {data['name']} - {data['code']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Curso {data['name']} - {data['code']} creado exitosamente!",
            )
            return super().form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    fields = ["name", "code", "description"]

    def get_success_url(self):
        course_id = self.kwargs["pk"]
        return reverse_lazy("course:course-detail", kwargs={"pk": course_id})


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy("course:course-list")
