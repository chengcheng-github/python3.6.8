#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author JourWon
# @date 2021/2/17
# @file login.py
import jwt
from django.http import JsonResponse
from django.conf import settings


def login_check(func):
    def wrap(request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            result = {'code': 403, 'errpr': '请登录'}
            return JsonResponse(result)
        try:
            # decode 方法中 首先会验签 签名是否有效
            # 验签通过后 从payload获取有效期 判断token是否在有效期内
            payload = jwt.decode(token,
                                 settings.JWT_TOKEN_KEY,
                                 algorithms='HS256')
        except:
            result = {'code': 403, 'error': '请登录'}
            return JsonResponse(result)
            # 从结果中获取私有声明
        username = payload['username']
        # 根据用户名称获取用户对象
        # user = UserProfile.objects.get(username=username)
        # 将用户对象作为request的附加属性
        # request.myuser = user
        # 调用所修饰的函数
        return func(request, *args, **kwargs)

    return wrap

def get_user_by_reuqest(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    if not token:
        return None

