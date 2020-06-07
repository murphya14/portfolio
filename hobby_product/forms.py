from .models import Review
from django import forms


class PostForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('content', 'image', 'published_date')