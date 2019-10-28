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
    return token_obj.user_id
    # use_id = User.objects.get(pk=token_obj.user.id)
    # return use_id


# Create your views here.
class TodoSetView(ModelViewSet):
    model = TodoSet
    serializer_class = TodoSetSerializer

    def create(self, request, *args, **kwargs):
        ret = dict(
            code=code.TODO_SET_POST_SUCCESS,
            msg=msg.TODO_SET_POST_SUCCESS
        )

        # 0. take the use object from database
        use_id = get_user(request)

        name = request.data.get('name', None)
        # 1. check if there is name for todoSet
        if name is None:
            ret.update(
                code=code.TODO_SET_NOT_NAME,
                msg=msg.TODO_SET_NOT_NAME
            )
            return Response(ret, HTTP_204_NO_CONTENT)
        else:
            # 1.1 check if there had exit todoSet
            try:
                todo_set_obj = TodoSet.objects.filter(name=name, belongUser=use_id).first()
                if not todo_set_obj:
                    todo_set_new = TodoSet(name=name, belongUser_id=use_id)
                    # TodoSet.objects.create(name=name, belongUser=use_id)
                    todo_set_new.save()
                    todo_set_new_data = TodoSetSerializer(todo_set_new, many=False).data
                    ret.update(
                        todoSet=todo_set_new_data
                    )
                    return Response(ret, HTTP_200_OK)
                else:
                    ret.update(
                        code=code.TODO_SET_EXITED,
                        msg=msg.TODO_SET_EXITED
                    )
                    return Response(ret, HTTP_201_CREATED)

            except Exception as e:
                print('exception occurs at create todoSet' + '*** %s ***' % str(type(e)))
                ret.update({
                    'code': code.TODO_SET_SERVER_ERROR,
                    'msg': msg.TODO_SET_SERVER_ERROR,
                })
                return Response(ret, HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        ret = dict(
            code=code.T0DO_SET_GET_SUCCESS,
            msg=msg.T0DO_SET_GET_SUCCESS
        )

        use_id = get_user(request)

        try:
            todo_set_all = TodoSet.objects.filter(belongUser_id=use_id)
            todo_set_all_data = TodoSetSerializer(todo_set_all, many=True)
            if len(todo_set_all_data.data) == 0:
                ret.update(
                    code=code.TODO_SET_GET_EMPTY,
                    msg=msg.TODO_SET_GET_EMPTY
                )
                return Response(ret, HTTP_204_NO_CONTENT)
            else:
                ret.update(
                    todoSetList=todo_set_all_data.data
                )
                return Response(ret, HTTP_200_OK)

        except Exception as e:
            print('exception occurs at get todoSet' + ' *** %s ***' % str(type(e)))
            ret.update({
                'code': code.TODO_SET_GET_FAIL,
                'msg': msg.TODO_SET_GET_FAIL,
            })
            return Response(ret, HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, *args, **kwargs):
        ret = dict(
            code=code.TODO_SET_UPDATE_SUCCESS,
            msg=msg.TODO_SET_UPDATE_SUCCESS
        )

        use_id = get_user(request)
        # todo_set_id = kwargs['todoSetID']
        # print(todo_set_id)
        old_todo_set_name = request.data.get('oldTodoSetName')
        new_todo_set_name = request.data.get('newTodoSetName')

        try:
            todo_set_obj = TodoSet.objects.filter(name=old_todo_set_name, belongUser_id=use_id).first()
            if not todo_set_obj:
                ret.update(
                    code=code.TODO_SET_UPDATE_NOT_EXIT,
                    msg=msg.TODO_SET_UPDATE_NOT_EXIT
                )
                return Response(ret, HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                todo_set_obj.name = new_todo_set_name
                todo_set_obj.save()
                todo_set = TodoSetSerializer(todo_set_obj, many=False)
                todo_set_data = todo_set.data
                ret.update(
                    todoSet=todo_set_data
                )
                return Response(ret, HTTP_200_OK)
        except Exception as e:
            print('exception occurs at update todoSet' + ' *** %s ***' % str(type(e)))
            ret.update({
                'code': code.TODO_SET_UPDATE_FAIL,
                'msg': msg.TODO_SET_UPDATE_FAIL,
            })
            return Response(ret, HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        ret = dict(
            code=code.TODO_SET_DELETE_SUCCESS,
            msg=msg.TODO_SET_DELETE_SUCCESS
        )
        # todo_set_id = kwargs['todoSetID']
        todo_set_name = request.data.get("todoSetName")
        use_id = get_user(request)
        todo_set_obj = TodoSet.objects.filter(name=todo_set_name, belongUser_id=use_id).first()
        if not todo_set_obj:
            ret.update(
                code=code.TODO_SET_UPDATE_NOT_EXIT,
                msg=msg.TODO_SET_UPDATE_NOT_EXIT
            )
            return Response(ret, HTTP_204_NO_CONTENT)
        else:
            try:
                TodoSet.objects.filter(name=todo_set_name, belongUser_id=use_id).delete()
                return Response(ret, HTTP_200_OK)
            except Exception as e:
                print('exception occurs at delete todoSet' + ' *** %s ***' % str(type(e)))
                ret.update({
                    'code': code.TODO_SET_DELETE_FAIL,
                    'msg': msg.TODO_SET_DELETE_FAIL,
                })
                return Response(ret, HTTP_500_INTERNAL_SERVER_ERROR)

