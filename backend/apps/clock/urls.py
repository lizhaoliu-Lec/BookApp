from django.urls import path
from ..clock.views import ClockView

urlpatterns = [
    path('api/v1/clock/', ClockView.as_view({'get': 'list', 'post': 'create',
                                             'put': "partial_update", "delete": "destroy"}))
]