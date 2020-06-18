from rest_framework.views import APIView, Response

from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class UserDetail(APIView):
    # 前台携带 jwt token时 在前面加上 jwt 空格
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, req, *args, **kwargs):
        return Response({
            'result':{
                'username': req.user.username
            }
        })

    def post(self, req, *args, **kwargs):
        return Response({
            'result':{
                'username': req.user.username
            }
        })