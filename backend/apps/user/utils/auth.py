import hashlib
import time
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from .. import models


class Authentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.GET.get('token')
        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed("用户认证失败")
        return token_obj.user, token_obj


def md5(account):
    ctime = str(time.time())
    m = hashlib.md5(bytes(account, encoding="utf-8"))
    m.update(bytes(ctime, encoding="utf-8"))
    return m.hexdigest()
