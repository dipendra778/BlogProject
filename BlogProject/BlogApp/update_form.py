from django import forms
from .models import PostArticles

class UpdateForm(forms.ModelForm):
    class Meta:
        model=PostArticles
        fields='__all__'