from rest_framework.viewsets import ModelViewSet
from ..remain.models import Remain
from ..remain.serializers import RemainSerializer
from ..remain.utils import code, msg
from ..todoSet.views import get_user
from ..user.models import User
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED


# Create your views here.
class RemainView(ModelViewSet):
    queryset = Remain
    serializer_class = RemainSerializer

    def create(self, request, *args, **kwargs):
        ret = dict(
            code=code.REMAIN_POST_SUCCESS,
            msg=msg.REMAIN_POST_SUCCESS
        )
        detail = request.POST.get('detail', None)
        timeToRemind = request.POST.get('timeToRemind', None)
        repeatDay = request.data.get("repeatDay", None)

        try:
            user_id = get_user(request)
            user = User.objects.filter(id=user_id).first()
            if not user:
                ret.update(
                    code=code.REMAIN_POST_NO_USER,
                    msg=msg.REMAIN_POST_NO_USER
                )
                return Response(ret, HTTP_404_NOT_FOUND)
            else:
                if detail is not None and timeToRemind is not None and repeatDay is not None:
                    remain = Remain.objects.filter(detail=detail, timeToRemind=timeToRemind, user=user, repeatDay=repeatDay).first()
                    if not remain:
                        remain_new = Remain(detail=detail, timeToRemind=timeToRemind, user=user, repeatDay=repeatDay)
                        remain_new.save()
                        remain_data = RemainSerializer(remain_new, many=False).data
                        ret.update(
                            remain=remain_data
                        )
                        return Response(ret, HTTP_200_OK)
                    else:
                        ret.update(
                            code=code.REMAIN_POST_EXITED,
                            msg=msg.REMAIN_POST_EXITED
                        )
                        return Response(ret, HTTP_201_CREATED)

                else:
                    ret.update(
                        code=code.REMAIN_POST_CONDITION_ERROR,
                        msg=msg.REMAIN_POST_CONDITION_ERROR
                    )
                    return Response(ret, HTTP_404_NOT_FOUND)
        except Exception as e:
            ret.update(
                code=code.REMAIN_POST_FAIL,
                msg=msg.REMAIN_POST_FAIL
            )
            return Response(ret, HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        ret = dict(
            code=code.REMAIN_DELETE_SUCCESS,
            msg=msg.REMAIN_DELETE_SUCCESS
        )
        detail = request.POST.get('detail', None)

        try:
            user_id = get_user(request)
            user = User.objects.filter(id=user_id).first()
            if not user:
                ret.update(
                    code=code.REMAIN_DELETE_NO_USER,
                    msg=msg.REMAIN_DELETE_NO_USER
                )
                return Response(ret, HTTP_404_NOT_FOUND)
            else:
                if detail is not None:
                    remain = Remain.objects.filter(detail=detail, user=user).first()
                    if not remain:
                        ret.update(
                            msg=msg.REMAIN_DELETE_NO_REMAIN,
                            code=code.REMAIN_DELETE_NO_REMAIN
                        )
                        return Response(ret, HTTP_404_NOT_FOUND)
                    else:
                        remain.delete()
                        return Response(ret, HTTP_200_OK)
                else:
                    ret.update(
                        code=code.REMAIN_DELETE_CONDITION_ERROR,
                        msg=msg.REMAIN_DELETE_CONDITION_ERROR
                    )
                    return Response(ret, HTTP_404_NOT_FOUND)
        except Exception as e:
            ret.update(
                code=code.REMAIN_DELETE_FAIL,
                msg=msg.REMAIN_DELETE_FAIL
            )
            return Response(ret, HTTP_500_INTERNAL_SERVER_ERROR)