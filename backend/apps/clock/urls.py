from django.urls import path
from ..todo.views import TodoView

urlpatterns = [
    path('api/v1/clock/', TodoView.as_view({'get': 'list', 'post': 'create',
                                           'put': "partial_update", "delete": "destroy"}))
]