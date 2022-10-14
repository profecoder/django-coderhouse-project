from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from profesor.models import Profesor


def create_profesor(request, name: str, last_name: str, email: str, profession: str):

    template = loader.get_template("template_profesor.html")

    profesor = Profesor(
        name=name, last_name=last_name, email=email, profession=profession
    )
    profesor.save()  # save into the DB

    context_dict = {"profesor": profesor}
    render = template.render(context_dict)
    return HttpResponse(render)


def profesors(request):
    profesors = Profesor.objects.all()

    context_dict = {"profesors": profesors}

    return render(
        request=request,
        context=context_dict,
        template_name="profesor/profesor_list.html",
    )
    