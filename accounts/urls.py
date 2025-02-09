from django.urls import path
from .views import SignUpView, UserLoginView, ProfileView, LogoutView, LogoutSuccessView, DashboardView


app_name = "accounts"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("logout-success/", LogoutSuccessView.as_view(), name="logout_success"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
]