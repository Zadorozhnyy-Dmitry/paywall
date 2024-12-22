from django import forms

from comments.models import Comment


class CommentForm(forms.ModelForm):
    """Класс для описания формы комментария"""

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Введите текст комментария",
                "rows": 5,
            }
        )
    )

    class Meta:
        model = Comment
        fields = ("text",)
