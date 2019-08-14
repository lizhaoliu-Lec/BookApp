import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..user.utils.auth import Authentication
from .models import TimingRecord
from .serializers import TimingRecordSerializer
from .utils.data import TIMING_TYPE_2_INT


class TimingRecordView(APIView):
    authentication_classes = [Authentication, ]

    def get(self, *args, **kwargs):
        try:
            user = self.request.user
            timing_records = TimingRecord.objects.filter(user=user)
            timing_records = TimingRecordSerializer(instance=timing_records, many=True)
            for d in timing_records.data:
                int_type = TIMING_TYPE_2_INT[d['type']]
                if int_type == 1 or int_type == 2:
                    del d['time']
                    del d['end_time']

            return Response(data=timing_records.data,
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data='exception occurs at getting TimingRecordView' + '*** %s ***' % str(type(e)),
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, *args, **kwargs):
        try:
            user = self.request.user
            str_type = self.request.POST.get('type', None)
            str_start_time = self.request.POST.get('start_time', None)
            start_time = datetime.datetime.strptime(str_start_time, '%Y-%m-%d %H:%M:%S')
            remark = self.request.POST.get('remark', None)

            if not (str_type and start_time and remark):
                return Response(data='type, start_time and remark must provided.',
                                status=status.HTTP_200_OK)

            int_type = TIMING_TYPE_2_INT.get(str_type, None)

            if int_type is None:
                return Response(data='type must be one of `%s`' % ', '.join(TIMING_TYPE_2_INT.keys()),
                                status=status.HTTP_200_OK)

            if int_type == 0:
                time = self.request.POST.get('time', None)
                str_end_time = self.request.POST.get('end_time', None)
                if not (time and str_end_time):
                    return Response(data='Time and end_time must provided.',
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

            return Response(data='Timing Record post!',
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data='exception occurs at posting TimingRecordView' + '*** %s ***' % str(type(e)),
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
