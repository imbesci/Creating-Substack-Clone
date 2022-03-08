from django.urls import include, path, re_path
from . import views

app_name = 'articles'

urlpatterns = [
    re_path(r'^$', views.articles_list, name="list"),
    re_path(r'^create/$', views.create_article, name="create"),
    re_path(r'^(?P<slug>[\w-]+)/$', views.full_article, name='full'),
]