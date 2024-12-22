from django import forms

from publications.models import Publication


class StyleFormMixin:
    """Миксин для стилизации формы"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != "is_paid":
                field.widget.attrs["class"] = "form-control"


class PublicationForm(StyleFormMixin, forms.ModelForm):
    """Класс для описания формы публикации"""

    class Meta:
        model = Publication
        fields = (
            "title",
            "body",
            "preview",
            "is_paid",
        )
