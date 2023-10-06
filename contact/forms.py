from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['comment', 'name', 'email']
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Comment'}),
            'name': forms.TextInput(attrs={'placeholder': 'Your Name*'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email*'}),
        }
    comment = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Comment'})
    )

    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Name*'})
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your Email*'})
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
    def save(self, commit=True):
        instance = super().save(commit=True)
        if self.user and self.user.is_authenticated:
            instance.username = self.user
        if commit:
            instance.save()
        return instance