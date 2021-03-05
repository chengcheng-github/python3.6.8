from django.urls import path

from novel1 import views

urlpatterns = [
    # 分布式路由
    # path("money", views.Money.as_view()),
    # path("get_money",views.Get_Money.as_view()),
    path("show_novels", views.Show_Novels.as_view()),
    path("novel_index", views.Novel_Index.as_view()),
    path("read_novel", views.Read_Novel.as_view()),
    path("shoucang", views.Shoucang.as_view()),
]
