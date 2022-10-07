from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context


def hello_world(request):
    return HttpResponse("Hello this is my first view in Django!!")

def title(request):
    return HttpResponse("<h1>Este es un título en H1 </h1>")

def my_name_is(request, name, age):
    # edad = int(edad)
    documentoDeTexto = f"Mi nombre es: <br><br>  {name} <br><br> Mi edad multiplicada por 2: {age*2}"
    return HttpResponse(documentoDeTexto)

def calculate_age(request, birth_day):
    birth_day = datetime.strptime(birth_day, '%Y-%m-%d')
    print(type(birth_day))
    delta_time = datetime.now() - birth_day
    days_by_year = 365.25

    http_response = '''
    <br><br>
    I'm {years} years, {months} months, {days} days old.
    '''.format(
        years=int(delta_time.days // days_by_year),
        months=int((delta_time.days % days_by_year) // 30),
        days=int((delta_time.days % days_by_year) % 30),
    )
    return HttpResponse(http_response)


def my_template(request):
    my_html = open('C:/Users/jfpin/Documents/coder_projects/borrar/django-coderhouse-project/my_blog/templates/template.html')

    template = Template(my_html.read())#Se carga en memoria nuestro documento, template1
    ##OJO importar template y contex, con: from django.template import Template, Context

    my_html.close() #Cerramos el archivo

    context = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    render = template.render(context) #Aca renderizamos la plantilla en documento

    return HttpResponse(render)