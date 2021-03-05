from django.shortcuts import render

# Create your views here.
import random
import hashlib
import json
import time
# 下一行存在多个同名包,需要的是pyjwt这个包
import jwt
from django.conf import settings
from django.views import View
from django.core import mail
from django.core.cache import cache
from django.http import HttpResponse
from django.http.response import JsonResponse
from register_and_login import models as r_models
from novel1 import models as n_models


class Show_Novels(View):
    def post(self, request):
        print("客户端首页从后端获取书的数据:")
        print("正常运行")
        # 这个集合也是一个类里的对象
        # print(n_models.Novel.objects.all(),"数据类型:",type(n_models.Novel.objects.all()))
        # 这里获取到的是orm里的对象(具体的书)
        # print(n_models.Novel.objects.all()[0])
        # 可以直接取id
        # print(n_models.Novel.objects.all()[0].id)
        # 用字典把书名和id都传递到前端
        res = {}
        for item in n_models.Novel.objects.all():
            res[item.name] = item.id
            # print(item.name, item.id)
            pass
        print(res)
        print()
        return JsonResponse(res)
        pass


class Novel_Index(View):
    def post(self, request):
        print("客户端获取一本书的目录:")
        json_obj = json.loads(request.body.decode())
        # print(json_obj)
        try:
            book = n_models.Novel.objects.get(id=json_obj["novel_id"])
        except Exception as e:
            print("获取书籍功能异常:")
            print(e)
            print("没查到id为", json_obj["novel_id"], "的书")
            result = {"code": "1001", "error": "没查到这本书"}
            print()
            return JsonResponse(result)
        book_message = n_models.NovelMessage.objects.get(novel=book)
        book_sections = n_models.NovelSections.objects.filter(
            novel=book).order_by("content_id")
        res = {}
        for item in book_sections:
            res[item.content_id] = item.title
        print("看看目录结果")
        print(res)
        # print(book_sections)
        print("正常运行")
        print()
        return JsonResponse({"code": "2000", "book": book.name, "author": book_message.author, "introduce": book_message.introduce, "up": book_message.up, "serialize": book_message.serialize, "vip_type": book_message.vip_type, "cover": str(book_message.cover), "data": res})
        pass


class Read_Novel(View):
    def post(self, request):
        print("进入阅读小说功能:")
        json_obj = json.loads(request.body.decode())
        print("看看前端发的什么东西")
        print(json_obj)
        # 先找找有没有这本小说
        try:
            book = n_models.Novel.objects.get(id=json_obj["novel_id"])
        except Exception as e:
            print("获取书籍异常:")
            print(e)
            print("没查到id为", json_obj["novel_id"], "的书")
            result = {"code": "1001", "error": "没查到这本书"}
            print()
            return JsonResponse(result)
        # 如果有,看看小说的详情
        book_message = n_models.NovelMessage.objects.get(novel=book)
        # 如果小说是vip才能看的,那就校验token检查用户是不是vip
        if book_message.vip_type == True:
            # 先解token看看是不是合法用户
            try:
                payload = jwt.decode(
                    json_obj["token"], settings.JWT_TOKEN_KEY, algorithms="HS256")
            except Exception as e:
                print("验证登录状态功能:token校验异常")
                print("异常:", e)
                result = {"code": 403, "error": "请登录"}
                print("校验结束,验证登录状态结束,返回出现异常的json到前端")
                return JsonResponse(result)
            mail = payload["mail"]
            user = r_models.User.objects.get(mail=mail)
            user_info = r_models.User_info.objects.get(mail=mail)
            if user_info.user_vip != "1":
                result = {"code": "888", "error": "不是vip,赶紧充值"}
                print("不是vip,得赶紧充值")
                return JsonResponse(result)
        # 如果是vip,或者这书不需要vip也给看,那就找有没有对应章节
        try:
            content_id = n_models.NovelSections.objects.get(
                novel=book, content_id=json_obj["content_id"])
        except Exception as e:
            print("获取书籍目录异常:")
            print(e)
            print("没查到id为", json_obj["content_id"], "的书")
            result = {"code": "1002", "error": "没查到这本书的第" +
                      json_obj["content_id"]+"章"}
            print()
            return JsonResponse(result)
        # 找到对应章节了,就找对应内容
        content = n_models.NovelContent.objects.get(novelsections=content_id)
        # 看看内容
        print(content.content)
        print("正常运行")
        return JsonResponse({"code": "2000", "title": content_id.title, "content": content.content})
        pass


class Shoucang(View):
    def get(self,request):
        shoucang1=n_models.Shoucang.objects.get(id=1)
        shoucang1=shoucang1.novel.all()
        res_code=""
        for item in shoucang1:
            res_code=res_code+item.name+"<br>\n"
        if "没有收藏时只添加这个" in res_code:
            res_code="没有收藏"
        return HttpResponse(res_code)
        pass