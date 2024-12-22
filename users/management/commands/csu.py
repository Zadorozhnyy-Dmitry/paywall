from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Кастомная команда для создания суперпользователя"""

    def handle(self, *args, **options):
        user = User.objects.create(phone="+79999999999")
        user.set_password("admin")
        user.nickname = "admin"
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.is_sub = True
        user.save()
