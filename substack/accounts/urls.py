from django.urls import include, path, re_path
from . import views

app_name = 'accounts'

urlpatterns = [
    re_path(r'^$', views.send_to_login, name='homepage'),
    re_path(r'^login/$', views.login_screen, name='login'),
    re_path(r'^signup/$', views.create_account, name='create'),
    re_path(r'^create/$', views.create_account, name='signup'),
    re_path(r'^info/$', views.account_management, name='info'),
    re_path(r'^logout/$', views.logout_view, name='logout'),
]