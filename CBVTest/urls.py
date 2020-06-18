from django.conf.urls import url
from django.urls import path, re_path
from .CBV import Book,User

urlpatterns = [
    path('book/',Book.as_view()),
    re_path(r'book/(?P<pk>.*)/$', Book.as_view()),

    path('user/', User.as_view()),
    re_path(r'user/(?P<pk>.*)/$', User.as_view()),

]
