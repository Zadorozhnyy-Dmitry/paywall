from django.test import TestCase
from django.urls import reverse

from comments.models import Comment
from publications.models import Publication
from users.models import User


class CommentModelTest(TestCase):
    """Тесты для модели комментариев"""

    def setUp(self):
        """Фикстуры"""
        self.user = User.objects.create(
            phone="+79999999999",
            nickname="admin",
        )
        self.publication = Publication.objects.create(
            title="title",
            body="body",
            author=self.user,
        )
        self.comment = Comment.objects.create(
            publication=self.publication,
            author=self.user,
            text="комментарий",
        )

    def test_labels(self):
        """Проверка атрибутов verbose_name Comment"""

        field_label_publication = self.comment._meta.get_field(
            "publication"
        ).verbose_name
        field_label_author = self.comment._meta.get_field("author").verbose_name
        field_label_created_at = self.comment._meta.get_field("created_at").verbose_name
        field_label_text = self.comment._meta.get_field("text").verbose_name

        self.assertEquals(field_label_publication, "Публикация")
        self.assertEquals(field_label_author, "Автор")
        self.assertEquals(field_label_created_at, "Дата и время создания")
        self.assertEquals(field_label_text, "Текст")


class CommentViewTest(TestCase):
    """Тесты для контроллеров комментариев"""

    def setUp(self):
        """Фикстуры"""
        self.user = User.objects.create(
            phone="+79999999999",
            nickname="admin",
        )
        self.client.force_login(user=self.user)
        self.publication = Publication.objects.create(
            title="title",
            body="body",
            author=self.user,
        )

    def test_comment_create(self):
        """Проверка создания комментария"""
        url = reverse("comments:comment_create", args=(self.publication.pk,))
        data = {
            "publication": self.publication,
            "text": "комментарий",
            "author": self.user,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.all().count(), 1)
