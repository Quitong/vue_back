from django import forms

from blog.models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)


class LoginForm(forms.Form):
    login = forms.CharField(label="Your name",max_length=100)
    password = forms.CharField(label="Your pass", max_length=100)
