from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^api/v1/timing_record/$', views.TimingRecordView.as_view(), name='timing_record'),
    re_path(r'^api/v1/timing_plan/$', views.TimingPlanView.as_view(), name='timing_plan'),
    re_path(r'^api/v1/timing_group/$', views.TimingGroupView.as_view(), name='timing_group'),
]
