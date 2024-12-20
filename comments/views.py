from django.views.generic import CreateView, UpdateView, DeleteView

from comments.forms import CommentForm
from comments.models import Comment
from publications.models import Publication
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class BaseCommentView:
    """Базовый класс для всех контроллеров"""
    model = Comment

    def get_success_url(self):
        """Метод определяет ссылку на публикацию, к которой привязан комментарий"""
        publication = Publication.objects.get(pk=self.object.publication.pk)
        return reverse(
            'publications:publication_view', args=[str(self.object.publication.pk)]
        )


class CommentCreateView(BaseCommentView, CreateView, LoginRequiredMixin):
    """Контроллер для создания комментария"""
    form_class = CommentForm

    def form_valid(self, form):
        """Автоматическая привязка к комментарию автора и публикации"""
        form.instance.author = self.request.user
        form.instance.publication = Publication.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)


class CommentUpdateView(BaseCommentView, UpdateView, LoginRequiredMixin):
    """Контроллер для редактирования комментария"""
    form_class = CommentForm
    template_name = 'comments/comment_form.html'
    extra_context = {"title": "Редактировать комментарий"}


class CommentDeleteView(BaseCommentView, DeleteView, LoginRequiredMixin):
    """Контроллер для удаления комментария"""
    template_name = 'comments/comment_confirm_delete.html'
    extra_context = {"title": "Удалить комментарий"}
