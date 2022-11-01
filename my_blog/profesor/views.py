from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from profesor.models import Profesor
from profesor.forms import ProfesorForm


class ProfesorListView(ListView):
    model = Profesor
    paginate_by = 3


class ProfesorDetailView(DetailView):
    model = Profesor
    fields = ["name", "last_name", "email", "profession"]


class ProfesorCreateView(LoginRequiredMixin, CreateView):
    model = Profesor
    success_url = reverse_lazy("profesor:profesor-list")

    form_class = ProfesorForm

    def form_valid(self, form):
        """Filter to avoid duplicate profesors"""
        data = form.cleaned_data
        actual_objects = Profesor.objects.filter(
            name=data["name"],
            last_name=data["last_name"],
            email=data["email"],
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El Profesor {data['name']} {data['last_name']} | {data['email']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Profesor: {data['name']} - {data['last_name']}. Creado exitosamente!",
            )
            return super().form_valid(form)


class ProfesorUpdateView(LoginRequiredMixin, UpdateView):
    model = Profesor
    fields = ["name", "last_name", "email", "profession"]

    def get_success_url(self):
        profesor_id = self.kwargs["pk"]
        return reverse_lazy("profesor:profesor-detail", kwargs={"pk": profesor_id})


class ProfesorDeleteView(LoginRequiredMixin, DeleteView):
    model = Profesor
    success_url = reverse_lazy("profesor:profesor-list")
