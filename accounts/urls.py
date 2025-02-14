from django.urls import path
from .views import SignUpView, UserLoginView, ProfileView, LogoutView, LogoutSuccessView, DashboardView,enrollment_data, subject_distribution


app_name = "accounts"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('api/enrollment-data/', enrollment_data, name='enrollment_data'),
    path('api/subject-distribution/', subject_distribution, name='subject_distribution'),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("logout-success/", LogoutSuccessView.as_view(), name="logout_success"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
]