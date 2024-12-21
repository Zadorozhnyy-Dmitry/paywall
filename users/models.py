from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from config.settings import NULLABLE
from datetime import datetime


class User(AbstractUser):
    """Модель юзера"""
    username = None
    phone = PhoneNumberField(
        unique=True,
        verbose_name='Телефон',
        help_text='Укажите телефон',
    )
    avatar = models.ImageField(
        upload_to='users/avatars',
        verbose_name='Аватар',
        help_text='Загрузите фото',
        **NULLABLE,
    )
    nickname = models.CharField(
        max_length=15,
        unique=True,
        verbose_name='Ник',
        help_text='Введите свой nick_name',
    )
    is_sub = models.BooleanField(
        default=False,
        verbose_name='Есть платная подписка'
    )

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.nickname} - {self.phone}'


class PaidSubscription(models.Model):
    """Класс для платной подписки"""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь", **NULLABLE
    )
    paid_date = models.DateTimeField(
        default=datetime.now, verbose_name="Дата оплаты", **NULLABLE
    )
    amount = models.PositiveSmallIntegerField(verbose_name="Сумма оплаты", **NULLABLE)
    session_id = models.CharField(max_length=255, verbose_name='Id сессии', **NULLABLE)
    link = models.URLField(max_length=400, verbose_name='Ссылка на оплату', **NULLABLE)

    def __str__(self):
        return f"{self.user} - оплатил за подписку {self.paid_date}"

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
