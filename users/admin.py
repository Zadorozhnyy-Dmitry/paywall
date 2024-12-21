from django.contrib import admin

from users.models import User, PaidSubscription


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


@admin.register(PaidSubscription)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "paid_date",
        "amount",
    )
