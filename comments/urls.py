from django.urls import path

from comments.apps import CommentsConfig
from comments.views import CommentUpdateView, CommentCreateView, CommentDeleteView

app_name = CommentsConfig.name

urlpatterns = [
    path(
        "create/<int:pk>/", CommentCreateView.as_view(), name="comment_create"
    ),  # создание комментария
    path(
        "update/<int:pk>/",
        CommentUpdateView.as_view(),
        name="comment_update",
    ),  # редактирование комментария
    path(
        "delete/<int:pk>/",
        CommentDeleteView.as_view(),
        name="comment_delete",
    ),  # удаление комментария
]
