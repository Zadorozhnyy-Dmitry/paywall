from django.urls import path

from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView

from users.views import UserCreateView

app_name = UsersConfig.name

urlpatterns = [
    # вход
    path("login/", LoginView.as_view(template_name="users/login.html", extra_context={"title": "Вход"}), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),  # выход
    path('register/', UserCreateView.as_view(), name='register'),  # регистрация

]
