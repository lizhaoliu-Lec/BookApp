from django.urls import re_path
from ..todo.views import TodoView

urlpatterns = [
    re_path(r'^api/v1/todo/$', TodoView.as_view({'get': 'list', 'post': 'create'}))
]