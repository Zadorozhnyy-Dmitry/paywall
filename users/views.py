from django.shortcuts import render, redirect
from django.views.generic import CreateView

from config.settings import SUBSCRIPTION_COST
from users.form import UserRegisterForm, PaidSubscriptionForm
from users.models import User, PaidSubscription
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from django.contrib.auth import authenticate

from users.services import (
    create_stripe_product,
    create_stripe_price,
    create_stripe_sessions,
)


class UserLoginView(LoginView):
    """Расширенный вариант базового контроллера логина"""

    template_name = "users/login.html"
    extra_context = {"title": "Вход"}

    def form_valid(self, form):
        """
        Проверка, что пользователь есть в БД
        Перенаправляет в окно подтверждение логина через смс
        Пользователь не авторизовывавется
        """

        if self.request.method == "POST":
            username = self.request.POST.get("username")
            password = self.request.POST.get("password")
            user = authenticate(self.request, username=username, password=password)
            if user is not None:
                self.request.session["pk"] = user.pk
                return redirect("codes:verify")
        return render(self.request, "users/login.html", {"form": form})


class UserCreateView(CreateView):
    """Контроллер для регистрации пользователя"""

    model = User
    form_class = UserRegisterForm
    extra_context = {"title": "Регистрация"}
    success_url = reverse_lazy("users:login")


class PaidSubscriptionCreateView(CreateView):
    """Контроллер для создания платежа"""

    model = PaidSubscription
    form_class = PaidSubscriptionForm
    extra_context = {"title": "Подписка", "cost": SUBSCRIPTION_COST}

    # success_url = reverse_lazy("publications:publication_list")

    def form_valid(self, form):
        """Создание платежа"""
        user = self.request.user
        subscription = form.save()
        subscription.user = user
        subscription.amount = SUBSCRIPTION_COST
        product = create_stripe_product()
        price = create_stripe_price(product, subscription.amount)
        session_id, payment_link = create_stripe_sessions(price)
        subscription.session_id = session_id
        subscription.link = payment_link
        subscription.save()
        # флаг, что пользователь оплатил подписку
        user.is_sub = True
        user.save()
        return redirect(f"{subscription.link}")
