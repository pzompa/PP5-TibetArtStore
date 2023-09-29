from django import forms
from .models import ProductComment, BlogPostComment

class ProductCommentForm(forms.ModelForm):
    comment_text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Share your thoughts about this product'}),
        required=True,
    )

    class Meta:
        model = ProductComment
        fields = ['comment_text']

class BlogPostCommentForm(forms.ModelForm):
    comment_text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Share your thoughts about this Blog'}),
        required=True,
    )

    class Meta:
        model = BlogPostComment
        fields = ['comment_text']