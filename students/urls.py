from django.urls import path
from students.views import (
    StudentListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
)

app_name = 'students'

urlpatterns = [
    path("", StudentListView.as_view(), name="list"),
    path("<int:pk>/", StudentDetailView.as_view(), name="detail"),
    path("add/", StudentCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", StudentUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", StudentDeleteView.as_view(), name="delete"),
]
