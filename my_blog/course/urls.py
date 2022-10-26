from django.urls import path

from course import views

app_name = "course"
urlpatterns = [
    path("courses", views.courses, name="course-list"),
    path("course/add", views.create_course, name="course-add"),
    path("homeworks", views.homeworks, name="homework-list"),
]
