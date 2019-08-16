from django.db import models


class User(models.Model):
    class Meta:
        db_table = "user"

    account = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    created_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s-%s-%s" % (self.name, self.account, self.password)


class UserToken(models.Model):
    class Meta:
        db_table = "user_token"

    user = models.OneToOneField(User, on_delete=None)
    token = models.CharField(max_length=64)
    created_datetime = models.DateTimeField(auto_now=True)
    modified_datetime = models.DateTimeField(auto_now_add=True)
