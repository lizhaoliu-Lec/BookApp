from rest_framework.viewsets import ModelViewSet
from ..clockIn.serializers import ClockInSerializer
from ..clockIn.models import ClockIn
from ..todoSet.views import get_user
from ..clockIn.utils import code, msg
from ..user.models import User
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED, HTTP_200_OK


# Create your views here.
class ClockView(ModelViewSet):
    serializer_class = ClockInSerializer
    queryset = ClockIn

    def create(self, request, *args, **kwargs):
        ret = dict(
            code=code.CLOCK_IN_POST_SUCCESS,
            msg=msg.CLOCK_IN_POST_SUCCESS
        )
        punchTime = request.POST.get('punchTime', None)
        type = request.POST.get('type', None)

        try:
            user_id = get_user(request)
            user = User.objects.filter(id=user_id).first()
            if not user:
                ret.update(
                    code=code.CLOCK_IN_POST_NO_USER,
                    msg=msg.CLOCK_IN_POST_NO_USER
                )
                return Response(ret, HTTP_404_NOT_FOUND)
            else:
                if type is not None and punchTime is not None:
                    clockIn = ClockIn.objects.filter(type=type, punchTime=punchTime).first()
                    if not clockIn:
                        clockIn_new = ClockIn(user=user, punchTime=punchTime, type=type)
                        clockIn_new.save()
                        clockIn_data = ClockInSerializer(clockIn_new, many=False).data
                        ret.update(
                            clockIn=clockIn_data
                        )
                        return Response(ret, HTTP_200_OK)
                    else:
                        ret.update(
                            code=code.CLOCK_IN_POST_EXITED,
                            msg=msg.CLOCK_IN_POST_EXITED
                        )
                        return Response(ret, HTTP_201_CREATED)

                else:
                    ret.update(
                        code=code.CLOCK_IN_POST_CONDITION_ERROR,
                        msg=msg.CLOCK_IN_POST_CONDITION_ERROR
                    )
                    return Response(ret, HTTP_404_NOT_FOUND)
        except Exception as e:
            ret.update(
                code=code.CLOCK_IN_POST_FAIL,
                msg=msg.CLOCK_IN_POST_FAIL
            )
            return Response(ret, HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        ret = dict(
            code=code.CLOCK_IN_DELETE_SUCCESS,
            msg=msg.CLOCK_IN_DELETE_SUCCESS
        )
        punchTime = request.POST.get('punchTime', None)
        type = request.POST.get('type', None)

        try:
            user_id = get_user(request)
            user = User.objects.filter(id=user_id).first()
            if not user:
                ret.update(
                    code=code.CLOCK_IN_DELETE_NO_USER,
                    msg=msg.CLOCK_IN_DELETE_NO_USER
                )
                return Response(ret, HTTP_404_NOT_FOUND)
            else:
                if type is not None and punchTime is not None:
                    clockIn = ClockIn.objects.filter(type=type, punchTime=punchTime).first()
                    if not clockIn:
                        ret.update(
                            msg=msg.CLOCK_IN_DELETE_NO_CLOCK_IN,
                            code=code.CLOCK_IN_DELETE_NO_CLOCK_IN
                        )
                        return Response(ret, HTTP_404_NOT_FOUND)
                    else:
                        clockIn.delete()
                        return Response(ret, HTTP_200_OK)
                else:
                    ret.update(
                        code=code.CLOCK_IN_POST_CONDITION_ERROR,
                        msg=msg.CLOCK_IN_POST_CONDITION_ERROR
                    )
                    return Response(ret, HTTP_404_NOT_FOUND)
        except Exception as e:
            ret.update(
                code=code.CLOCK_IN_DELETE_FAIL,
                msg=msg.CLOCK_IN_DELETE_FAIL
            )
            return Response(ret, HTTP_500_INTERNAL_SERVER_ERROR)