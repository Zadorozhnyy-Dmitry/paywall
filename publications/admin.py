from django.contrib import admin

from publications.models import Publication


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    """Админка для публикации"""

    list_display = (
        "id",
        "author",
        "title",
        "slug",
        "created_at",
        "is_paid",
        "views_count",
    )
    list_filter = ("author", "is_paid")
    ordering = ("created_at",)
