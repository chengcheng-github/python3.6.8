import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from ranks.models import *


class TopicView(View):
    def get(self,request,book_id):
        print('----------topic get view in--------')
        result = {'code': 200, 'data': {}}
        # book_id = request.GET.get('bid')
        # print('-----------',book_id,'-------')
        # book_id = request.GET.get('book_id')
        #一本书的名字
        # book_id = 1
        books = Novel.objects.get(id=book_id)
        print('------11111',books)
        print(books.name)
        print(books.id)
        print(book_id)
        # boo =books.id
        bookall =NovelMessage.objects.filter(novel_num_id=books.id)
        print(bookall)
        for book in bookall:
            result['data']['author'] = book.author
            print(book.author)
            result['data']['introduce'] = book.introduce

            result['data']['cover'] = str(book.cover)

        # 所有章节集合
        chapters = Chapter.objects.filter(topic=books.id)
        print(chapters)
        list_chapter = []
        # list_chapter_id = {}
        for cha in chapters:
            dict_chapter = {}
            print('------xxxxxx',cha.chapter)
            # list_chapter_id.append(cha.id)
            # list_chapter.append(cha.chapter)
            dict_chapter['id'] = cha.id  #章节id
            list_chapter.append(dict_chapter)
            dict_chapter['chapter'] = cha.chapter




        print('-----aaaaa',list_chapter)
        result['data']['name'] = books.name

        # for book in bookall:
        #     result['data']['author'] = book.author
        #     # result['data']['tag'] = books.tag
        #     result['data']['introduce'] = book.introduce
        #     result['data']['cover'] = str(book.cover)
        result['data']['chapters'] = list_chapter
        max_id = max(list_chapter[len(list_chapter) - 1])
        print('------dadddddd', max_id)
            # result['data']['chapters'] = cha.chapter
            # result['data']['zhangjie'] = list01
        return JsonResponse(result)





#内容详情页　　待完善
class ConView(View):
    def get(self, request,):
        # print('--------------cccc----')
        con = request.GET.get('cid')
        # print(con)
        # # con = 1
        contents = Chapter.objects.get(id=con)
        # contents.content
        print(contents.content)
        # result = {'code':202}
        result = {'code': 200, 'data': {}}
        result['data']['content'] = contents.content
        result['data']['chapter'] = contents.chapter
        return JsonResponse(result)

        # 得到名称
        # cha = request.GET.get('cid')
        # print('--------',cha)
        # contents = Chapter.objects.get(chapter=cha)
        # result = {'code': 202, 'data': {}}
        # result['data']['content'] = contents.content
        # return JsonResponse(result)



# def get_neirong(zhangjies):
#     print('------内容函数开始------')
#     list02 = []
#     for zj in zhangjies:
#         # print(zj.chapter)
#         # list02['cha1'] = zj.content
#         # list02['cha2'] = zj.content
#         # print(zj.content)
#         list02.append(zj.content)
#     print(list02)
#     return list02
#
# def con(request):
#     function1 = get_neirong
#     return render(request,'content.html',locals())