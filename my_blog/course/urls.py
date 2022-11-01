from django.urls import path

from course import views

app_name = "course"
urlpatterns = [
    path("courses/", views.CourseListView.as_view(), name="course-list"),
    path("course/add/", views.CourseCreateView.as_view(), name="course-add"),
    path("course/<int:pk>/detail/", views.CourseDetailView.as_view(), name="course-detail"),
    path("course/<int:pk>/update/", views.CourseUpdateView.as_view(), name="course-update"),
    path("course/<int:pk>/delete/", views.CourseDeleteView.as_view(), name="course-delete"),
    path("comment/<int:pk>/add/", views.CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),

    path("homeworks", views.HomeworkListView.as_view(), name="homework-list"),
    path("homework/add/", views.HomeworkCreateView.as_view(), name="homework-add"),
    path("homework/<int:pk>/detail/", views.HomeworkDetailView.as_view(), name="homework-detail"),
    path("homework/<int:pk>/update/", views.HomeworkUpdateView.as_view(), name="homework-update"),
    path("homework/<int:pk>/delete/", views.HomeworkDeleteView.as_view(), name="homework-delete"),
]
