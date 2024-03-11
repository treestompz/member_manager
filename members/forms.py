from django import forms
from django.core.exceptions import ValidationError

from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["first_name", "last_name", "email", "phone_number", "role"]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "phone_number": "Phone Number",
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if not phone_number.isdigit():
            raise ValidationError("Phone Number must contain only digits.")
        if len(phone_number) != 10:
            raise ValidationError("Phone Number must be exactly 10 digits long.")

        return phone_number
