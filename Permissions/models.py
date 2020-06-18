from django.db import models
from django.contrib.auth.models import AbstractUser

# 用户表 角色 groups 权限 user_permissions
# 角色表 用户 user_set 权限 permissions
# 权限表 用户 user_set 角色 group_set
class User(AbstractUser):
    mobile = models.CharField(max_length=11,unique=True)

    class Meta:
        db_table = 'newuser'
        verbose_name = '自定义用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
