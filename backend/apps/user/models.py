from django.db import models


class User(models.Model):
    class Meta:
        db_table = "user"

    account = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

    def __str__(self):
        return "%s-%s-%s" % (self.name, self.account, self.password)


# class Machines(models.Model):
#     class Meta:
#         db_table = "machines"
#
#     machine_num = models.CharField(max_length=20, primary_key=True)
#     user = models.ManyToManyField(Users, through="User_Machine_relationship")
#
#     def __str__(self):
#         return "%s" % (self.machine_num)


# class User_Machine_relationship(models.Model):
#     class Meta:
#         db_table = "user_machine_relationship"
#
#     # 关联外键
#     account = models.ForeignKey("Users", on_delete=models.CASCADE)
#     machine_num = models.ForeignKey("Machines", on_delete=models.CASCADE)
#     address = models.CharField(max_length=20)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#
#     def __str__(self):
#         return "%s-%s-%s-%s-%s" % (self.account, self.machine_num, self.address, self.start_time, self.end_time)


class UserToken(models.Model):
    class Meta:
        db_table = "user_token"

    user = models.OneToOneField(User, on_delete=None)
    token = models.CharField(max_length=64)
