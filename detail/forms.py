from django import forms
from .models import Detail,Comment, Hashtag

class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ['title', 'content','hashtags','image'] 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']

class MediaForm(forms.ModelForm):
    model = Detail
    fields = ['medias']