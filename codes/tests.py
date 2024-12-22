from django.test import TestCase

from codes.models import Code
from users.models import User


class CodeModelTest(TestCase):
    """Тесты для модели кода верификации"""

    def setUp(self):
        """Фикстуры меняются при применении методов класса"""
        self.user = User.objects.create(
            phone='+79999999999',
            nickname='admin',
        )
        self.code = Code.objects.create(
            user=self.user,
        )

    def test_labels(self):
        """Проверка атрибутов verbose_name Code"""

        field_label_number = self.code._meta.get_field('number').verbose_name
        field_label_user = self.code._meta.get_field('user').verbose_name

        self.assertEquals(field_label_number, 'Код верификации')
        self.assertEquals(field_label_user, 'user')

    def test_number_field(self):
        """Проверка создания, содержания и изменения кода верификации"""

        length_code = len(self.code.number)
        is_str_code = isinstance(self.code.number, str)
        is_numeric_code = self.code.number.isnumeric()
        # проверка, что код при сохранении перезаписывается
        first_code = self.code.number
        self.code.save()
        second_code = self.code.number

        self.assertEquals(length_code, 5)
        self.assertEquals(is_str_code, True)
        self.assertEquals(is_numeric_code, True)
        self.assertFalse(first_code == second_code)
