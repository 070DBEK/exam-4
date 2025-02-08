from django.urls import path
from .views import (
    DirectorListView, DirectorDetailView, DirectorCreateView,
    DirectorUpdateView, DirectorDeleteView
)


app_name = 'directors'

urlpatterns = [
    path('', DirectorListView.as_view(), name="list"),
    path('<int:pk>/', DirectorDetailView.as_view(), name="detail"),
    path('add/', DirectorCreateView.as_view(), name="create"),
    path('<int:pk>/edit/', DirectorUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', DirectorDeleteView.as_view(), name="delete"),
]
