# django 脚本化启动
import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'day_0613.settings')
django.setup()

from Permissions import models

user = models.User.objects.first()  # type: models.User
print(user.username)
print(user.groups.first())
print(user.user_permissions.first().name)

print('-'*30)

from django.contrib.auth.models import Group
group = Group.objects.first()
print(group.name)
print(group.user_set.first().username)
print(group.permissions.first().name)

print('-'*30)

from django.contrib.auth.models import Permission

permission = Permission.objects.filter(pk=45).first()
print(permission.user_set.first().username)
permission = Permission.objects.filter(pk=46).first()
print(permission.group_set.first().name)

# from API import models

# print(models.Author.objects.values('id','book__price'))
# author = models.Author.objects.first()
# print(author)
# print(author.authordetail.mobile)