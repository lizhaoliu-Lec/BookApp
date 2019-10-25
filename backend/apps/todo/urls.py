from django.urls import path
from ..todo.views import TodoView

urlpatterns = [
    path('api/v1/todo', TodoView.as_view({'get': 'list', 'post': 'create'}))
]

