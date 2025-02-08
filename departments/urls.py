from django.urls import path
from .views import DepartmentListView, DepartmentDetailView, DepartmentCreateView, DepartmentUpdateView, DepartmentDeleteView


app_name = 'departments'

urlpatterns = [
    path('', DepartmentListView.as_view(), name='list'),
    path('<int:pk>/', DepartmentDetailView.as_view(), name='detail'),
    path('create/', DepartmentCreateView.as_view(), name='create'),
    path('<int:pk>/update/', DepartmentUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', DepartmentDeleteView.as_view(), name='delete'),
]
