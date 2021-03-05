#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author JourWon
# @date 2021/2/13
# @file views.py
from django.http import JsonResponse

from django.views import View
import pymysql

class IndexView(View):
    def get(self,request):
        self.db = pymysql.connect('127.0.0.1', 'root', '123456', 'noveldb', charset='utf8')
        self.cur = self.db.cursor()
        self.cur.execute('select * from ranks_novelmessage;')
        tuple_all_bk = self.cur.fetchall()
        self.cur.execute('select * from ranks_novelmessage order by up limit 7;')
        tuple_rank_bk = self.cur.fetchall()

        list_bk1 = []
        list_bk2 = []

        for bk in tuple_all_bk:
            dict_bk = {}
            self.cur.execute('select * from ranks_novel where id=%s;', bk[0])
            dict_bk['bname'] = self.cur.fetchall()[0][1]
            dict_bk['author'] = bk[1]
            dict_bk['introduce'] = bk[2]
            dict_bk['cover'] = bk[6]
            list_bk1.append(dict_bk)

        for bk in tuple_rank_bk:
            dict_bk = {}
            self.cur.execute('select * from ranks_novel where id=%s;', bk[0])
            dict_bk['bname'] = self.cur.fetchall()[0][1]
            dict_bk['author'] = bk[1]
            dict_bk['introduce'] = bk[2]
            dict_bk['cover'] = bk[6]
            list_bk2.append(dict_bk)


        res = {'code': 200, 'data': (list_bk1,list_bk2)}
        return JsonResponse(res)
