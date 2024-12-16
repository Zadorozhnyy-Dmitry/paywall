from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from config.settings import NULLABLE


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
