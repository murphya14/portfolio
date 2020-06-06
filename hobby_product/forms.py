from .models import Review


class PostForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('content', 'image', 'published_date')