from django import forms
from .models import User
from groups.models import Group


class UserCreateForm(forms.ModelForm):
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(), required=False, label="Группа"
    )

    class Meta:
        model = User
        fields = ["name", "role"]
