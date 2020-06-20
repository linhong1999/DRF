from django.urls import path, re_path
from . import views,JWTTest
from rest_framework_jwt.views import ObtainJSONWebToken,obtain_jwt_token
urlpatterns = [
    path('test/',views.TestAPIView.as_view()),
    path('test2/',views.TestAPIView2.as_view()),
    path('test3/',views.TestAPIView3.as_view()),
    path('test4/',views.TestAPIView4.as_view()),
    path('sms/',views.TestThrottles.as_view()),

    # 登录
    #path('login/',ObtainJSONWebToken.as_view()),  # 两个一样
    path('login/',obtain_jwt_token),              # 只提供了 post 方法
    path('user_detail/',JWTTest.UserDetail.as_view()),              # 只提供了 post 方法
    # path('login/',JWTTest.JWTTestToken.as_view()),

    path('loginv2/', views.LoginAPIView.as_view()),  # 只提供了 post 方法

]
