from django.db import models

from config.settings import AUTH_USER_MODEL, NULLABLE


class Publication(models.Model):
    """Модель для публикации"""

    title = models.CharField(max_length=150, verbose_name='Заголовок', help_text='Введите заголовок публикации')
    body = models.TextField(verbose_name='Содержимое', help_text='Введите содержимое статьи')
    preview = models.ImageField(
        upload_to='publications/photo',
        verbose_name='Изображение',
        help_text='Добавьте изображение',
        **NULLABLE
    )
    slug = models.CharField(max_length=150, verbose_name='Slug', **NULLABLE)
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    is_paid = models.BooleanField(
        default=False,
        verbose_name="Платная публикация",
    )
    views_count = models.PositiveIntegerField(
        default=0, editable=False, verbose_name="Просмотры"
    )
    author = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор", **NULLABLE
    )
    liked_by = models.ManyToManyField(
        AUTH_USER_MODEL,
        verbose_name='Пользователи, которые поставили лайк',
        related_name="liked_posts"
    )

    def __str__(self):
        return f'{self.title} {self.created_at}'

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-id']
