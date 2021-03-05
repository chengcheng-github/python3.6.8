from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from register_and_login import models
from django.conf import settings
import json
import jwt
import time
import datetime

# import sys
# Create your views here.
# sys.path.append("../tools/login_check.py")
# 导包还是没导出自动补全,那就麻烦点把用到的函数在views里复制一遍吧


def login_check(func):
    def warp(request, *args, **kwargs):
        print("验证登录状态功能:显示客户端浏览器发送的token:")
        json_obj = json.loads(request.body.decode())
        # 如果前端发到这里的数据里,json里没有token这个键
        # 返回一个异常的json
        print(json_obj)
        # 貌似一定会有这个键..但是如果从window.localstorage里删掉就,键的值是null,传到后端服务端这里变none
        # if "token" not in json_obj:
        #     print("验证登录状态功能:前端提交的json里没有token键")
        #     result = {"code": 403, "error": "请登录"}
        #     return JsonResponse(result)

        # 如果有token就试着验证一下内容是否被修改,token是否过期
        try:
            payload = jwt.decode(
                json_obj["token"], settings.JWT_TOKEN_KEY, algorithms="HS256")
        except Exception as e:
            print("验证登录状态功能:token校验异常")
            print("异常:", e)
            result = {"code": 403, "error": "请登录"}
            print("校验结束,验证登录状态结束,返回出现异常的json到前端")
            return JsonResponse(result)

        # 现在,token通过校验了,从token中取出mail的值,在用户表中返回用户对象
        mail = payload["mail"]
        user = models.User.objects.get(mail=mail)
        user_info = models.User_info.objects.get(mail=mail)
        # 给request对象添加一个myuser属性(值是用户表里的用户对象)
        request.myuser = user
        request.myuser_info = user_info
        if request.myuser_info.user_vip == "1":
            print("vip校验")
            # print(request.myuser_info.user_vip_time)
            # 将datetime.datetime转化为时间戳
            vip_time_stamp = request.myuser_info.user_vip_time.timestamp()
            print(vip_time_stamp)
            # 当前时间时间戳
            print(time.time())
            if time.time() >= vip_time_stamp:
                print("消除vip状态")
                request.myuser_info.user_vip = ""
                request.myuser_info.user_vip_time = None
                request.myuser_info.save()

        return func(request, *args, **kwargs)
        pass
    return warp


class Show_Index_After_Login(View):
    # 下一行方法这个只有django里有
    @method_decorator(login_check)
    def post(self, request):
        # print(json_obj1)
        print("验证登录状态功能:正常运行")
        print()
        user_info = models.User_info.objects.get(mail=request.myuser)
        result = {"code": "2000", "error": "没有异常",
                  "my_site_1_user": user_info.nickname,
                  "user_mail": request.myuser.mail, }
        return JsonResponse(result)
        pass
    pass
