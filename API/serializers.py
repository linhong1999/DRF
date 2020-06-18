from rest_framework import serializers
from . import models


class PublishModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publish
        # 前台返回的字段
        fields = ('name', 'address')


class BookModelSerializer(serializers.ModelSerializer):

    # 外键序列化
    # publish = PublishModelSerializer()

    class Meta:
        model = models.Book
        # 前台返回的字段
        fields = ('name', 'price', 'publish_name', 'publish','author_list')
        # depth = 1
        '''
        fields = '__all__' # 前台返回字段 元组
        exclude = (tuple) # 剔除
        depth 深入表 可查看关联表 row 的内容
        # 在 model 中出现了方法 也可以在 fields 里添上
        '''


class BookListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        # print(self.child)
        print(instance)
        print(validated_data)
        for _instance, _validated_data in zip(instance,validated_data):
            self.child.update(_instance,_validated_data)

        return instance


class BookModelDeserializer(serializers.ModelSerializer):

    class Meta:

        model = models.Book
        # 前台返回的字段
        fields = ('name', 'price', 'publish', 'authors','img')
        extra_kwargs = {
            'name': {
                'max_length': 30,
                'required': True,
                'error_messages': {
                    'max_length': '太长',
                    'required': '这是必填项'
                }
            },
            'img': {
                # 'required': True,
                'error_messages': {
                    'required': '这是必填项'
                }
            }
        }
        list_serializer_class = BookListSerializer

        # depth = 1
        '''
        extra_kwargs # 用来完成反序列化字段的 系统校验规则
        # 单独定义局部钩子，用来处理一些特殊的逻辑，
        '''

    # def is_valid(self, raise_exception=False):
    #     self.context.get('request')

'''
在 fields 设置所有序列化和反序列化字段
所有自定义字段默认都是 read_only 如果再设置 write_only 会报错
最后再设置 反序列化 所需的 系统，局部，全局钩子 等校验规则
'''
class BookV2ModelSerializer(serializers.ModelSerializer):
    # 序列化反序列化整合
    class Meta:
        model = models.Book
        fields = ('name', 'price', 'img', 'publish','authors')
        extra_kwargs = {
            'publish': {
                'write_only': True,  # 只参与反序列化
            },
            'authors': {
                'write_only': True,  # read_only 只参与序列化
            },
        }