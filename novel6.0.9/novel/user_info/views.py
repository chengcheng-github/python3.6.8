from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse
from django.http import HttpResponse
from register_and_login import models
from django.utils.decorators import method_decorator
from django.conf import settings
import json
import jwt
import time
import datetime
# Create your views here.


class User_Info(View):
    def post(self, request, username):
        print("显示用户个人信息功能:")
        print("前端通过url传递需要查找的用户邮箱:", username)
        try:
            user = models.User_info.objects.get(mail=username)
        except Exception as e:
            print(e)
            print("显示用户个人信息功能异常:在用户信息表User_info里没有查到邮箱为",
                  username, "的用户,向前端浏览器返回异常的json")
            result = {"code": "10104", "error": "用户邮箱异常"}
            print()
            return JsonResponse(result)
        if user.user_vip == "1":
            print("vip校验")
            # print(request.myuser_info.user_vip_time)
            # 将datetime.datetime转化为时间戳
            vip_time_stamp = user.user_vip_time.timestamp()
            print(vip_time_stamp)
            # 当前时间时间戳
            print(time.time())
            if time.time() >= vip_time_stamp:
                print("消除vip状态")
                user.user_vip = ""
                user.user_vip_time = None
                user.save()
        print()
        user_info = {}
        user_info["nickname"] = user.nickname
        print("用户名:", user.nickname)
        # 这东西要改成str再发到前端浏览器
        user_info["avatar"] = str(user.avatar)
        print("用户头像:", user.avatar)
        user_info["collection"] = user.collection
        print("用户收藏:", user.collection)
        user_info["user_type"] = user.user_type
        print("用户类型:", user.user_type)
        user_info["created_time"] = user.created_time
        print("用户注册时间:", user.created_time)
        user_info["updated_time"] = user.updated_time
        print("用户更新资料时间:", user.updated_time)
        user_info["phone"] = user.phone
        print("用户手机号:", user.phone)
        user_info["user_vip"] = user.user_vip
        print("用户vip状态:", user.user_vip)
        user_info["user_vip_time"] = user.user_vip_time
        print("用户vip截止时间:", user.user_vip_time)
        result = {"code": "2000", "data": user_info, }
        print()
        return JsonResponse(result)
        pass


def login_check(func):
    def warp(request, *args, **kwargs):
        print("验证登录状态功能:显示客户端浏览器发送的token:")
        json_obj = json.loads(request.body.decode())
        # 如果前端发到这里的数据里,json里没有token这个键
        # 返回一个异常的json
        print(json_obj)
        # 好像一定会有这个键..但是如果从window.localstorage里删掉就,键的值是null,传到后端服务端这里变none
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
        if json_obj["usermail"] != mail:
            print("验证登录状态功能:token与浏览器存储登录账户邮箱不匹配")
            result = {"code": 405, "error": "token与浏览器存储登录账户邮箱不匹配"}
            print("校验结束,验证登录状态结束,返回出现异常的json到前端")
            return JsonResponse(result)

        # 下面两行数据库里表里的记录,在orm里是对象
        user = models.User.objects.get(mail=mail)
        user_info = models.User_info.objects.get(mail=user)
        # 给request对象添加一个myuser属性(值是用户表里的用户对象)
        request.myuser = user
        # 把用户信息页添加进request属性里
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
        print()
        return func(request, *args, **kwargs)
        pass
    return warp


def login_check2(func):
    def warp(request, *args, **kwargs):
        token = request.META.get("HTTP_AUTHORIZATION")
        if not token:
            result = {"code": 403, "error": "请登录"}
            print("校验结束,验证登录状态结束,返回出现异常的json到前端")
            return JsonResponse(result)
            pass
        try:
            payload = jwt.decode(
                token, settings.JWT_TOKEN_KEY, algorithms="HS256")
        except Exception as e:
            print("验证登录状态功能:token校验异常")
            print("异常:", e)
            result = {"code": 403, "error": "请登录"}
            print("校验结束,验证登录状态结束,返回出现异常的json到前端")
            return JsonResponse(result)

        # 下面两行数据库里表里的记录,在orm里是对象
        user = models.User.objects.get(mail=payload["mail"])
        user_info = models.User_info.objects.get(mail=user)
        # 给request对象添加一个myuser属性(值是用户表里的用户对象)
        request.myuser = user
        # 把用户信息页添加进request属性里
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
        print()
        return func(request, *args, **kwargs)
        pass
    return warp


class User_Info_Change(View):
    @method_decorator(login_check)
    def post(self, request, username):
        print("修改个人信息功能(显示个人信息):")
        print("先看看返回给前端浏览器的个人信息:")
        # print(request.myuser_info)
        # 因为是对象,所以可以用.__dict__方法得到属性与方法字典
        # 直接输出字典会输出键值对(字典形式输出)
        # print(request.myuser_info.__dict__)
        # 遍历字典输出只输出键,需要手动把值也加上
        # 这里是返回字典(Json)
        res = {}
        for item in request.myuser_info.__dict__:
            if item != "_state" and item != "id":
                # 为了针对这个avatar路径..把全部字段的值都弄成字符串
                res[item] = str(request.myuser_info.__dict__[item])
        for item in res:
            print(item, ":", res[item])

        print()
        return JsonResponse({"code": "2000", "data": res})


class User_Info_Change_Avatar(View):
    @method_decorator(login_check2)
    def post(self, request, username):
        # 用FormData对象(FormData()),直接提交就行了,什么请求头都不需要
        request.myuser_info.avatar = request.FILES.get("avatar")
        request.myuser_info.save()
        return JsonResponse({"code": "2000", "useravatar": str(request.myuser_info.avatar)})


class Change_User_Info(View):
    @method_decorator(login_check2)
    def post(self, request, username):
        # print(333)
        json_obj = json.loads(request.body.decode())
        print(json_obj)
        request.myuser_info.phone = json_obj["phone"]
        request.myuser_info.nickname = json_obj["nickname"]
        request.myuser_info.save()
        return JsonResponse({"code": "2000", "nickname": json_obj["nickname"], "phone": json_obj["phone"]})



# django.http.multipartparser.MultiPartParserError: Invalid boundary in multipart:None
