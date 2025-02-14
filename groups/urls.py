from django.urls import path
from .views import (
    GroupListView, GroupDetailView, GroupCreateView,
    GroupUpdateView, GroupDeleteView
)

app_name = "groups"

urlpatterns = [
    path("", GroupListView.as_view(), name="list"),
    path("<int:year>/<int:month>/<int:day>/<slug:slug>/detail/", GroupDetailView.as_view(), name="detail"),
    path("create/", GroupCreateView.as_view(), name="create"),
    path("<int:pk>/update/", GroupUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", GroupDeleteView.as_view(), name="delete"),
]
