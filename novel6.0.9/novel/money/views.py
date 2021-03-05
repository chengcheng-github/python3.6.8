from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse
from django.http import HttpResponse
from register_and_login import models
from django.utils.decorators import method_decorator
from django.conf import settings
from alipay import AliPay
import json
import jwt
import time
import datetime
# Create your views here.

app_private_key_string = open(
    settings.ALIPAY_KEY_DIR+"app_private_key.pem").read()
alipay_public_key_string = open(
    settings.ALIPAY_KEY_DIR+"alipay_public_key.pem").read()


class MyAliPay(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.alipay = AliPay(
            appid=settings.ALIPAY_APP_ID,
            app_notify_url=settings.ALIPAY_NOTIFY_URL,
            app_private_key_string=app_private_key_string,
            alipay_public_key_string=alipay_public_key_string,
            sign_type="RSA2",
            debug=True,
        )

    def get_trade_url(self, order_id, subject1, amount):
        base_url = "https://openapi.alipaydev.com/gateway.do"
        order_string = self.alipay.api_alipay_trade_page_pay(
            out_trade_no=order_id,
            total_amount=amount,
            subject=subject1,
            return_url=settings.ALIPAY_RETURN_URL,
            notify_url=settings.ALIPAY_NOTIFY_URL,


        )
        return base_url+"?"+order_string


class Money(MyAliPay):
    def post(self, request):
        json_obj = json.loads(request.body.decode())
        print("充值功能!!")
        print(json_obj)
        print()
        pay_url = self.get_trade_url(
            json_obj["order_no"], json_obj["subject1"], json_obj["amount"])
        return JsonResponse({"pay_url": pay_url})



class Get_Money(MyAliPay):
    def get(self, request):
        print("进入充值结算:")
        print(request.GET.keys())
        print()
        try:
            pay_result = self.alipay.api_alipay_trade_query(
                # out_trade_no是我自己设置的订单编号,由用户邮箱和时间(年月日时分秒组成)
                out_trade_no=request.GET.get("out_trade_no"))
            print(pay_result)
            print()
            print("显示主动查询支付结果:", pay_result["trade_status"])
            # 如果查询某个订单编号显示支付成功
            if pay_result["trade_status"] == "TRADE_SUCCESS":
                # 先把充值的用户邮箱找出来
                mail1 = request.GET.get("out_trade_no").split(".com")[0]+".com"
                print("充值账户邮箱:", mail1)
                print("充值时间:", pay_result["send_pay_date"])
                money_time1 = time.strptime(
                    pay_result["send_pay_date"], "%Y-%m-%d %H:%M:%S")
                # 以秒为单位的时间戳,类型是字符串
                money_time1 = time.mktime(money_time1)
                print("vip生效时间:",money_time1)
                # 过期时间开始是时间戳
                # 用日期对象datetime.datetime好像最少得开一天vip才行
                # 要不把vip时长直接用用int来存时间戳?那可省事多了
                # 不过消除vip功能目前正常运行
                money_time2 = money_time1+3600*24*30
                print("vip到期时间:",money_time2)
                # 然后从时间戳转化为datetime.datetime对象
                # 这里datetime.datetime.fromtimestamp()
                money_time2 = datetime.datetime.fromtimestamp(money_time2)
                print("vip到期日期对象",money_time2)
                user_info1 = models.User_info.objects.get(mail=mail1)
                print(user_info1.__dict__)
                # 修改vip状态为1
                user_info1.user_vip = "1"
                # 每次启动后端服务,第一次运行到这里时会有一个warning提示时区异常(mysql和django的时区好像不同),第二次开始就没有这个warning了
                user_info1.user_vip_time = money_time2
                # 记得保存
                # 然后修改login_check,查找个人信息那里也要修改,每次登录时或者被查找时检测这个用户的vip状态,如果为1就继续判断其vip过期时间,将时间转化为时间戳,如果现在时间的时间戳比vip过期时间大,将vip状态改为"",vip过期时间改为None
                user_info1.save()
            print()
        except Exception as e:
            print("充值结算请求异常:")
            print(e)
            print()
        return render(request, "get_money.html")

    def post(self, request):
        print(request.POST.keys())
        return HttpResponse("success")
