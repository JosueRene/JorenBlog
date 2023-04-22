from django import forms

from .models import Post

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('type', 'title', 'description',)
        widgets = {
            'type': forms.Select(attrs={
            'class': 'form-control mt-5 mb-5'
            }),
            'title': forms.TextInput(attrs={
            'class': 'form-control mb-5',
            'placeholder': 'Post Title'
            }),
            'description': forms.Textarea(attrs={
            'class': 'form-control mb-5',
            'placeholder': 'Post Description'
            })
        }