# 用点在pycharm里直接执行报错
from register_and_login import views
# 用下一行在vscode里没法用这个包里的自动补全
# from register_and_login import views
from django.urls import path
# 想用智能补全的话也许可以用import sys 来手动添加.py模块
# 像下面这样
import sys

# sys.path.append("../houduan/urls.py")

urlpatterns = [
    # 注册功能
    path("register", views.Register.as_view()),
    # 发送验证码到电子邮件功能
    path("sendmail", views.Sendmail.as_view()),
    path("login", views.Login.as_view()),
]
