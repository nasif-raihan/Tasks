from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("name", "email", "phone", "home_city")
        labels = {
            "name": "Name",
            "email": "Email",
            "phone": "Phone",
            "home_city": "Home City",
        }
