from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils.auth import md5
from .utils import code
from .utils import msg
from . import models


class AuthView(APIView):
    """"
    User authentication.
    """
    authentication_classes = []

    @staticmethod
    def get(request, *args, **kwargs):
        return Response({'auth': 'get'}, status.HTTP_200_OK)

    @staticmethod
    def post(request, *args, **kwargs):

        ret = dict(code=code.AUTHENTICATION_FAIL,
                   msg=msg.AUTHENTICATION_FAIL)
        try:
            account = request.POST.get("account", None)
            password = request.POST.get("password", None)
            user = models.User.objects.filter(account=account, password=password).first()
            # if user doesn't exist
            if not user:
                ret.update({
                    'code': code.AUTHENTICATION_FAIL,
                    'msg': msg.AUTHENTICATION_ACCOUNT_PSW_ERROR,
                })
                return Response(ret, status.HTTP_200_OK)
            else:
                # create or update token for user
                token = md5(account)
                models.UserToken.objects.update_or_create(user=user, defaults={"token": token})
                ret.update({
                    'code': code.AUTHENTICATION_SUCCESS,
                    'msg': msg.AUTHENTICATION_SUCCESSFULLY,
                    'token': token,
                    'account': user.account,
                    'password': user.password,
                    'name': user.name,
                })

                return Response(ret, status.HTTP_200_OK)
        except Exception as e:
            print(e, '*** exception on auth view post')
            return Response(ret, status.HTTP_200_OK)


class RegisterView(APIView):
    """"
    User register.
    """
    authentication_classes = []

    @staticmethod
    def post(request, *args, **kwargs):

        ret = dict(code=code.REGISTER_FAIL,
                   msg=msg.REGISTER_USER_FAIL, )
        try:
            account = request.POST.get("account", None)
            password = request.POST.get("password", None)
            name = request.POST.get("name", None)
            try:
                models.User.objects.get(pk=account)
                ret.update({
                    'code': code.REGISTER_FAIL,
                    'msg': msg.REGISTER_USER_EXISTS,
                })
                return Response(ret, status.HTTP_200_OK)
            except Exception as e:
                print(e, '*** exception on getting users. ***')
                new_user = models.User()
                new_user.account = account
                new_user.password = password
                new_user.name = name
                new_user.save()

                ret.update({
                    'code': code.REGISTER_SUCCESS,
                    'msg': msg.REGISTER_USER_SUCCESSFULLY,
                    'account': account,
                    'password': password,
                    'name': name,
                })
                return Response(ret, status.HTTP_200_OK)

        except Exception as e:
            print(e, '*** exception on posting. ***')
            return Response(ret, status.HTTP_200_OK)
