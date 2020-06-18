from rest_framework.generics import GenericAPIView
from . import models,serializers
from rest_framework.views import Response
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin


class BookGenericAPIView(GenericAPIView):
    queryset = models.Book.objects.filter(is_delete=False)
    serializer_class = serializers.BookModelSerializer
    def get(self, req, *args, **kwargs):
        # book_query = models.Book.objects.filter(is_delete=False)
        book_query = self.get_queryset()
        # book_query = self.get_object() 单取 many=False
        # book_ser = serializers.BookModelSerializer(book_query, many=True).data
        book_ser = self.get_serializer(book_query, many=True).data
        return Response({
            'result': book_ser,
        })


class BookListGenericAPIView(RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = models.Book.objects.filter(is_delete=False)
    serializer_class = serializers.BookModelSerializer

    def get(self, req, *args, **kwargs):  # 群查
        if kwargs.get('pk'):
            response = self.retrieve(req, *args, **kwargs)
        else:
            response = self.list(req, *args, **kwargs)
        return response

    def post(self, req, *args, **kwargs):
        response = self.create(req, *args, **kwargs)
        return response

    def put(self, req, *args, **kwargs):
        response = self.update(req, *args, **kwargs)
        return response

    def patch(self, req, *args, **kwargs):
        response = self.partial_update(req, *args, **kwargs)
        return response


from rest_framework.generics import ListCreateAPIView
'''
generics 封装了很多 自己去看
'''


# 群查和单增
class BookListCreateAPIView(ListCreateAPIView):
    queryset = models.Book.objects.filter(is_delete=False)
    serializer_class = serializers.BookModelSerializer
