from django.contrib import admin

from django.core.cache import caches
RANKS_CACHES = caches['ranks']

# Register your models here.
from .models import *


class BaseModel(admin.ModelAdmin):
    """
    继承admin.ModelAdmin
    重写save_model / delete_model 方法
    """

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # 删除首页缓存
        RANKS_CACHES.clear()
        print("保存数据时，首页缓存删除")

    def delete_model(self, request, obj):
        super().delete_model(request, obj)
        # 删除首页缓存
        RANKS_CACHES.clear()
        print("删除数据时，首页缓存删除")

@admin.register(User)
class UserManage(BaseModel):
    list_display = ['id', 'mail']


@admin.register(User_info)
class User_infoManager(BaseModel):
    list_display = ["mail", "avatar", "nickname", "collection", "user_type",
                    "created_time", "updated_time", "phone", "user_vip", "user_vip_time"]



@admin.register(UserToSc)
class UserToScManage(BaseModel):
    list_display = ['id', 'user', 'number']
    list_display_links = ['id', 'user', 'number']

@admin.register(Novel)
class NovelManage(BaseModel):
    list_display = ['id', 'name', 'number']
    list_display_links = ['id', 'name', 'number']
    list_filter = ['number']


# admin.site.register(Novel, NovelManage)

@admin.register(NovelTag)
class NovelTagManage(BaseModel):
    list_display = ['id', 'tag']
    list_display_links = ['id', 'tag']
    list_filter = ['tag']

    # def number(self, obj):
    #     novel_num = obj.tag.number
    #     return novel_num


# admin.site.register(NovelTag, NovelTagManage)

@admin.register(NumToTag)
class NumToTagManage(BaseModel):
    list_display = ['id', 'tags', 'num']


# admin.site.register(NumToTag, NumToTagManage)

@admin.register(NovelMessage)
class NovelMessageManage(BaseModel):
    list_display = ['id', 'author', 'up', 'introduce', 'serialize', 'vip_type', 'cover', 'novel_num']
    list_display_links = ['id', 'author', 'up', 'introduce', 'serialize', 'vip_type', 'cover', 'novel_num']
    list_filter = ['author', 'up', 'vip_type', 'novel_num']
    search_fields = ['author', 'vip_type']

# admin.site.register(NovelMessage, NovelMessageManage)


@admin.register(Chapter)
class ChapterManage(BaseModel):
    list_display = ['id', 'chapter', 'content', 'topic']

