# from django.contrib import admin
#
# # Register your models here.
# from novel1 import models
#
# from register_and_login import models as r_m
#
# class NovelManager(admin.ModelAdmin):
#     list_display = ["id", "name"]
#
#
# admin.site.register(models.Novel, NovelManager)
#
#
# class NovelTagManager(admin.ModelAdmin):
#     list_display = ["id", "tag", "novel_name"]
#
#     def novel_name(self, obj):
#         novel_name = []
#         for item in obj.novel.all():
#             # 就是这样,用id就返回id列表,用name就返回name列表
#             print("123")
#             novel_name.append(item.name)
#             pass
#         return novel_name
#
#
# admin.site.register(models.NovelTag, NovelTagManager)
#
#
# class NovelMessageManager(admin.ModelAdmin):
#     list_display = ["id", "author", "introduce", "up",
#                     "serialize", "vip_type", "cover", "novel"]
#
#
# admin.site.register(models.NovelMessage, NovelMessageManager)
#
#
# class NovelSectionsManager(admin.ModelAdmin):
#     list_display = ["id", "title", "content_id", "novel"]
#
#     # 多对多里的函数放在这里报错,提示novel在这里没有all()方法
#     # 下面的函数会直接把所有书名返回到novel_name这栏里,所有的书名都会在里面,数据显示的不对
#     # def novel_name(self, obj):
#     #     novel_name = []
#     #     for item in models.Novel.objects.all():
#     #         # 就是这样,用id就返回id列表,用name就返回name列表
#     #         novel_name.append(item.name)
#     #         pass
#     #     return novel_name
#
#
# admin.site.register(models.NovelSections, NovelSectionsManager)
#
#
# class NovelContentManager(admin.ModelAdmin):
#     list_display = ["id", "content", "novelsections", "novel_name"]
#
#     def novel_name(self, obj):
#         novel_name = obj.novelsections.novel.name
#         return novel_name
#
#
# admin.site.register(models.NovelContent, NovelContentManager)
# # class User_infoManager(admin.ModelAdmin):
# #     list_display = ["mail", "avatar", "nickname", "collection", "user_type",
# #                     "created_time", "updated_time", "phone", "user_vip", "user_vip_time"]
#
#
# # admin.site.register(models.User_info, User_infoManager)
#
# class ShoucangManager(admin.ModelAdmin):
#
#     list_display = ["id","user", "novel_name"]
#
#     def novel_name(self, obj):
#         novel_name = []
#         for item in obj.novel.all():
#             # 就是这样,用id就返回id列表,用name就返回name列表
#             novel_name.append(item.name)
#             pass
#         return novel_name
#
#
#
# admin.site.register(models.Shoucang, ShoucangManager)