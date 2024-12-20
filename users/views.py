from django.shortcuts import render, redirect
from django.views.generic import CreateView

from users.form import UserRegisterForm
from users.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from django.contrib.auth import authenticate


class UserLoginView(LoginView):
    """Расширенный вариант базового контроллера логина"""
    template_name = "users/login.html"
    extra_context = {"title": "Вход"}

    def form_valid(self, form):
        """
        Проверка, что пользователь есть в БД
        Перенаправляет в окно подтверждение логина через смс
        """

        if self.request.method == 'POST':
            username = self.request.POST.get('username')
            password = self.request.POST.get('password')
            user = authenticate(self.request, username=username, password=password)
            if user is not None:
                self.request.session['pk'] = user.pk
                return redirect('codes:verify')
        return render(self.request, 'users/login.html', {'form': form})


class UserCreateView(CreateView):
    """Контроллер для регистрации пользователя"""

    model = User
    form_class = UserRegisterForm
    extra_context = {"title": "Регистрация"}
    success_url = reverse_lazy("users:login")
