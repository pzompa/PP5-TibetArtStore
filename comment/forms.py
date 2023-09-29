from django import forms
from .models import ProductComment

class ProductCommentForm(forms.ModelForm):
    comment_text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Share your thoughts about this product'}),
        required=True,
    )

    class Meta:
        model = ProductComment
        fields = ['comment_text']

