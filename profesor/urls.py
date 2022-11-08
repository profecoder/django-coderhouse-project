from django.urls import path

from profesor import views

app_name = "profesor"
urlpatterns = [
    path("profesors", views.ProfesorListView.as_view(), name="profesor-list"),
    path("profesor/add/", views.ProfesorCreateView.as_view(), name="profesor-add"),
    path("profesor/<int:pk>/detail/", views.ProfesorDetailView.as_view(), name="profesor-detail"),
    path("profesor/<int:pk>/update/", views.ProfesorUpdateView.as_view(), name="profesor-update"),
    path("profesor/<int:pk>/delete/", views.ProfesorDeleteView.as_view(), name="profesor-delete"),
]
