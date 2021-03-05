from django.db import models
import random
from ranks.models import *

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
# class User(models.Model):
#     mail = models.CharField('邮箱', max_length=50)
#     number = models.ManyToManyField(verbose_name='num1', to='Novel', through='UserToSc', through_fields=('user', 'number'))
#     def __str__(self):
#         return self.mail
#
# class UserToSc(models.Model):
#     user = models.ForeignKey(to='User', on_delete=models.CASCADE)
#     number = models.ForeignKey(to='Novel', on_delete=models.CASCADE)
#
#
# class Novel(models.Model):
#     name = models.CharField('名称', max_length=20)
#     number = models.IntegerField('编号', default=num)
#     tag = models.ManyToManyField(to='NovelTag', through='NumToTag', through_fields=('num', 'tags'))
#     mail = models.ManyToManyField(to='User', through='UserToSc', through_fields=('number', 'user'))
#     # sc = models.ForeignKey(Sc, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return str(self.number)
#
#
# class NovelTag(models.Model):
#     tag = models.CharField('标签', max_length=60)
#     number = models.ManyToManyField(verbose_name='num', to='Novel', through='NumToTag', through_fields=('tags', 'num'))
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
#         ordering = ['-up']
#
#
# class Chapter(models.Model):
#     chapter  = models.CharField('小说章节', max_length=100)
#     content = models.TextField('单章内容')
#     #一对多外键
#     topic = models.ForeignKey(Novel, on_delete=models.CASCADE)
