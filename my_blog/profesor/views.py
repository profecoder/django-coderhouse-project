from django.contrib import messages
from django.shortcuts import render

from profesor.models import Profesor
from profesor.forms import ProfesorForm


def get_profesors(request):
    profesors = Profesor.objects.all()
    return profesors


def create_profesor(request):
    if request.method == "POST":
        profesor_form = ProfesorForm(request.POST)
        if profesor_form.is_valid():
            data = profesor_form.cleaned_data
            actual_objects = Profesor.objects.filter(
                name=data["name"],
                last_name=data["last_name"],
                email=data["email"],
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El profesor {data['name']} - {data['last_name']} ya está creado",
                )
            else:
                profesor = Profesor(
                    name=data["name"],
                    last_name=data["last_name"],
                    email=data["email"],
                    profession=data["profession"],
                )
                profesor.save()
                messages.success(
                    request,
                    f"Profesor {data['name']} - {data['last_name']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"profesors": get_profesors(request)},
                template_name="profesor/profesor_list.html",
            )

    profesor_form = ProfesorForm(request.POST)
    context_dict = {"form": profesor_form}
    return render(
        request=request,
        context=context_dict,
        template_name="profesor/profesor_form.html",
    )


def profesors(request):
    profesors = Profesor.objects.all()

    context_dict = {"profesors": profesors}

    return render(
        request=request,
        context=context_dict,
        template_name="profesor/profesor_list.html",
    )
