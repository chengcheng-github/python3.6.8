from django.urls import path

from money import views

urlpatterns = [
    # 分布式路由
    path("money", views.Money.as_view()),
    path("get_money",views.Get_Money.as_view()),
]
