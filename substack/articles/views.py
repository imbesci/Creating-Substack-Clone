from django.shortcuts import render
from .models import Article
from . import forms

# Create your views here.
def articles_list(request):
    articles = Article.objects.all().order_by("-date")
    return render(request, 'articles/articles_list.html', context = { 'articles' : articles } )


def full_article(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, "articles/full_article.html" , context = { 'article' : article } )

def create_article(request):
    articleForm = forms.CreateArticle()
    return render(request, 'articles/article_creation.html', context = { 'articleForm' : articleForm } )