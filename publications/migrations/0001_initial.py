# Generated by Django 4.2.2 on 2024-12-16 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Publication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Введите заголовок публикации",
                        max_length=150,
                        verbose_name="Заголовок",
                    ),
                ),
                (
                    "body",
                    models.TextField(
                        help_text="Введите содержимое статьи", verbose_name="Содержимое"
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Добавьте изображение",
                        null=True,
                        upload_to="publications/photo",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "slug",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="Slug"
                    ),
                ),
                (
                    "created_at",
                    models.DateField(auto_now_add=True, verbose_name="Дата создания"),
                ),
                (
                    "is_paid",
                    models.BooleanField(
                        default=True, verbose_name="Платная публикация"
                    ),
                ),
                (
                    "views_count",
                    models.PositiveIntegerField(
                        default=0, editable=False, verbose_name="Просмотры"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
                (
                    "liked_by",
                    models.ManyToManyField(
                        related_name="liked_posts",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователи, которые поставили лайк",
                    ),
                ),
            ],
            options={
                "verbose_name": "Публикация",
                "verbose_name_plural": "Публикации",
                "ordering": ["-id"],
            },
        ),
    ]
