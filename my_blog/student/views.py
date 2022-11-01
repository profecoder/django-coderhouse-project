from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from student.models import Student
from student.forms import StudentForm


class StudentListView(ListView):
    model = Student
    paginate_by = 3


class StudentDetailView(DetailView):
    model = Student
    fields = ["name", "last_name", "email"]


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    success_url = reverse_lazy("student:student-list")

    form_class = StudentForm

    def form_valid(self, form):
        """Filter to avoid duplicate students"""
        data = form.cleaned_data
        actual_objects = Student.objects.filter(
            name=data["name"],
            last_name=data["last_name"],
            email=data["email"],
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El Estudiente {data['name']} {data['last_name']} | {data['email']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Estudiente: {data['name']} - {data['last_name']}. Creado exitosamente!",
            )
            return super().form_valid(form)


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    fields = ["name", "last_name", "email"]

    def get_success_url(self):
        student_id = self.kwargs["pk"]
        return reverse_lazy("student:student-detail", kwargs={"pk": student_id})


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy("student:student-list")
