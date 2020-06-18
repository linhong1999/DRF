# 自定义认证类
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import BasePermission

from . import models
'''
1 继承 BaseAuthentication
2 重写 authenticate(self, request) 自定义认证规则
3 认证规则的基本条件：
        没有认证信息返回 None 游客
        有认证信息但认证失败抛出异常 非法用户
        有认证信息成功返回用户与认证信息元组 合法用户
4 完成视图类的全局（settings）或局部配置
'''
class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 前台在请求头携带认证信息， 默认规范 Authorization 字段携带认证信息
        # 后台固定在请求对象的 META 中获取
        auth = request.META.get('HTTP_AUTHORIZATION')

        # 游客
        if auth is None:
            return None

        auth_list = auth.split()
        # 校验合法还是非法
        if not(len(auth_list) == 2 and auth_list[0] == 'auth'):
            raise AuthenticationFailed('认证信息有误，非法用户')

        # 合法用户 从 auth_list[1] 解析
        # 设 abc.123.xyz 即可解析出 admin 用户
        if auth_list[1] != 'abc.123.xyz':
            raise AuthenticationFailed('用户校验失败，非法用户')

        user = models.User.objects.filter(username='lh').first()
        if not user:
            raise AuthenticationFailed('用户数据有误，非法用户')

        return user, None


class MyPermission(BasePermission):
    SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

    def has_permission(self, request, view):
        print(request.user.groups.values('name'))
        return True
        # return bool(
        #     request.method in self.SAFE_METHODS or
        #     request.user and
        #     request.user.is_authenticated
        # )

from rest_framework.throttling import SimpleRateThrottle
class Throttles(SimpleRateThrottle):
    scope = 'sms'

    # 只对 get 限制
    def get_cache_key(self, request, view):
        # .query_params 限制 GET  .data 限制 POST
        mobile = request.query_params.get('mobile') or request.data.get('mobile')
        # print(view)
        if not mobile:
            return None

        return 'throttle_%(scope)s_%(ident)s' % {'scope': self.scope, 'ident': mobile}
