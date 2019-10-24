from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^api/v1/todo/$', views.TodoView.as_view({'get': 'list', 'post': 'create'})),
]