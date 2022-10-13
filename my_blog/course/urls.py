from django.urls import path

from course import views

app_name = "course"
urlpatterns = [
    path("courses", views.courses, name="course-list"),
]
