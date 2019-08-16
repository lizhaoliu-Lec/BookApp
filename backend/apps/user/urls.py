from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^api/v1/auth/$', views.AuthView.as_view(), name='auth'),
    re_path(r'^api/v1/register/$', views.RegisterView.as_view(), name='register'),
]
