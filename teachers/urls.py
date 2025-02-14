from django.urls import path
from .views import TeacherListView, TeacherDetailView, TeacherCreateView, TeacherUpdateView, TeacherDeleteView

app_name = 'teachers'

urlpatterns = [
    path('', TeacherListView.as_view(), name='list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/detail/', TeacherDetailView.as_view(), name='detail'),
    path('create/', TeacherCreateView.as_view(), name='create'),
    path('<int:pk>/update/', TeacherUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', TeacherDeleteView.as_view(), name='delete'),
]
