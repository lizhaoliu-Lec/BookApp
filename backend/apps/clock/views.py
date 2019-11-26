from rest_framework.viewsets import ModelViewSet
from ..clock.models import Clock
from ..todo.models import Todo
from ..todoSet.models import TodoSet
from ..todoSet.views import get_user
from ..clock.utils import msg, code
from ..clock.serializer import ClockSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED


# Create your views here.
class ClockView(ModelViewSet):
    model = Clock
    serializer_class = ClockSerializer

    def create(self, request, *args, **kwargs):
        ret = dict(
            code=code.CLOCK_POST_SUCCESS,
            msg=msg.CLOCK_POST_SUCCESS
        )
        startTime = request.data.get("startTime", None)
        endTime = request.data.get("endTime", None)
        reason = request.data.get("reason", None)
        isCompleted = request.data.get("isCompleted", None)
        todoName = request.data.get("todoName", None)
        todoSetName = request.data.get("todoSetName", None)

        # 1. check if todoSetName and todoName
        if todoSetName and todoName and isCompleted and endTime and startTime:
            # 2. check if there is todoSet object
            use_id = get_user(request)
            todo_set_obj = TodoSet.objects.filter(name=todoSetName, belongUser_id=use_id).first()
            if not todo_set_obj:
                ret.update(
                    code=code.CLOCK_POST_NO_TODO_SET,
                    msg=msg.CLOCK_POST_NO_TODO_SET
                )
                return Response(ret, HTTP_204_NO_CONTENT)
            else:
                todo_obj = Todo.objects.filter(name=todoName, belongTodoSet=todo_set_obj).first()
                if not todo_obj:
                    ret.update(
                        code=code.CLOCK_POST_NO_TODO,
                        msg=msg.CLOCK_POST_NO_TODO
                    )
                    return Response(ret, HTTP_204_NO_CONTENT)
                else:
                    print(startTime)
                    print(endTime)
                    clock_obj = Clock.objects.filter(startTime=startTime, endTime=endTime, isCompleted=isCompleted,
                                                     reason=reason, belongTodo=todo_obj).first()
                    if not clock_obj:
                        clock_obj = Clock(startTime=startTime, endTime=endTime, isCompleted=isCompleted,
                                          reason=reason, belongTodo=todo_obj)
                        clock_data = ClockSerializer(clock_obj, many=False).data
                        ret.update(
                            clock=clock_data
                        )
                        return Response(ret, HTTP_200_OK)
                    else:
                        ret.update(
                            code=code.CLOCK_POST_EXITED_CLOCK,
                            msg=msg.CLOCK_POST_EXITED_CLOCK
                        )
                        return Response(ret, HTTP_201_CREATED)
        else:
            ret.update(
                code=code.CLOCK_POST_NO_CONDITION,
                msg=msg.CLOCK_POST_NO_CONDITION
            )
            return Response(ret, HTTP_204_NO_CONTENT)