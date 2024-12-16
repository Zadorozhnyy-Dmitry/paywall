from django import forms
from phonenumber_field.formfields import PhoneNumberField


class PhoneForm(forms.Form):
    number = PhoneNumberField(region="RU")
