from django import forms
from codes.models import Code


class CodeForm(forms.ModelForm):
    """Форма для кода верификации"""

    number = forms.CharField(label="Code", help_text="Введите код подтверждения из смс")

    class Meta:
        model = Code
        fields = ("number",)
