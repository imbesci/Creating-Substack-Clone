from django import forms
from . import models


#add form for making new articles
class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'description', 'body', 'slug', 'thumbnail' ]
