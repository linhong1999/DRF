from rest_framework.views import APIView,Response
# Create your views here.


class TestAPIView(APIView):
    def get(self, req, *args, **kwargs):
        return Response({
            'msg': 'test ok',
        })

from rest_framework.permissions import IsAuthenticated
class TestAPIView2(APIView):  # 只有登录之后才能访问
    permission_classes = [IsAuthenticated,]
    def get(self, req, *args, **kwargs):
        return Response({
            'msg': 'test login ok',
        })

from rest_framework.permissions import IsAuthenticatedOrReadOnly
class TestAPIView3(APIView):  # 只有登录之后才能访问
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, req, *args, **kwargs):
        return Response({
            'msg': 'test 读 ok',
        })

    def post(self, req, *args, **kwargs):
        return Response({
            'msg': 'test 写 ok',
        })

# 游客只读，登录用户只读，只有登录用户属于 管理员 分组，才能增删改
from Permissions.authentications import MyPermission
class TestAPIView4(APIView):  # 只有登录之后才能访问
    permission_classes = [MyPermission]

    def get(self, req, *args, **kwargs):
        return Response({
            'msg': 'test 读 ok',
        })

    def post(self, req, *args, **kwargs):
        return Response({
            'msg': 'test 写 ok',
        })


from Permissions.authentications import Throttles
class TestThrottles(APIView):  # 只有登录之后才能访问
    throttle_classes = [Throttles]

    def get(self, req, *args, **kwargs):
        return Response({
            'msg': 'get 获取 ok',
        })

    def post(self, req, *args, **kwargs):
        return Response({
            'msg': 'post 获取 ok',
        })