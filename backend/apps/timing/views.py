import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..user.utils.auth import Authentication
from .models import TimingRecord
from .models import TimingPlan
from .models import TimingGroup
from .serializers import TimingRecordSerializer
from .serializers import TimingPlanSerializer
from .serializers import TimingGroupSerializer
from .utils.data import TIMING_TYPE_2_INT
from .utils import code, msg


class TimingRecordView(APIView):
    authentication_classes = [Authentication, ]

    def get(self, *args, **kwargs):
        ret = dict(code=code.TIMING_RECORD_GET_FAIL,
                   msg=msg.TIMING_RECORD_GET_FAIL)
        try:
            user = self.request.user
            timing_records = TimingRecord.objects.filter(user=user)
            timing_records = TimingRecordSerializer(instance=timing_records, many=True)
            for d in timing_records.data:
                int_type = TIMING_TYPE_2_INT[d['type']]
                if int_type == 1 or int_type == 2:
                    del d['time']
                    del d['end_time']

            ret.update({
                'code': code.TIMING_RECORD_GET_SUCCESS,
                'msg': msg.TIMING_RECORD_GET_SUCCESS,
                'data': timing_records.data
            })
            return Response(data=ret,
                            status=status.HTTP_200_OK)
        except Exception as e:
            print('exception occurs at getting TimingRecordView' + '*** %s ***' % str(type(e)))
            ret.update({
                'code': code.TIMING_RECORD_GET_FAIL,
                'msg': msg.TIMING_RECORD_GET_FAIL,
            })
            return Response(data=ret,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, *args, **kwargs):
        ret = dict(code=code.TIMING_RECORD_POST_FAIL,
                   msg=msg.TIMING_RECORD_POST_FAIL)
        try:
            user = self.request.user
            str_type = self.request.POST.get('type', None)
            str_start_time = self.request.POST.get('start_time', None)
            start_time = datetime.datetime.strptime(str_start_time, '%Y-%m-%d %H:%M:%S')
            remark = self.request.POST.get('remark', None)

            if not (str_type and start_time and remark):
                print('type, start_time and remark must provided.')
                ret.update({
                    'code': code.TIMING_RECORD_POST_FAIL,
                    'msg': msg.TIMING_RECORD_POST_FAIL
                })
                return Response(data=ret,
                                status=status.HTTP_200_OK)

            int_type = TIMING_TYPE_2_INT.get(str_type, None)

            if int_type is None:
                print('type must be one of `%s`' % ', '.join(TIMING_TYPE_2_INT.keys()))
                ret.update({
                    'code': code.TIMING_RECORD_POST_FAIL,
                    'msg': msg.TIMING_RECORD_POST_FAIL
                })
                return Response(data=ret,
                                status=status.HTTP_200_OK)

            if int_type == 0:
                time = self.request.POST.get('time', None)
                str_end_time = self.request.POST.get('end_time', None)
                if not (time and str_end_time):
                    print('Time and end_time must provided.')
                    ret.update({
                        'code': code.TIMING_RECORD_POST_FAIL,
                        'msg': msg.TIMING_RECORD_POST_FAIL
                    })
                    return Response(data=ret,
                                    status=status.HTTP_200_OK)
                time = int(time)
                end_time = datetime.datetime.strptime(str_end_time, '%Y-%m-%d %H:%M:%S')

            else:
                time = None
                end_time = None

            timing_record = TimingRecord(type=int_type,
                                         user=user,
                                         time=time,
                                         remark=remark,
                                         start_time=start_time,
                                         end_time=end_time)
            timing_record.save()

            ret.update({
                'code': code.TIMING_RECORD_POST_SUCCESS,
                'msg': msg.TIMING_RECORD_POST_SUCCESS,
                'type': str_type,
                'user': user.name,
                'time': time,
                'remark': remark,
                'start_time': start_time,
                'end_time': end_time,
            })

            return Response(data=ret,
                            status=status.HTTP_200_OK)
        except Exception as e:
            print('exception occurs at posting TimingRecordView' + '*** %s ***' % str(type(e)))
            ret.update({
                'code': code.TIMING_RECORD_POST_FAIL,
                'msg': msg.TIMING_RECORD_POST_FAIL,
            })
            return Response(data=ret,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TimingPlanView(APIView):
    authentication_classes = [Authentication, ]

    def get(self, *args, **kwargs):
        ret = dict(code=code.TIMING_PLAN_GET_FAIL,
                   msg=msg.TIMING_PLAN_GET_FAIL)

        try:
            user = self.request.user
            timing_plans = TimingPlan.objects.filter(user=user)
            timing_plans = TimingPlanSerializer(instance=timing_plans, many=True)
            ret.update({
                'code': code.TIMING_PLAN_GET_SUCCESS,
                'msg': msg.TIMING_PLAN_GET_SUCCESS,
                'data': timing_plans.data,
            })

            return Response(data=ret,
                            status=status.HTTP_200_OK)
        except Exception as e:
            print('exception occurs at getting TimingPlanView' + '*** %s ***' % str(type(e)))
            ret.update({
                'code': code.TIMING_PLAN_GET_FAIL,
                'msg': msg.TIMING_PLAN_GET_FAIL,
            })
            return Response(data=ret,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, *args, **kwargs):
        ret = dict(code=code.TIMING_RECORD_POST_FAIL,
                   msg=msg.TIMING_RECORD_POST_FAIL)
        try:
            user = self.request.user

            description = self.request.POST.get('description', None)

            if not user and description:
                print('user and description must provided.')
                ret.update({
                    'code': code.TIMING_RECORD_POST_FAIL,
                    'msg': msg.TIMING_RECORD_POST_FAIL,
                })
                return Response(data=ret,
                                status=status.HTTP_200_OK)

            timing_plan = TimingPlan(user=user,
                                     description=description)
            timing_plan.save()

            ret.update({
                'code': code.TIMING_PLAN_POST_SUCCESS,
                'msg': msg.TIMING_PLAN_POST_SUCCESS,
                'user': user.name,
                'description': description
            })

            return Response(data=ret,
                            status=status.HTTP_200_OK)

        except Exception as e:
            ret.update({
                'code': code.TIMING_RECORD_POST_FAIL,
                'msg': msg.TIMING_RECORD_POST_FAIL,
            })
            print('exception occurs at posting TimingRecordView' + '*** %s ***' % str(type(e)))
            return Response(data=ret,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TimingGroupView(APIView):
    authentication_classes = [Authentication, ]

    def get(self, *args, **kwargs):
        ret = dict(code=code.TIMING_GROUP_GET_FAIL,
                   msg=msg.TIMING_GROUP_GET_FAIL)
        try:
            user = self.request.user
            timing_groups = TimingGroup.objects.filter(user=user)
            timing_groups = TimingGroupSerializer(instance=timing_groups, many=True)
            ret.update({
                'code': code.TIMING_PLAN_GET_SUCCESS,
                'msg': msg.TIMING_PLAN_GET_SUCCESS,
                'data': timing_groups.data,
            })

            return Response(data=ret,
                            status=status.HTTP_200_OK)
        except Exception as e:
            print('exception occurs at getting TimingPlanView' + '*** %s ***' % str(type(e)))
            ret.update({
                'code': code.TIMING_PLAN_GET_FAIL,
                'msg': msg.TIMING_PLAN_GET_FAIL,
            })
            return Response(data=ret,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, *args, **kwargs):
        ret = dict(code=code.TIMING_RECORD_POST_FAIL,
                   msg=msg.TIMING_RECORD_POST_FAIL)
        try:
            user = self.request.user

            description = self.request.POST.get('description', None)

            if not user and description:
                print('user and description must provided.')
                ret.update({
                    'code': code.TIMING_RECORD_POST_FAIL,
                    'msg': msg.TIMING_RECORD_POST_FAIL,
                })
                return Response(data=ret,
                                status=status.HTTP_200_OK)

            timing_plan = TimingPlan(user=user,
                                     description=description)
            timing_plan.save()

            ret.update({
                'code': code.TIMING_PLAN_POST_SUCCESS,
                'msg': msg.TIMING_PLAN_POST_SUCCESS,
                'user': user.name,
                'description': description
            })

            return Response(data=ret,
                            status=status.HTTP_200_OK)

        except Exception as e:
            ret.update({
                'code': code.TIMING_RECORD_POST_FAIL,
                'msg': msg.TIMING_RECORD_POST_FAIL,
            })
            print('exception occurs at posting TimingRecordView' + '*** %s ***' % str(type(e)))
            return Response(data=ret,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
