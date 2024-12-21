from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from comments.forms import CommentForm
from config.settings import NUMBER_OF_PUBLICATION_ON_PAGE
from publications.forms import PublicationForm
from publications.models import Publication
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


class PublicationListView(ListView):
    """Контроллер для списка публикаций"""

    paginate_by = NUMBER_OF_PUBLICATION_ON_PAGE
    model = Publication
    extra_context = {"title": "Публикации", 'back_to_top': True}

    def get_queryset(self, *args, **kwargs):
        """ Запрет просмотр платного контента без подписки"""

        queryset = super().get_queryset(*args, **kwargs)
        # Условие: пользователя нет в БД или не имеет подписку
        if not self.request.user.pk or not self.request.user.is_sub:
            queryset = queryset.exclude(is_paid=True)
        return queryset


class PublicationOwnerListView(ListView):
    """Контроллер для списка своих публикаций"""

    paginate_by = NUMBER_OF_PUBLICATION_ON_PAGE
    model = Publication
    extra_context = {"title": "Мои публикации", 'back_to_top': True}

    def get_queryset(self, *args, **kwargs):
        """ Возвращает список публикаций, для которых пользователь является автором"""

        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user
        queryset = queryset.filter(author=user)
        return queryset


class PublicationDetailView(DetailView):
    """Контроллер для детального просмотра публикаций"""

    model = Publication
    extra_context = {"title": "Публикации"}

    def get_object(self, queryset=None):
        """Счетчик просмотров"""
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save(update_fields=['views_count'])
        return self.object

    def get_context_data(self, **kwargs):
        """Добавляем форму комментария"""
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class PublicationCreateView(CreateView, LoginRequiredMixin):
    """Контроллер создания публикации"""

    model = Publication
    form_class = PublicationForm
    extra_context = {"title": "Создать публикацию"}
    success_url = reverse_lazy("publications:publication_list")

    def form_valid(self, form):
        """Автоматическая привязка автора к публикации и формирование slug"""
        publication = form.save()
        user = self.request.user
        publication.author = user
        publication.slug = slugify(publication.title)
        publication.save()
        return super().form_valid(form)


class PublicationUpdateView(UpdateView, LoginRequiredMixin):
    """Контроллер изменения публикации"""

    model = Publication
    form_class = PublicationForm
    extra_context = {"title": "Изменить публикацию"}
    success_url = reverse_lazy("publications:publication_list")

    def form_valid(self, form):
        """формирование slug"""
        publication = form.save()
        publication.slug = slugify(publication.title)
        publication.save()
        return super().form_valid(form)

    def get_success_url(self):
        """Перенаправление на нужное сообщение после редактирования"""

        return reverse("publications:publication_view", args=[self.kwargs.get("pk")])


class PublicationDeleteView(DeleteView, LoginRequiredMixin):
    """Контроллер удаления публикации"""

    model = Publication
    extra_context = {"title": "Удалить публикацию"}
    permission_required = 'publications.publication_delete'
    success_url = reverse_lazy("publications:publication_list")


class AddRemoveLike(View, LoginRequiredMixin):
    """Контроллер для лайка"""

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Publication, pk=pk)
        # автор публикации не может поставить себе лайк
        if post.author.id != request.user.id:
            if not post.liked_by.filter(id=request.user.id).exists():
                """если пользователь еще не ставил лайк"""
                post.liked_by.add(request.user)
                post.save()
                return HttpResponseRedirect(reverse("publications:publication_view", args=[str(pk)]))
            else:
                """если пользователь уже ставил лайк"""
                post.liked_by.remove(request.user)
                post.save()
                return HttpResponseRedirect(reverse("publications:publication_view", args=[str(pk)]))

        return HttpResponseRedirect(reverse("publications:publication_view", args=[str(pk)]))
