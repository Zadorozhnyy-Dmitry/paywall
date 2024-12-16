from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "phone",
        "nickname",
        "is_sub",
        "is_active",
        "last_login",
    )
