from django import forms
from .models import Posts, Comment


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ("title", "link")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
