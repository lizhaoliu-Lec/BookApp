from rest_framework.viewsets import ModelViewSet
from ..todo.models import Todo
from ..todoSet.models import TodoSet
from ..todo.serializers import TodoSerializer
from .utils import code, msg
from rest_framework.response import Response
from ..todoSet.views import get_user
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_200_OK, \
    HTTP_500_INTERNAL_SERVER_ERROR
import datetime


# Create your views here.
class TodoView(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def create(self, request, *args, **kwargs):
        ret = dict(
            code=code.TODO_POST_SUCCESS,
            msg=msg.TODO_POST_SUCCESS
        )

        name = request.data.get('name', None)
        todo_set_name = request.data.get('todoSetName', None)

        # 1. check if there is name
        if name is None:
            ret.update(
                code=code.TODO_POST_NO_NAME,
                msg=msg.TODO_POST_NO_NAME
            )
            return Response(ret, HTTP_204_NO_CONTENT)
        # 2. check if there is todo_set_name
        if todo_set_name is None:
            ret.update(
                code=code.TODO_POST_NO_TODO_SET_NAME,
                msg=msg.TODO_POST_NO_TODO_SET_NAME
            )
            return Response(ret, HTTP_204_NO_CONTENT)
        # 3. check other conditions
        else:
            try:
                type = request.data.get('type', None)
                expectedTime = request.data.get('expectedTime', None)
                deadline = request.data.get('deadline', None)
                loopMode = request.data.get('loopMode', None)

                if type is None:
                    type = 0
                if expectedTime is None:
                    expectedTime = 25
                if deadline is None:
                    deadline = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if loopMode is None:
                    loopMode = 0

                use_id = get_user(request)

                # 2. check if there is todoSet
                todo_set_obj = TodoSet.objects.filter(name=todo_set_name, belongUser=use_id).first()
                if not todo_set_obj:
                    ret.update(
                        code=code.TODO_POST_TODO_SET_NOT_EXIT,
                        msg=msg.TODO_POST_TODO_SET_NOT_EXIT
                    )
                    return Response(ret, HTTP_404_NOT_FOUND)
                else:
                    todo_obj = Todo.objects.filter(name=name, belongTodoSet=todo_set_obj).first()
                    if todo_obj:
                        ret.update(
                            code=code.TODO_POST_EXITED,
                            msg=msg.TODO_POST_EXITED
                        )
                        return Response(ret, HTTP_201_CREATED)
                    else:
                        # 3. create todo
                        todo_obj_new = Todo(name=name, type=type, expectedTime=expectedTime, deadline=deadline,
                                            loopMode=loopMode, belongTodoSet=todo_set_obj)
                        todo_obj_new.save()
                        # 4. update todoSet
                        todo_set_obj.todoNum += 1
                        todo_set_obj.save()
                        todo_data = TodoSerializer(todo_obj_new, many=False).data
                        ret.update(
                            todo=todo_data
                        )
                        return Response(ret, HTTP_200_OK)
            except Exception as e:
                print('exception occurs at create todo' + ' *** %s ***' % str(type(e)))
                ret.update({
                    'code': code.TODO_POST_FAIL,
                    'msg': msg.TODO_POST_FAIL,
                })
                return Response(ret, HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        ret = dict(
            code=code.TODO_GET_SUCCESS,
            msg=msg.TODO_GET_SUCCESS
        )

        use_id = get_user(request)

        # 1. check if there is todoSet name
        todo_set_name = request.data.get("todoSetName", None)
        try:
            if todo_set_name is not None:
                todo_set_default = TodoSet.objects.filter(name=todo_set_name, belongUser_id=use_id).first()
                # 2. check if there is todo in todoSet
                if not todo_set_default:
                    ret.update(
                        code=code.TODO_GET_NOT_DEFAULT_TODO_SET,
                        msg=msg.TODO_GET_NOT_DEFAULT_TODO_SET
                    )
                    return Response(ret, HTTP_404_NOT_FOUND)
                else:
                    # print(todo_set_default.id, todo_set_default.name)
                    todo_default = Todo.objects.filter(belongTodoSet_id=todo_set_default.id)
                    print(todo_default)
                    if not todo_default:
                        ret.update(
                            code=code.TODO_GET_EMPTY,
                            msg=msg.TODO_GET_EMPTY
                        )
                        return Response(ret, HTTP_204_NO_CONTENT)
                    else:
                        todo_default_data = TodoSerializer(todo_default, many=True).data
                        ret.update(
                            todoList=todo_default_data
                        )
                        return Response(ret, HTTP_200_OK)
            else:
                todo_set_all = TodoSet.objects.filter(belongUser_id=use_id)
                if not todo_set_all:
                    ret.update(
                        code=code.TODO_GET_EMPTY,
                        msg=msg.TODO_GET_EMPTY
                    )
                    return Response(ret, HTTP_204_NO_CONTENT)
                else:
                    todo_list = {}
                    for todo_set in todo_set_all:
                        if todo_set.name != "默认":
                            todo_obj = Todo.objects.filter(belongTodoSet=todo_set)
                            todo_data = TodoSerializer(todo_obj, many=True).data
                            todo_list[todo_set.name] = todo_data
                    ret.update(
                        todo_list=todo_list
                    )
                    return Response(ret, HTTP_200_OK)

        except Exception as e:
            print('exception occurs at get todo' + ' *** %s ***' % str(type(e)))
            ret.update({
                'code': code.TODO_GET_FAIL,
                'msg': msg.TODO_GET_FAIL,
            })
            return Response(ret, HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, *args, **kwargs):
        ret = dict(
            code=code.TODO_UPDATE_SUCCESS,
            msg=msg.TODO_UPDATE_SUCCESS
        )

        # 1. check if there is todoName and todoSetName
        todoName = request.data.get("oldTodoName", None)
        todoSetName = request.data.get("todoSetName", None)
        if todoName is None or todoSetName is None:
            ret.update(
                code=code.TODO_UPDATE_NO_CONDITION,
                msg=msg.TODO_UPDATE_NO_CONDITION
            )
            return Response(ret, HTTP_204_NO_CONTENT)

        # 2. update todo
        else:
            deadline = request.data.get("deadline")
            expectedTime = request.data.get("expectedTime")
            type = request.data.get("type")
            loopMode = request.data.get("loopMode")
            newTodoName = request.data.get("newTodoName")
            use_id = get_user(request)
            try:
                # 2.1 check if there is todoSet
                todo_set_obj = TodoSet.objects.filter(name=todoSetName, belongUser_id=use_id).first()
                if not todo_set_obj:
                    ret.update(
                        code=code.TODO_UPDATE_NO_TODO_SET,
                        msg=msg.TODO_UPDATE_NO_TODO_SET
                    )
                    return Response(ret, HTTP_204_NO_CONTENT)
                else:
                    # 3. check if there is todo
                    todo_obj = Todo.objects.filter(name=todoName, belongTodoSet=todo_set_obj.id).first()
                    if todo_obj:
                        if deadline is not None:
                            # ????????????????????????????????????????????? how to update deadline
                            todo_obj.deadline = deadline
                        if expectedTime is not None:
                            todo_obj.expectedTime = expectedTime
                        if type is not None:
                            todo_obj.type = type
                        if loopMode is not None:
                            todo_obj.loopMode = loopMode
                        if newTodoName is not None:
                            todo_obj.name = newTodoName
                        todo_obj.save()
                        todo_obj_data = TodoSerializer(todo_obj, many=False).data
                        ret.update(
                            todo_new=todo_obj_data
                        )
                        return Response(ret, HTTP_200_OK)
                    else:
                        ret.update(
                            code=code.TODO_UPDATE_NO_TODO,
                            msg=msg.TODO_UPDATE_NO_TODO
                        )
                        return Response(ret, HTTP_204_NO_CONTENT)
            except Exception as e:
                print('exception occurs at update todo' + ' *** %s ***' % str(type(e)))
                ret.update({
                    'code': code.TODO_UPDATE_FAIL,
                    'msg': msg.TODO_UPDATE_FAIL,
                })
                return Response(ret, HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        ret = dict(
            code=code.TODO_DELETE_SUCCESS,
            msg=msg.TODO_DELETE_SUCCESS
        )
        todoSetName = request.data.get("todoSetName", None)
        todoName = request.data.get("todoName", None)
        if (todoSetName is None) or (todoName is None):
            ret.update(
                code=code.TODO_DELETE_NO_CONDITION,
                msg=msg.TODO_DELETE_NO_CONDITION
            )
            return Response(ret, HTTP_204_NO_CONTENT)
        else:
            try:
                use_id = get_user(request)
                # check if there is todoSet
                todo_set_obj = TodoSet.objects.filter(name=todoSetName, belongUser=use_id).first()
                if not todo_set_obj:
                    ret.update(
                        code=code.TODO_DELETE_NO_TODO_SET,
                        msg=msg.TODO_DELETE_NO_TODO_SET
                    )
                    return Response(ret, HTTP_204_NO_CONTENT)
                else:
                    # check if there is todo
                    todo_obj = Todo.objects.filter(name=todoName, belongTodoSet_id=todo_set_obj.id)
                    if todo_obj:
                        Todo.objects.filter(name=todoName, belongTodoSet_id=todo_set_obj.id).delete()
                        todo_set_obj.todoNum -= 1
                        todo_set_obj.save()
                        return Response(ret, HTTP_200_OK)
                    else:
                        ret.update(
                            code=code.TODO_DELETE_NO_TODO,
                            msg=msg.TODO_DELETE_NO_TODO
                        )
                        return Response(ret, HTTP_204_NO_CONTENT)
            except Exception as e:
                print('exception occurs at delete todo' + ' *** %s ***' % str(type(e)))
                ret.update({
                    'code': code.TODO_DELETE_FAIL,
                    'msg': msg.TODO_DELETE_FAIL,
                })
                return Response(ret, HTTP_500_INTERNAL_SERVER_ERROR)
