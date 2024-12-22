from django.db import models

from users.models import User
import random


class Code(models.Model):
    """Класс для смс-кода верификации юзера"""

    number = models.CharField(max_length=5, blank=True, verbose_name="Код верификации")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.number} - {self.user.phone}"

    def save(self, *args, **kwargs):
        """Генерация случайного кода для верификации"""
        number_list = [x for x in range(10)]
        code_items = []

        for i in range(5):
            num = random.choice(number_list)
            code_items.append(num)

        code_string = "".join(str(item) for item in code_items)
        self.number = code_string
        super().save(*args, **kwargs)
