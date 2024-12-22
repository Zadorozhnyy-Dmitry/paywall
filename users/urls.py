from django.urls import path

from users.apps import UsersConfig
from django.contrib.auth.views import LogoutView

from users.views import UserCreateView, UserLoginView, PaidSubscriptionCreateView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),  # вход
    path("logout/", LogoutView.as_view(), name="logout"),  # выход
    path("register/", UserCreateView.as_view(), name="register"),  # регистрация
    # оплата подписки
    path(
        "paid_subscription/",
        PaidSubscriptionCreateView.as_view(),
        name="paid_subscription",
    ),
]
