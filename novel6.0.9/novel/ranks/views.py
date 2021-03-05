from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

from .models import NovelMessage, Novel, NovelTag
from django.views import View
from .models import *
from django.conf import settings


class NovelsIndexView(View):

    def get(self, request):
        # 按小说信息显示小说
        print('-----------------------novel-----------------------')
        novel_name = Novel.objects.all()
        novel_info = []
        novel_data = []
        for nov in novel_name:
            novel_dict = {}
            novel_dict['novel_id'] = nov.id
            novel_dict['novel_num'] = nov.number
            novel_dict['novel_name'] = nov.name
            print('novel_dict>>>11111', nov.number)
            Num_id = NumToTag.objects.filter(num_id=nov.id).values("id")
            print('NovelTag2Novel_id>>>2222222', Num_id)
            novel_dict['tag'] = []
            for i in Num_id:
                nid = i['id']
                tag_id = NumToTag.objects.filter(id=nid).values('tags_id')
                print('tag_id>>33333333', tag_id)
                tag = NovelTag.objects.filter(id=tag_id[0]['tags_id']).values('tag')
                print('tag>>>>>>>44444', tag)
                novel_dict['tag'].append(tag[0]['tag'])
            novel_message_id = NovelMessage.objects.filter(novel_num_id=nov.id).values("id")
            print('novel_message_id>>>>>5555555', novel_message_id)
            novel_messages_author = NovelMessage.objects.filter(id=novel_message_id[0]['id'], vip_type=0).values(
                "author")
            novel_messages_up = NovelMessage.objects.filter(id=novel_message_id[0]['id'], vip_type=0).values("up")
            novel_messages_cover = NovelMessage.objects.filter(id=novel_message_id[0]['id'], vip_type=0).values("cover")
            print('novel_dict>>>55555', novel_messages_author)
            print('novel_messages_up>>>55566666', novel_messages_up)
            novel_dict['author'] = novel_messages_author[0]['author']
            novel_dict['up'] = novel_messages_up[0]['up']
            novel_dict['cover'] = str(novel_messages_cover[0]['cover'])
            novel_data.append(novel_dict)
        print('novel_data>>>>6666666', novel_data)
        novel_rank0 = sorted(novel_data, key=lambda obj: obj['up'], reverse=True)
        novel_info.append(novel_rank0)
        novel_rank1 = sorted(novel_data, key=lambda obj: obj['novel_name'], reverse=True)
        novel_info.append(novel_rank1)
        novel_rank2 = sorted(novel_data, key=lambda obj: obj['novel_name'])
        novel_info.append(novel_rank2)
        novel_rank3 = sorted(novel_data, key=lambda obj: obj['novel_num'], reverse=True)
        novel_info.append(novel_rank3)
        novel_rank4 = sorted(novel_data, key=lambda obj: obj['novel_num'])
        novel_info.append(novel_rank4)
        novel_rank5 = sorted(novel_data, key=lambda obj: obj['novel_id'], reverse=True)
        novel_info.append(novel_rank5)
        print('sort_up>>>>>>>>8888888', novel_info)
        result = {'code': 200, 'data': novel_info, 'base_url': settings.PIC_URL}
        print('result>>>66666')
        return JsonResponse(result)
