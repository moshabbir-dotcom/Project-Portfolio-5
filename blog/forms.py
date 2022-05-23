from django import forms
from .models import Comment, Post, Newsletter


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
