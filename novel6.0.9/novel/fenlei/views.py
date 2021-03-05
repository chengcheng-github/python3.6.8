from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
# Create your views here.
import pymysql
from django.conf import settings


class FenleiView(View):

    def get(self, request,url=''):#tag1=0&tag2=5&tag3=2
        # print(tag1,tag2,tag3)
        self.db = pymysql.connect('127.0.0.1', 'root', '123456', 'noveldb', charset='utf8')
        self.cur = self.db.cursor()
        if url=='':
            self.cur.execute('select id from ranks_novelmessage;')
            tuple_bid = self.cur.fetchall()
        else:
            tag1 = url.split('tag1=')[1].split('&')[0]
            # tag2 = url.split('tag2=')[1].split('&')[0]
            # tag3 = url.split('tag3=')[1].split('&')[0]
            if tag1 != '0':
                self.cur.execute('select num_id from ranks_numtotag where tags_id=%s;', tag1)
                tuple_bid = self.cur.fetchall()
            else:
                self.cur.execute('select id from ranks_novelmessage;')
                tuple_bid = self.cur.fetchall()
        list_bk = []
        for bid in tuple_bid:
            dict_bk = {}
            if url == '':
                self.cur.execute('select * from ranks_novelmessage where id=%s', bid[0])
                tuple_bk = self.cur.fetchall()
            else:
                tag3 = url.split('tag3=')[1]
                if tag3 == '0':
                    self.cur.execute('select * from ranks_novelmessage where id=%s', bid[0])
                    tuple_bk = self.cur.fetchall()
                elif tag3 == '1':
                    self.cur.execute('select * from ranks_novelmessage where id=%s and serialize=1;', bid[0])
                    tuple_bk = self.cur.fetchall()
                else:
                    self.cur.execute('select * from ranks_novelmessage where id=%s and serialize=0;', bid[0])
                    tuple_bk = self.cur.fetchall()
            if len(tuple_bk):
                print(tuple_bk)
                self.cur.execute('select * from ranks_novel where id=%s;', bid[0])
                dict_bk['bname'] = self.cur.fetchall()[0][1]

                dict_bk['book_id'] = bid[0]
                print(dict_bk['book_id'])
                dict_bk['author'] = tuple_bk[0][1]
                dict_bk['introduce'] = tuple_bk[0][2]
                dict_bk['cover'] = tuple_bk[0][6]
                # print(dict_bk['cover'])
                list_bk.append(dict_bk)
            else:
                continue



        # ins = 'select * from ranks_novelmessage;'
        # self.cur.execute(ins)
        # tuple_book = self.cur.fetchall()
        # self.db.commit()
        # list_book = []
        # for b in tuple_book:
        #     dict_book = {}
        #     self.cur.execute('select * from ranks_novel where id=%s;',b[0])
        #     dict_book['bname'] = self.cur.fetchall()[0][1]
        #     dict_book['author'] = b[1]
        #     dict_book['introduce'] = b[2]
        #     dict_book['cover'] = b[6]
        #     list_book.append(dict_book)
        res = {'code': 200, 'data': list_bk, 'base_url': settings.PIC_URL}
        return JsonResponse(res)
