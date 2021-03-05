from django.contrib import admin

# Register your models here.
from .models import *


# class NovelManage(admin.ModelAdmin):
#     list_display = ['id', 'name', 'number']
#     list_display_links = ['id', 'name', 'number']
#     list_filter = ['number']
#
#
# admin.site.register(Novel, NovelManage)
#
#
# class NovelTagManage(admin.ModelAdmin):
#     list_display = ['id', 'tag']
#     list_display_links = ['id', 'tag']
#     list_filter = ['tag']

    # def number(self, obj):
    #     novel_num = obj.tag.number
    #     return novel_num


# admin.site.register(NovelTag, NovelTagManage)
#
#
# class NumToTagManage(admin.ModelAdmin):
#     list_display = ['id', 'tags', 'num']
#
# admin.site.register(NumToTag, NumToTagManage)

# class NovelMessageManage(admin.ModelAdmin):
#     list_display = ['id', 'author', 'up', 'introduce', 'serialize', 'vip_type', 'cover', 'novel_num']
#     list_display_links = ['id', 'author', 'up', 'introduce', 'serialize', 'vip_type', 'cover', 'novel_num']
#     list_filter = ['author', 'up', 'vip_type', 'novel_num']
#     search_fields = ['author', 'vip_type']
#
#
# admin.site.register(NovelMessage, NovelMessageManage)
# class ChapterManage(admin.ModelAdmin):
#     list_display = ['id', 'chapter', 'content', 'topic']
#
# admin.site.register(Chapter,ChapterManage)