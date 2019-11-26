from django.urls import path
from .views import RemainView

urlpatterns = [
    path('api/v1/remain/', RemainView.as_view({'get': 'list', 'post': 'create',
                                           'put': "partial_update", "delete": "destroy"}))
]