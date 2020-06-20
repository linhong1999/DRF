
from rest_framework import serializers, exceptions
from django.conf import settings
from . import models

class UserSerializer(serializers.Serializer):

    name = serializers.CharField()
    phone = serializers.CharField()
    sex = serializers.SerializerMethodField()
    icon = serializers.SerializerMethodField()

    def get_sex(self,obj):
        return obj.get_sex_display()

    def get_icon(self,obj):
        return '{}{}{}'.format('http://127.0.0.1:8000',settings.MEDIA_URL,str(obj.icon))


class UserDeserializer(serializers.Serializer):

    # 反序列化字段都是原来入库的，故不会出现自定义
    # 自定义校验规则
    name = serializers.CharField(
        max_length = 20,
        min_length = 1,
        error_messages= {
            'max_length' : '字段太长',
            'min_length' : '字段太短',
        }
    )
    pwd = serializers.CharField()
    phone = serializers.CharField(
        required = False
    )
    sex = serializers.IntegerField(
        required = False
    )

    re_pwd = serializers.CharField()
    # 局部构造 validate_字段名
    def validate_name(self,value):
        print('value', value)
        return value

    # 全局钩子 attrs: 系统与局部钩子校验通过的所有数据
    def validate(self, attrs):
        pwd = attrs.get('pwd')
        re_pwd = attrs.pop('re_pwd')
        if pwd != re_pwd:
            raise exceptions.ValidationError({'pwd':'两次密码不一致'})

        print('attrs', attrs)
        return attrs

    # 必须写
    def create(self, validated_data):

        print('validated_data', validated_data)
        return models.User.objects.create(**validated_data)


    # icon = serializers.SerializerMethodField()

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Car
        fields = ['name', 'price', 'brand']
