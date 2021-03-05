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
from django.shortcuts import render
from register_and_login import models


# Create your views here.
# 制作token,有效期一天
def make_token(mail1, expire=3600 * 24):
    payload = {"mail": mail1, "exp": time.time() + expire}
    return jwt.encode(payload, settings.JWT_TOKEN_KEY, algorithm="HS256")
    pass


# 注册功能
class Register(View):
    def post(self, request):
        # 前端发给后端的内容需要.decode()转换成字符串,然后操作
        # print("后端显示前端发送的内容:", request.body.decode())
        # json.loads(request.body.decode())
        print("注册功能:后端显示前端发送的注册信息:")
        # print(json.loads(request.body.decode()))
        # 不能将字典一样同时遍历key和value,只能遍历键,用键取值
        # 字典其实也能遍历键用键取值
        for key in json.loads(request.body.decode()):
            print(key, ":", json.loads(request.body.decode())[key])
        # print()
        # print("全部")
        # 不用.body 无法获取内容,获取到的是请求的url
        # print(request)
        # print("body")
        # 我这里直接用body是字节串
        # print(request.body)
        # json对象
        json_obj = json.loads(request.body.decode())
        mail1 = json_obj["mail1"]
        # print(mail1)
        pwd1 = json_obj["pwd1"]
        # print(pwd1)
        pwd2 = json_obj["pwd2"]
        # print(pwd2)
        # 这个是验证码
        confirm2 = json_obj["confirm2"]
        # print(confirm2)
        # redis缓存键
        cache_key = "register_mail_%s" % (mail1)
        # 用键来获取生成的验证码
        # 如果没有获取到生成的验证码
        if not cache.get(cache_key):
            print("注册功能异常:从缓存中获取验证码失败")
            print()
            result = {"code": 10110, "error": "从缓存中获取验证码失败"}
            return JsonResponse(result)
        # 或者验证码与前端获取到用户输入的验证码不同
        # 这两种情况都不行,返回有问题的具体信息
        elif cache.get(cache_key) != confirm2:
            print("注册功能异常:验证码输入错误")
            print()
            result = {"code": 10111, "error": "验证码输入错误"}
            return JsonResponse(result)
        # 如果这两地方没问题,再看电子邮箱是否重复
        same_mail = models.User.objects.filter(mail=mail1)
        # 如果电子邮箱是重复的(前端获取的电子邮箱在数据库里查到了)
        if same_mail:
            result = {"code": 10112, "error": "邮箱已注册"}
            print("注册功能异常:邮箱已经注册过了")
            print()
            return JsonResponse(result)
        # 如果验证码,邮箱都没问题,那就判断一下输的两次密码是不是相同的
        if pwd1 != pwd2:
            result = {"code": 10113, "error": "两次输入的密码不同"}
            print("注册功能异常:两次输的密码不一样")
            print()
            return JsonResponse(result)
        if not pwd1 or not pwd2:
            result = {"code": 10114, "error": "密码没输入啊"}
            print("注册功能异常:没输入密码")
            print()
            return JsonResponse(result)
        # 不存在邮箱不输入的情况,不输入邮箱,过不了验证码
        # if not mail1:
        #     result = {"code": 10115, "error": "邮箱没输入啊"}
        #     print("注册功能异常:密码没输入啊")
        #     print()
        #     return JsonResponse(result)
        # 如果输入都没问题,那就把密码hash加密
        md5 = hashlib.md5()
        md5.update(pwd1.encode())
        pwd_hash = md5.hexdigest()
        # 用捕获异常来把数据插入数据库(因为有可能有人一起注册这个邮箱)
        try:
            user = models.User.objects.create(mail=mail1, password=pwd_hash)
            pass
        except Exception as e:
            result = {"code": 10114, "error": "邮箱已注册"}
            print("注册功能异常:邮箱已经注册过了")
            print(e)
            print()
            return result
            pass
        # token刚做好是字节串,需要.decode()转化为字符串
        # 学校用下一行
        # token = make_token(mail1).decode()
        # 家里用下一行
        # 将补习班python3安装的包的版本获取以后,将pyjwt的版本调整的与补习班的一致,于是token又需要.decode()变字符串了..
        token = make_token(mail1).decode()
        print("注册功能:显示一下制作好的token")
        print(token)
        # 用户表添加完以后,用户信息表也添加一下
        user_info = models.User_info.objects.create(mail=user, nickname="普通用户")
        result = {
            "code": 200,
            "mail": user_info.nickname,
            "user_mail":mail1,
            "data": {
                "token": token,
            },
        }
        print("注册功能正常运行!")
        print()
        # 用return JsonResponse(result)返回的内容如果前端用文本显示,
        # 是不能正常显示汉字的,需要发短句可以用return HttpResponse
        return JsonResponse(result)


class Sendmail(View):
    def post(self, request):
        print("获取注册邮件功能:后端显示前端发送的电子邮箱:")
        # json.loads(request.body.decode())["mail1"]
        print(json.loads(request.body.decode())["mail1"])
        # 因为发邮件只能用字符串,所以这里的验证码需要转换成字符串
        code1 = str(random.randint(1000, 9999))
        print("获取注册邮件功能:生成验证码", code1)
        # 发送邮件方法(导包)
        try:
            mail.send_mail(
                "项目网站注册验证码",  # 题目
                "验证码:" + code1 + ",5分钟以后失效",  # 消息内容
                "3127547189@qq.com",  # 发送者[当前配置邮箱]
                recipient_list=[json.loads(request.body.decode())[
                    "mail1"], ],  # 接收者邮件列表
            )
            # redis键值对 键:register_eail_403714067@qq.com 值:刚生成的验证码
            cache_key = "register_mail_%s" % (
                json.loads(request.body.decode())["mail1"])
            # 这个值在redis里的第0库里
            #         键          值    有效期,单位为秒
            cache.set(cache_key, code1, 300)
            # 捕获异常
        except Exception as e:
            # 显示异常
            print("获取注册邮件功能异常:")
            print(e)
            return HttpResponse("后端发送验证码失败,建议检查输入的电子邮箱")
        # 生成验证码,发送以后,把这个验证码保存到redis里,设置收到的邮箱为键,验证码为值.设置有效期300秒
        print("获取注册邮件功能正常运行!")
        print()
        return HttpResponse("后端发送验证码去电子邮箱了")


class Login(View):
    def post(self, request):
        json_obj = json.loads(request.body.decode())
        print(json_obj)
        mail = json_obj["mail1"]
        pwd = json_obj["pwd1"]
        print("登录功能:显示前端输入的内容")
        print(mail, pwd)
        try:
            user = models.User.objects.get(mail=mail)
        except Exception as e:
            print("登陆功能异常:没找到对应的邮箱")
            print(e)
            result = {"code": "10200", "error": "用户名或密码错误"}
            return JsonResponse(result)
        # 邮箱校验正常后
        md5 = hashlib.md5()
        md5.update(pwd.encode())
        pwd_h = md5.hexdigest()
        if user.password != pwd_h:
            print("登陆功能异常:密码与数据库存放的密码不同")
            result = {"code": "10200", "error": "用户名或密码错误"}
            return JsonResponse(result)
        # 邮箱和密码都正常,制作token发送到客户端浏览器
        print("登陆功能:正常运行")
        token = make_token(mail).decode()
        user_info = models.User_info.objects.get(mail=user)
        return JsonResponse({
            "code": "200",
            "my_site_1_user": user_info.nickname,
            "user_mail":mail,
            "data": {"token": token},
        })
        pass
