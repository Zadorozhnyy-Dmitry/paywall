from django.urls import path

from users.apps import UsersConfig
from django.contrib.auth.views import LogoutView

from users.views import UserCreateView, UserLoginView

app_name = UsersConfig.name

urlpatterns = [
    # вход
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),  # выход
    path('register/', UserCreateView.as_view(), name='register'),  # регистрация

]
