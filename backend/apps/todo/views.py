from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from ..todo.models import Todo
from ..user.models import User, UserToken
from ..todoSet.models import TodoSet
from ..user.utils.auth import Authentication
from ..todo.serializers import TodoSerializer
from .utils import code, msg


# Create your views here.
class TodoView(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    #
    # def create(self, request, *args, **kwargs):
    #     ret = dict(
    #         code=code.TODO_POST_SUCCESS,
    #         msg=msg.TODO_POST_SUCCESS
    #     )
    #     token = request.GET.get('token')
    #     name = request.data.get('name', None)
    #     type = request.data.get('type', None)
    #     expectedTime = request.data.get('expectedTime', None)
    #     deadline = request.data.get('deadline', None)
    #     loopMode = request.data.get('loopMode', None)
    #     belongTodoSet = request.data.get('todoSetName', None)
    #     belongUser = request.data.get('userName', None)
    #
    #     token_obj = UserToken.objects.filter(token=token).first()
    #     use_id = User.objects.get(pk=token_obj.user.id)
    #
    #     todoSetObject = TodoSet.objects.filter(name=belongTodoSet, belongUser=use_id)
    #     if not todoSetObject:
    #
    #         raise exceptions.AuthenticationFailed(msg.AUTHENTICATION_FAIL)
    #     return token_obj.user, token_obj
    #
    #
    #
    #
    #     try:
    #         if

