# -*- coding: utf-8 -*-
import re
# from django.core.exceptions import DoesNotExist
from rest_framework import serializers
from rest_framework import serializers, exceptions
from Permissions.models import User
from rest_framework_jwt.settings import api_settings
from . import models

jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER


class UserModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('username', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

    def validate_password(self, value):
        return value

    def validate(self, attrs):

        username = attrs.get('username')
        password = attrs.get('password')
        mobile_regex = r'^1[3-8]\d{9}$'
        email_regex = r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$'
        user = None
        try:
            if re.match(mobile_regex, username):
                user = models.User.objects.get(mobile=username)
            elif re.match(email_regex, username):
                user = models.User.objects.get(email=username)
            else:
                user = models.User.objects.get(username=username)
        except User.DoesNotExist as err_msg:
            raise exceptions.ValidationError("账号信息不存在")

        if user and user.check_password(password):
            # 设置token
            payload = jwt_payload_handler(user)
            self.token = jwt_encode_handler(payload)
            self.user = user

            return attrs


