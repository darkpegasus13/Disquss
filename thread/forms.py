from django import forms
from thread.models import Post, Post_reply


class Post_Thread(forms.ModelForm):
    category = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Category'
        }
    ))
    post = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Description'
        }
    ))
    post_title =  forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Title'
        }
    ))

    class Meta:
        model = Post
        fields = ('post', 'category', 'post_title')


class Post_answer(forms.ModelForm):
    post = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a reply.....'
        }
    ))
    comment =forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Leave A Comment .....'
        }
    ),required=False)

    class Meta:
        model = Post_reply
        fields = ('post','Post_reply_reply')
