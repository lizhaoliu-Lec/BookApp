from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^api/v1/timing_record/$', views.TimingRecordView.as_view(), name='timing_record'),
]
