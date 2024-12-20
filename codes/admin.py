from django.contrib import admin

from codes.models import Code


@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "number",
    )
