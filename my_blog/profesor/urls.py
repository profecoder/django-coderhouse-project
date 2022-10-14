from django.urls import path

from profesor import views

app_name = "profesor"
urlpatterns = [
    path("profesors", views.profesors, name="profesor-list"),
]
