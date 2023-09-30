from django import forms
from .models import BlogPost

# Create new BlogPost form
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'writer_name',
            'article_text',
            'article_text_short',
            'active',
            'article_image_name'
        ]

        # Optionally, you can add widgets for specific fields if you want custom styling or attributes:
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'writer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'article_text': forms.Textarea(attrs={'class': 'form-control'}),
            'article_text_short': forms.Textarea(attrs={'class': 'form-control'}),
            'article_image_name': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

