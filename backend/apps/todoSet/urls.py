from django.urls import path
from ..todoSet.views import TodoSetView

urlpatterns = [
    path('api/v1/todoSet/', TodoSetView.as_view({'get': 'list', 'post': 'create',
                                                 'put': "partial_update", "delete": "destroy"}))
]