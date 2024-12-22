from django.test import TestCase
from django.urls import reverse

from config.settings import NUMBER_OF_PUBLICATION_ON_PAGE
from publications.models import Publication
from users.models import User


class PublicationModelTest(TestCase):
    """Тесты для модели публикации"""

    def setUp(self):
        """Фикстуры меняются при применении методов класса"""
        self.user = User.objects.create(
            phone="+79999999999",
            nickname="admin",
        )
        self.publication = Publication.objects.create(
            title="title",
            body="body",
            author=self.user,
        )

    def test_labels(self):
        """Проверка атрибутов verbose_name Publication"""

        field_label_title = self.publication._meta.get_field("title").verbose_name
        field_label_body = self.publication._meta.get_field("body").verbose_name
        field_label_preview = self.publication._meta.get_field("preview").verbose_name
        field_label_slug = self.publication._meta.get_field("slug").verbose_name
        field_label_is_paid = self.publication._meta.get_field("is_paid").verbose_name
        field_label_views_count = self.publication._meta.get_field(
            "views_count"
        ).verbose_name
        field_label_author = self.publication._meta.get_field("author").verbose_name
        field_label_liked_by = self.publication._meta.get_field("liked_by").verbose_name

        self.assertEquals(field_label_title, "Заголовок")
        self.assertEquals(field_label_body, "Содержимое")
        self.assertEquals(field_label_preview, "Изображение")
        self.assertEquals(field_label_slug, "Slug")
        self.assertEquals(field_label_is_paid, "Платная публикация")
        self.assertEquals(field_label_views_count, "Просмотры")
        self.assertEquals(field_label_author, "Автор")
        self.assertEquals(field_label_liked_by, "Пользователи, которые поставили лайк")


class PublicationViewTest(TestCase):
    """Тесты контроллеров публикаций"""

    def setUp(self):
        """Фикстуры"""
        self.user = User.objects.create(
            phone="+79999999999",
            nickname="admin",
        )
        self.client.force_login(user=self.user)
        # создаем необходимое кол-во публикаций для проверки пагинации
        for publication_num in range(NUMBER_OF_PUBLICATION_ON_PAGE + 1):
            Publication.objects.create(
                title="title %s" % publication_num,
                body="body %s" % publication_num,
                author=self.user,
            )

    def test_list_view(self):
        """Проверка отображения списка публикаций"""
        url = reverse("publications:publication_list")
        response = self.client.get(url)
        # проверка правильного url
        self.assertEqual(response.status_code, 200)
        # проверка пути к шаблону
        self.assertTemplateUsed(response, "publications/publication_list.html")
        # проверка пагинации
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] == True)
        self.assertFalse(len(response.context) == NUMBER_OF_PUBLICATION_ON_PAGE)
        self.assertTrue(
            len(response.context["publication_list"]) == NUMBER_OF_PUBLICATION_ON_PAGE
        )

    def test_publication_detail(self):
        """Проверка отображения одной публикации"""
        publication = Publication.objects.get(title="title 1")
        url = reverse("publications:publication_view", args=(publication.pk,))
        response = self.client.get(url)
        # проверка правильного url
        self.assertEqual(response.status_code, 200)

    def test_publication_create(self):
        """Проверка создания публикации"""
        url = reverse("publications:publication_create")
        Publication.objects.create(
            title="title 5",
            body="body 5",
            author=self.user,
        )
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Publication.objects.all().count(), 5)
