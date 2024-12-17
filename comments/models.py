from django.db import models

from config.settings import AUTH_USER_MODEL, NULLABLE
from publications.models import Publication


class Comment(models.Model):
    """Модель для комментария к публикации"""

    publication = models.ForeignKey(
        Publication,
        on_delete=models.CASCADE,
        verbose_name='Публикация',
        related_name='comments',
        **NULLABLE
    )
    author = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор", **NULLABLE
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания",
    )
    text = models.TextField(verbose_name='Текст', **NULLABLE)

    def __str__(self):
        return f'Комментарий от {self.author} к публикации {self.publication}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['id']
