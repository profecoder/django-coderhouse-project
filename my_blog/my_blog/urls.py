"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from course.views import create_course
from my_blog.views import (
    hello_world,
    title,
    my_name_is,
    calculate_age,
    my_template,
    template_loader,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', hello_world),
    path('title/', title),
    path('my-name-is/<str:name>/<int:age>/', my_name_is),
    path('calculate-age/<str:birth_day>/', calculate_age),
    path('template', my_template),
    path('template_loader/<str:name>/<str:last_name>', template_loader),
    path('create_course/<str:name>/<int:code>', create_course),
]
