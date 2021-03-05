# 用点在pycharm里直接执行报错
from show_index_after_login import views
# 用下一行在vscode里没法用这个包里的自动补全
# from register_and_login import views
from django.urls import path
# 想用智能补全的话也许可以用import sys 来手动添加.py模块
# 像下面这样
import sys
# 不行,下面这么写也没用
# sys.path.append("../houduan/urls.py")

urlpatterns = [
    # 显示登陆以后的首页,如果校验token异常则返回异常码,前端接受到异常码以后改变url进入登陆之前的首页
    path("show_index_after_login", views.Show_Index_After_Login.as_view()),
]
