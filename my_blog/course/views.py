from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from course.forms import CourseForm
from course.forms import HomeworkForm
from course.models import Course
from course.models import Homework


class CourseListView(ListView):
    model = Course
    paginate_by = 3


class CourseDetailView(DetailView):
    model = Course
    fields = ["name", "code", "description"]


class CourseCreateView(LoginRequiredMixin, CreateView):
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


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    fields = ["name", "code", "description"]

    def get_success_url(self):
        course_id = self.kwargs["pk"]
        return reverse_lazy("course:course-detail", kwargs={"pk": course_id})


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy("course:course-list")


class HomeworkListView(ListView):
    model = Homework
    paginate_by = 4


class HomeworkCreateView(LoginRequiredMixin, CreateView):
    model = Homework
    success_url = reverse_lazy("course:homework-list")

    form_class = HomeworkForm

    def form_valid(self, form):
        """Filter to avoid duplicate homeworks"""
        data = form.cleaned_data
        actual_objects = Homework.objects.filter(name=data["name"]).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El entregable {data['name']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Entregable: {data['name']}. Creado exitosamente!",
            )
            return super().form_valid(form)


class HomeworkDetailView(DetailView):
    model = Homework
    fields = ["name", "due_date", "is_delivered"]


class HomeworkUpdateView(LoginRequiredMixin, UpdateView):
    model = Homework
    fields = ["name", "due_date", "is_delivered"]

    def get_success_url(self):
        homework_id = self.kwargs["pk"]
        return reverse_lazy("course:homework-detail", kwargs={"pk": homework_id})


class HomeworkDeleteView(LoginRequiredMixin, DeleteView):
    model = Homework
    success_url = reverse_lazy("course:homework-list")
