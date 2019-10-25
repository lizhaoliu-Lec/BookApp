from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ..todoSet.models import TodoSet
from ..todoSet.serializer import TodoSetSerializer
from ..todoSet.utils import code, msg
from ..user.models import User, UserToken
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED, HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR


# get user from database
def get_user(request):
    token = request.GET.get('token')
    token_obj = UserToken.objects.filter(token=token).first()
    use_id = User.objects.get(pk=token_obj.user.id)
    return use_id


# Create your views here.
class TodoSetView(ModelViewSet):
    model = TodoSet
    serializer_class = TodoSetSerializer

    def create(self, request, *args, **kwargs):
        ret = dict(
            code=code.TODOSET_POST_SUCCESS,
            msg=msg.TODOSET_POST_SUCCESS
        )

        # 0. take the use object from database
        use_id = get_user(request)

        name = request.data.get('name', None)
        # 1. check if there is name for todoSet
        if name is None:
            ret.update(
                code=code.TODOSET_NOT_NAME,
                msg=msg.TODOSET_NOT_NAME
            )
            return Response(ret, HTTP_204_NO_CONTENT)
        else:
            # 1.1 check if there had exit todoSet
            try:
                todo_set_obj = TodoSet.objects.filter(name=name, belongUser=use_id).first()
                if not todo_set_obj:
                    TodoSet.objects.create(name=name, belongUser=use_id)
                    return Response(ret, HTTP_200_OK)
                else:
                    ret.update(
                        code=code.TODOSET_EXITED,
                        msg=msg.TODOSET_EXITED
                    )
                    return Response(ret, HTTP_201_CREATED)

            except Exception as e:
                print('exception occurs at create todoSet' + '*** %s ***' % str(type(e)))
                ret.update({
                    'code': code.TODOSET_SERVER_ERROR,
                    'msg': msg.TODOSET_SERVER_ERROR,
                })
                return Response(ret, HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        ret = dict(
            code=code.T0DOSET_GET_SUCCESS,
            msg=msg.T0DOSET_GET_SUCCESS
        )

        use_id = get_user(request)

        try:
            print(use_id)
            todo_set_all = TodoSet.objects.filter(belongUser=use_id).data

            todo_set_all_data = TodoSetSerializer(todo_set_all, many=True)
            if len(todo_set_all_data) == 0:
                ret.update(
                    code=code.TODOSET_GET_EMPTY,
                    msg=msg.TODOSET_GET_EMPTY
                )
                return Response(ret, HTTP_204_NO_CONTENT)
            else:
                return Response(todo_set_all_data, HTTP_200_OK)

        except Exception as e:
            print('exception occurs at get todoSet' + ' *** %s ***' % str(type(e)))
            ret.update({
                'code': code.TODOSET_GET_FAIL,
                'msg': msg.TODOSET_GET_FAIL,
            })
            return Response(ret, HTTP_500_INTERNAL_SERVER_ERROR)

