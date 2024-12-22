from django.test import TestCase

from users.models import User, PaidSubscription


class UserModelTest(TestCase):
    """Тесты для модели пользователя"""

    def setUp(self):
        """Фикстуры меняются при применении методов класса"""
        self.user = User.objects.create(
            phone='+79999999999',
            nickname='admin',
        )

    def test_labels(self):
        """Проверка атрибутов verbose_name User"""

        field_label_phone = self.user._meta.get_field('phone').verbose_name
        field_label_avatar = self.user._meta.get_field('avatar').verbose_name
        field_label_nickname = self.user._meta.get_field('nickname').verbose_name
        field_label_is_sub = self.user._meta.get_field('is_sub').verbose_name

        self.assertEquals(field_label_phone, 'Телефон')
        self.assertEquals(field_label_avatar, 'Аватар')
        self.assertEquals(field_label_nickname, 'Ник')
        self.assertEquals(field_label_is_sub, 'Есть платная подписка')


class PaidSubscriptionModelTest(TestCase):
    """Тесты для модели платной подписки"""

    def setUp(self):
        """Фикстуры меняются при применении методов класса"""
        self.user = User.objects.create(
            phone='+79999999999',
            nickname='admin',
        )
        self.paid_sub = PaidSubscription.objects.create(
            user=self.user,
            amount=1000,
        )

    def test_labels(self):
        """Проверка атрибутов verbose_name PaidSubscription"""

        field_label_user = self.paid_sub._meta.get_field('user').verbose_name
        field_label_paid_date = self.paid_sub._meta.get_field('paid_date').verbose_name
        field_label_amount = self.paid_sub._meta.get_field('amount').verbose_name
        field_label_session_id = self.paid_sub._meta.get_field('session_id').verbose_name
        field_label_link = self.paid_sub._meta.get_field('link').verbose_name

        self.assertEquals(field_label_user, 'Пользователь')
        self.assertEquals(field_label_paid_date, 'Дата оплаты')
        self.assertEquals(field_label_amount, 'Сумма оплаты')
        self.assertEquals(field_label_session_id, 'Id сессии')
        self.assertEquals(field_label_link, 'Ссылка на оплату')
