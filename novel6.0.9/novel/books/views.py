from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator

from  tools.login import login_check
from django.http import JsonResponse
from django.views import View
from .models import *
from django.conf import settings

from django.db import models

import random
import hashlib


class BooksView(View):
    # 处理 v1/users的 GET 请求
    # @method_decorator(login_check)
    def get(self, request, mail):
        print('------------get请求成功------------')
        print(mail)
        # try:
        novel_info = []
        #用户ｉｄ
        user_id = User.objects.filter(mail=mail).values('id')
        # except:
        #     result = {'code':10035,'error':'用户名错误'}
        #     return JsonResponse(result)

        print('user_id>>>>',user_id)
        u_id = user_id[0]['id']
        #获取用户的ｉｄ
        print('u_id>>>>>>',u_id)
        #获取关联表ｉｄ
        novel_id = UserToSc.objects.filter(user_id=u_id).values("id")
        print('novel_id>>>>>>>>>>>>>>>>>kkkkkkkkkk', novel_id)
        for uts_id in novel_id:
            nov_message = {}
            n_id=uts_id['id']
            print('nov_id>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',n_id)

            number_id = UserToSc.objects.filter(id=n_id).values("number_id")
            print('number_id>>>>>>>>>>>>>>>>>>>>>>',number_id)
            name_id = number_id[0]['number_id']
            print('name_id>>>>>>',name_id)
            novel_name=Novel.objects.filter(id=name_id).values('name')
            print('novel_name>>>>>>', novel_name)
            nov_message['name']=novel_name[0]['name']
            print(nov_message['name'])
            author=NovelMessage.objects.filter(id=name_id).values('author')
            nov_message['author']=author[0]['author']
            print(author[0]['author'])
            introduce=NovelMessage.objects.filter(id=name_id).values('introduce')
            nov_message['introduce']=introduce[0]['introduce']
            print(introduce[0]['introduce'])
            up = NovelMessage.objects.filter(id=name_id).values('up')
            nov_message['up'] = up[0]['up']
            print(up[0]['up'])
            serialize = NovelMessage.objects.filter(id=name_id).values('serialize')
            # nov_message['serialize'] = serialize[0]['serialize']
            if serialize[0]['serialize'] == 1:
                nov_message['serialize'] = '有更新'
            else:
                nov_message['serialize']= '无更新'



            # print(serialize[0]['serialize'])


            # vip_type = NovelMessage.objects.filter(id=name_id).values('vip_type')
            # nov_message['vip_type'] = up[0]['vip_type']
            # print(vip_type[0]['vip_type'])
            novel_info.append(nov_message)

        result = {'code': 200, 'data': novel_info}
        return JsonResponse(result)


















