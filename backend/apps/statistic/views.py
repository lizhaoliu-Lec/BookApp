from rest_framework.viewsets import ModelViewSet
from ..statistic.models import Statistic
from ..statistic.serializers import StatisticSerializer
from ..statistic.utils import code, msg
from ..todoSet.views import get_user
from ..user.models import User
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_204_NO_CONTENT


# Create your views here.
class StatisticView(ModelViewSet):
    serializer_class = StatisticSerializer
    queryset = Statistic

    def list(self, request, *args, **kwargs):
        ret = dict(
            code=code.STATISTIC_GET_SUCCESS,
            msg=msg.STATISTIC_GET_SUCCESS
        )

        use_id = get_user(request)

        # 1. check if there is todoSet name
        day = request.data.get("day", None)
        month = request.data.get("month", None)
        try:
            user = User.objects.filter(id=use_id).first()
            if not user:
                ret.update(
                    code=code.STATISTIC_GET_NO_USER,
                    msg=msg.STATISTIC_GET_NO_USER
                )
                return Response(ret, HTTP_404_NOT_FOUND)
            else:
                # print(todo_set_default.id, todo_set_default.name)
                statistics = Statistic.objects.filter(user=use_id)
                if not statistics:
                    ret.update(
                        code=code.STATISTIC_GET_NO,
                        msg=msg.STATISTIC_GET_NO
                    )
                    return Response(ret, HTTP_204_NO_CONTENT)
                else:
                    statistics_data = StatisticSerializer(statistics, many=True).data
                    ret.update(
                        statistics=statistics_data
                    )
                    return Response(ret, HTTP_200_OK)
        except Exception as e:
            print('exception occurs at get todo' + ' *** %s ***' % str(type(e)))
            ret.update({
                'code': code.TODO_GET_FAIL,
                'msg': msg.TODO_GET_FAIL,
            })
            return Response(ret, HTTP_500_INTERNAL_SERVER_ERROR)
