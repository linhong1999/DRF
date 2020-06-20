# -*- coding: utf-8 -*-

from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 2


class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 5

    # http://127.0.0.1:8000/v1/cars/?offset=2&limit=2 偏移两条 拿两条 跳过1，2拿3，4
