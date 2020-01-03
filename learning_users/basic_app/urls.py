from django.conf.urls import re_path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    re_path('^register/$', views.register, name='register'),
    re_path(r'^user_login/$', views.user_login, name='user_login'),
]
