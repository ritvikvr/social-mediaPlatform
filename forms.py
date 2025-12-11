from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        widgets = {'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'What\'s on your mind?'})}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {'content': forms.TextInput(attrs={'placeholder': 'Add a comment...'})}  # Inline style