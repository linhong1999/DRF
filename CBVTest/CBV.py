

# from django.views import View
#
# class Tester(View):
#     def get(self,req):
#         print('----get----',req.GET)
#         return HttpResponse('i am get')
#
#     def post(self,req):
#         print('----post----',req.POST)
#         return HttpResponse('i am post')
from . import models
from .serializers import UserSerializer,UserDeserializer,CarModelSerializer
from rest_framework.views import APIView ,Response
class Book(APIView):
    def get(self,req,*args,**kwargs):

        obj = models.Book.objects.filter(pk = kwargs['pk']).values('title','price').first()
        obj = models.Book.objects.get(pk = kwargs['pk'])
        print(obj,type(obj))
        return Response({
            'results': obj
        })
        # 设置为json_dumps_params={‘ensure_ascii’：False}不进行转码
        # return render(req,'index.html',context=obj)

    def post(self,req,*args,**kwargs):
        print(args)
        print(kwargs)
        print('----post----',req._request.POST) # 二次封装
        print('----post----',req.POST)
        print('----post----',req.data) #兼容
        print('----get----',req.query_params)

        return Response('i am post')


class User(APIView):

    def get(self, req, *args, **kwargs):
        pk = kwargs.get('pk')

        if pk:
            user_obj = models.User.objects.get(pk = pk)
            return Response({
                'status' : 200,
                'msg' : 'success',
                'results': UserSerializer(user_obj).data
            })
        else:
            user_obj_list = models.User.objects.all()
            return Response({
                'status': 200,
                'msg': 'success',
                'results': UserSerializer(user_obj_list,many=True).data
            })

    def post(self, req, *args, **kwargs):

        req_data = req.data
        if not isinstance(req_data, dict):
            return Response({
                'status': 500,
                'msg': '数据有误',
            })

        # 反序列化数据

        user_deser = UserDeserializer(data=req_data)
        if user_deser.is_valid():  # 这一步是必须的
            user_obj = user_deser.save() # 必须写 create 方法

            msg = '校验通过'
            result = UserSerializer(user_obj).data
            # result = '成功'
        else:
            # 校验失败的信息都会存在 反序列化对象.errors
            msg = user_deser.errors
            result = ''
        return Response({
            'status': 200,
            'msg': msg,
            'result': result,
        })

from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import MyPageNumberPagination, MyLimitOffsetPagination
class CarListAPIView(ListAPIView):
    queryset = models.Car.objects.all()
    serializer_class = CarModelSerializer

    # 局部配置过滤类 (全局配置 DEFAULT_FILTER_BACKENDS)
    filter_backends = [SearchFilter, OrderingFilter]
    # SearchFilter过滤类依赖的过滤条件 ： 接口： /cars/?search=...
    search_fields = ['name', 'brand']  # 多个字段，多个模糊查询
    ordering_fields = ['price', 'pk']
    # 127.0.0.1:8000/v1/cars/?search=1&ordering=-price&ordering=pk 多个排序条件
    # 127.0.0.1:8000/v1/cars/?search=1&ordering=-price,pk 也可

    pagination_class = MyLimitOffsetPagination


