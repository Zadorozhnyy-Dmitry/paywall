from django.views.generic import CreateView

from users.form import UserRegisterForm
from users.models import User
from django.urls import reverse_lazy


class UserCreateView(CreateView):
    """Контроллер для регистрации пользователя"""

    model = User
    form_class = UserRegisterForm
    extra_context = {"title": "Регистрация"}
    success_url = reverse_lazy("users:login")

    # def form_valid(self, form):
    #     """Верификация почты пользователя через отправленное письмо"""
    #
    #     user = form.save()
    #     user.is_active = False
    #     token = secrets.token_hex(16)
    #     user.token = token
    #     user.save()
    #     host = self.request.get_host()
    #     url = f"http://{host}/users/email-confirm/{token}/"
    #     send_mail(
    #         subject="Подтверждение почты",
    #         message=f"Перейдите по ссылке для подтверждения почты {url}",
    #         from_email=EMAIL_HOST_USER,
    #         recipient_list=[user.email],
    #     )
    #     return super().form_valid(form)
