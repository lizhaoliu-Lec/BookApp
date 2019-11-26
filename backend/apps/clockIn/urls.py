from django.urls import path
from ..clockIn.views import ClockView

urlpatterns = [
    path('api/v1/clockIn/', ClockView.as_view({'post': 'create', "delete": "destroy"}))
]