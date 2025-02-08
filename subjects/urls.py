from django.urls import path
from .views import SubjectCreateView, SubjectUpdateView, SubjectDeleteView, SubjectListView, SubjectDetailView


app_name = "subjects"

urlpatterns = [
    path("", SubjectListView.as_view(), name="list"),
    path("<int:pk>/", SubjectDetailView.as_view(), name="detail"),
    path("<int:pk>/delete/", SubjectDeleteView.as_view(), name="delete"),
    path('add/', SubjectCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', SubjectUpdateView.as_view(), name='update'),
]
