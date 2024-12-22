from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "", include("publications.urls", namespace="publications")
    ),  # маршрутизация к публикациям
    path(
        "users/", include("users.urls", namespace="users")
    ),  # маршрутизация к пользователям
    path(
        "comments/", include("comments.urls", namespace="comments")
    ),  # маршрутизация к комментариям
    path(
        "codes/", include("codes.urls", namespace="codes")
    ),  # маршрутизация к кодам верификации
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
