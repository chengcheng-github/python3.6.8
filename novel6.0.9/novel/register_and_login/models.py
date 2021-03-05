from django.db import models
from ranks.models import *

# Create your models here.
# 用户表,暂定以下字段,剩下的个人信息,历史记录等用一对一连接
# 电子邮箱  varchar   20位长度   主键,唯一
# 密码     varchar   32位长度,hash加密
# 主表
# class User(models.Model):
#     # 主键
#     mail = models.CharField("电子邮箱", max_length=30, primary_key=True)
#     password = models.CharField("密码", max_length=32)

#
# class User_info(models.Model):
#     # 用户信息id省略不写(主键自增)
#     # 级联删除,一对一,删除主表时,从表对应内容删除
#     # 用户信息关联用户
#     mail = models.OneToOneField(User, on_delete=models.CASCADE)
#     # 头像,上传到后端根目录/media/avatar这个目录里
#     avatar = models.ImageField(upload_to="avatar", null=True)
#     # 用户名
#     nickname = models.CharField("用户名", max_length=5)
#     # 收藏 字符串 "1,2,3,4,"->这些是小说的id
#     collection = models.CharField("收藏", max_length=100, default="")
#     # 用户类型 2普通用户(默认),3管理员, 封号不能做一个用户类型,封号单独做个表,表的内容是封号id(主键自增),封号账户(用户表邮箱)和封号截止日期
#     user_type = models.CharField("用户类型", max_length=100, default="2")
#     # 创建时间
#     created_time = models.DateTimeField(auto_now_add=True)
#     # 更新时间
#     updated_time = models.DateTimeField(auto_now=True)
#     # 手机号
#     phone = models.CharField("手机号", max_length=11, default="")
#     # vip状态 默认为"" ,充钱当vip之后就是1
#     user_vip = models.CharField("vip状态", max_length=20, default="")
#     # 创建时为空,充值以后把vip状态改成1,vip过期时间改成充值那天的31天后
#     user_vip_time = models.DateTimeField(null=True)
#
#     pass
