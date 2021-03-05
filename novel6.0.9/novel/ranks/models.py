from django.db import models
import random


# Create your models here.

def num():
    number = set()
    number.add(random.randint(10000, 99999))
    res = list(number)
    return res[0]


def up_num():
    number = set()
    number.add(random.randint(1000, 9999))
    res = list(number)
    return res[0]


class User(models.Model):
    mail = models.CharField('邮箱', max_length=50)
    password = models.CharField('密码', max_length=32,null=True)
    number = models.ManyToManyField(verbose_name='num1', to='Novel', through='UserToSc', through_fields=('user', 'number'))
    def __str__(self):
        return self.mail

class User_info(models.Model):
    # 用户信息id省略不写(主键自增)
    # 级联删除,一对一,删除主表时,从表对应内容删除
    # 用户信息关联用户
    mail = models.OneToOneField(User, on_delete=models.CASCADE)
    # 头像,上传到后端根目录/media/avatar这个目录里
    avatar = models.ImageField(upload_to="avatar", null=True)
    # 用户名
    nickname = models.CharField("用户名", max_length=5)
    # 收藏 字符串 "1,2,3,4,"->这些是小说的id
    collection = models.CharField("收藏", max_length=100, default="")
    # 用户类型 2普通用户(默认),3管理员, 封号不能做一个用户类型,封号单独做个表,表的内容是封号id(主键自增),封号账户(用户表邮箱)和封号截止日期
    user_type = models.CharField("用户类型", max_length=100, default="2")
    # 创建时间
    created_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    updated_time = models.DateTimeField(auto_now=True)
    # 手机号
    phone = models.CharField("手机号", max_length=11, default="")
    # vip状态 默认为"" ,充钱当vip之后就是1
    user_vip = models.CharField("vip状态", max_length=20, default="")
    # 创建时为空,充值以后把vip状态改成1,vip过期时间改成充值那天的31天后
    user_vip_time = models.DateTimeField(null=True)



class UserToSc(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    number = models.ForeignKey(to='Novel', on_delete=models.CASCADE)


class Novel(models.Model):
    name = models.CharField('名称', max_length=20)
    number = models.IntegerField('编号', default=num)
    tag = models.ManyToManyField(to='NovelTag', through='NumToTag', through_fields=('num', 'tags'))
    mail = models.ManyToManyField(to='User', through='UserToSc', through_fields=('number', 'user'))
    # sc = models.ForeignKey(Sc, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)


class NovelTag(models.Model):
    tag = models.CharField('标签', max_length=60)
    number = models.ManyToManyField(verbose_name='num', to='Novel', through='NumToTag', through_fields=('tags', 'num'))

    def __str__(self):
        return self.tag


class NumToTag(models.Model):
    tags = models.ForeignKey(to='NovelTag', on_delete=models.CASCADE)
    num = models.ForeignKey(to='Novel', on_delete=models.CASCADE)


class NovelMessage(models.Model):
    author = models.CharField('作者', max_length=30)
    introduce = models.CharField('介绍', max_length=999)
    up = models.IntegerField('点赞', default=up_num)
    serialize = models.BooleanField('连载状态', default=1)
    vip_type = models.BooleanField('VIP可阅读', default=0)
    cover = models.ImageField('封面', upload_to='cover', null=True)
    novel_num = models.OneToOneField(Novel, on_delete=models.CASCADE, verbose_name='小说编号')

    class Meta:
        ordering = ['-up']


class Chapter(models.Model):
    chapter = models.CharField('小说章节', max_length=100)
    content = models.TextField('单章内容')
    # 一对多外键
    topic = models.ForeignKey(Novel, on_delete=models.CASCADE)

