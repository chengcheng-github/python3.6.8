from django.db import models

# Create your models here.

# class Topic(models.Model):
#     name = models.CharField('名称', max_length=50)
#     author = models.CharField('作者', max_length=50)
#     tag = models.CharField('标签', max_length=50)
#     introduce = models.CharField('简介', max_length=100)
#     imgdir = models.CharField('图片路径', max_length=50)
#     chapters = models.CharField('总章数', max_length=50)
#     def __str__(self):
#         return '小说' + self.name
from django.db import models
# import random


# Create your models here.

# def num():
#     number = set()
#     number.add(random.randint(10000, 99999))
#     res = list(number)
#     return res[0]
#
#
# def up_num():
#     number = set()
#     number.add(random.randint(1000, 9999))
#     res = list(number)
#     return res[0]
#
#
# class Novel(models.Model):
#     name = models.CharField('名称', max_length=20)
#     number = models.IntegerField('编号', default=num)
#     tag = models.ManyToManyField(to='NovelTag', through='NumToTag', through_fields=('num', 'tags'))
#
#     def __str__(self):
#         return str(self.number)
#
#
# class NovelTag(models.Model):
#     tag = models.CharField('标签', max_length=60)
#     number = models.ManyToManyField(verbose_name='num',to='Novel', through='NumToTag', through_fields=('tags', 'num'))
#
#     def __str__(self):
#         return self.tag
#
#
# class NumToTag(models.Model):
#     tags = models.ForeignKey(to='NovelTag', on_delete=models.CASCADE)
#     num = models.ForeignKey(to='Novel', on_delete=models.CASCADE)
#
#
# class NovelMessage(models.Model):
#     author = models.CharField('作者', max_length=30)
#     introduce = models.CharField('介绍', max_length=999)
#     up = models.IntegerField('点赞', default=up_num)
#     serialize = models.BooleanField('连载状态', default=1)
#     vip_type = models.BooleanField('VIP可阅读', default=0)
#     cover = models.ImageField('封面', upload_to='cover', null=True)
#     novel_num = models.OneToOneField(Novel, on_delete=models.CASCADE, verbose_name='小说编号')
#
#     class Meta:
#         ordering = ['up']

# 测试请求成功　整合　添加　优化
from ranks.models import *

# class Chapter(models.Model):
#     chapter  = models.CharField('小说章节', max_length=100)
#     content = models.TextField('单章内容')
#     #一对多外键
#     topic = models.ForeignKey(Novel, on_delete=models.CASCADE)
#