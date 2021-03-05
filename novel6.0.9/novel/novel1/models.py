from django.db import models

# Create your models here.
import random

from register_and_login import models as r_m
from ranks.models import *

# Create your models here.
#
# # 小说表
# class Novel(models.Model):
#     name = models.CharField('名称', max_length=20)
#
#     def __str__(self):
#         return self.name
#
#
# # 标签表,与小说多对多关系(可以最后再处理?)
# class NovelTag(models.Model):
#     tag = models.CharField('标签', max_length=60)
#     novel = models.ManyToManyField(Novel)
#
#     # def __str__(self):
#     # return self.tag
#
#
# # 小说详情表,与小说一对一
# class NovelMessage(models.Model):
#     author = models.CharField('作者', max_length=30)
#     introduce = models.CharField('介绍', max_length=999)
#     up = models.IntegerField('点赞', default=random.randint(1, 999))
#     # 1连载中,其他,已完结
#     serialize = models.BooleanField('连载状态', default=True)
#     # 0代表不需要vip就能阅读
#     vip_type = models.BooleanField('vip可阅读', default=False)
#     cover = models.ImageField('封面', upload_to='cover')
#     # 对应小说
#     novel = models.OneToOneField(Novel, on_delete=models.PROTECT)
#
#
# # 章节表,与小说是一对多关系
# class NovelSections(models.Model):
#     title = models.CharField('章节标题', max_length=60)
#     # 这里是一个数字,对应的内容是 内容表的id
#     content_id = models.IntegerField('对应小说章节数')
#     # 对应小说
#     novel = models.ForeignKey(Novel, on_delete=models.PROTECT)
#
#     def __str__(self):
#         return self.title
#
#
# # 内容表,与章节表一对一对应
# class NovelContent(models.Model):
#     content = models.TextField('内容')
#     # 对应章节
#     novelsections = models.OneToOneField(
#         NovelSections, on_delete=models.CASCADE)
#
# # 收藏
# class Shoucang(models.Model):
#     user=models.ForeignKey(r_m.User,on_delete=models.PROTECT)
#     novel=models.ManyToManyField(Novel)