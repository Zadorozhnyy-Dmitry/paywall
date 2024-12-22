from django.contrib import admin

from comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Админка для комментариев"""

    list_display = (
        "id",
        "author",
        "publication",
        "created_at",
        "text",
    )
    list_filter = ("author", "publication")
    ordering = ("-id",)
