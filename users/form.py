from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.forms import (
    UserCreationForm,
)
from django import forms
from publications.forms import StyleFormMixin
from users.models import User, PaidSubscription


class PhoneForm(forms.Form):
    phone = PhoneNumberField(region="RU")


class UserRegisterForm(StyleFormMixin, PhoneForm, UserCreationForm):
    """Форма для регистрации пользователя"""

    class Meta:
        model = User
        fields = (
            "phone",
            "password1",
            "password2",
            'avatar',
            'nickname',
        )


class PaidSubscriptionForm(StyleFormMixin, forms.ModelForm):
    """Форма для платной подписки"""

    class Meta:
        model = PaidSubscription
        fields = (
            'user',
            'paid_date',
            'amount',
            'session_id',
            'link',
        )
