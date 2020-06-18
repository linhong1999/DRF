from django.shortcuts import render
from rest_framework.views import APIView,Response
from . import models,serializers


class Book(APIView):

    def get(self, req, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            book_obj = models.Book.objects.get(pk=pk, is_delete=False)
            book_ser = serializers.BookModelSerializer(book_obj).data
            return Response({
                'status':200,
                'msg': '',
                'results': book_ser,
            })
        else:
            book_query = models.Book.objects.filter(is_delete=False)
            book_ser_query = serializers.BookModelSerializer(book_query,many=True).data
            return Response({
                'status': 200,
                'msg': '',
                'results':book_ser_query,
            })

    def post(self, req, *args, **kwargs):
        book_query = req.data
        if isinstance(book_query, list):
            book_deser = serializers.BookModelDeserializer(data=book_query, many=True)
            many = True
        else:  # isinstance(book_query, dict):
            book_deser = serializers.BookModelDeserializer(data=book_query)
            many = False

        if book_deser.is_valid(raise_exception=True):
            book_query = book_deser.save()

        return Response({
            'status': 200,
            'msg': 'ok',
            'results': serializers.BookModelSerializer(book_query,many=many).data
        })

    def delete(self, req, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            pks = [pk]
        else:
            pks = req.data.get('pks')

        if models.Book.objects.filter(pk__in=pks,is_delete=False).update(is_delete=True):
            response = {
                'status': 0,
                'msg': '删除成功'
            }
        else:
            response = {
                'status': 1,
                'msg': '删除失败'
            }
        return Response(response)

    def put(self, req, *args, **kwargs):
        req_data = req.data
        pk = kwargs.get('pk')
        old_book_obj = models.Book.objects.filter(pk=pk).first()
        # 这样做只能整体修改
        # book_ser = serializers.BookModelDeserializer(instance=old_book_obj,data=req_data)
        # partial = True 局部修改 跳过校验
        book_ser = serializers.BookModelDeserializer(instance=old_book_obj,data=req_data, partial=True)

        book_ser.is_valid(raise_exception=True)
        book_ser.save()

        return Response({
            'stauts': 0,
            'msg': 'put ok',
        })

    def patch(self, req, *args, **kwargs):
        req_data = req.data
        pks = []
        if isinstance(req_data, dict):  # 单改
            pass
        elif isinstance(req_data, list):  #群改

            for book in req_data:
                pks.append(book.get('pk'))

            book_query = models.Book.objects.filter(pk__in=pks)
            # book_ser = serializers.BookModelDeserializer(instance=book_query, data=req_data, partial=True, many=True)
            # 如果要传 request 对象用context 因为 serializers 有 context属性 所以直接 self.context 获取即可
            book_ser = serializers.BookModelDeserializer(context={'request':req},instance=book_query, data=req_data, partial=True, many=True)
            book_ser.is_valid(raise_exception=True)
            book_ser.save()

        return Response({
            'status': 1,
            'msg': '数据有误',
        })

class BookV2(APIView):

    # 给 instance 是序列化 给 data 是反序列化
    def get(self, req, *args, **kwargs):

        pk = kwargs.get('pk')
        if pk:
            book_obj = models.Book.objects.get(pk=pk, is_delete=False)
            book_ser = serializers.BookV2ModelSerializer(book_obj).data
            return Response({
                'status':200,
                'msg': '',
                'results': book_ser,
            })
        else:
            book_query = models.Book.objects.filter(is_delete=False)
            book_ser_query = serializers.BookV2ModelSerializer(book_query,many=True).data
            return Response({
                'status': 200,
                'msg': '',
                'results':book_ser_query,
            })

    def post(self, req, *args, **kwargs):
        book_query = req.data
        if isinstance(book_query, list):
            pass
        elif isinstance(book_query, dict):
            pass
        else:
            return
        pass
