from django.conf.urls import url
from django.urls import path, re_path
from . import views,GenericAPIView
urlpatterns = [
    path('book/',views.Book.as_view()),
    re_path(r'book/(?P<pk>.*)/$', views.Book.as_view()),

    path('bookv2/',views.BookV2.as_view()),
    re_path(r'bookv2/(?P<pk>.*)/$', views.BookV2.as_view()),

    path('bookv3/',GenericAPIView.BookGenericAPIView.as_view()),
    re_path(r'bookv3/(?P<pk>.*)/$', GenericAPIView.BookGenericAPIView.as_view()),

    path('bookv4/',GenericAPIView.BookListGenericAPIView.as_view()),
    re_path(r'bookv4/(?P<pk>.*)/$', GenericAPIView.BookListGenericAPIView.as_view()),

    path('bookv5/',GenericAPIView.BookListCreateAPIView.as_view()),
    re_path(r'bookv5/(?P<pk>.*)/$', GenericAPIView.BookListCreateAPIView.as_view()),
]
