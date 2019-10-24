from django.db import models


class User(models.Model):
    class Meta:
        db_table = "user"

    account = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    signature = models.CharField(max_length=50, null=True)  # allow signature to be null

    def __str__(self):
        return "%s-%s-%s-%s" % (self.name, self.account, self.password, self.signature)


class UserToken(models.Model):
    class Meta:
        db_table = "user_token"

    user = models.OneToOneField(User, on_delete=None)
    token = models.CharField(max_length=64)
