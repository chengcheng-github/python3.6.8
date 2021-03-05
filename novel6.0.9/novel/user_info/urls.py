from django.urls import path
from user_info import views

urlpatterns = [
    path("<str:username>", views.User_Info.as_view()),
    path("<str:username>/change", views.User_Info_Change.as_view()),
    path("<str:username>/change/avatar", views.User_Info_Change_Avatar.as_view()),
    path("<str:username>/change/user_info",views.Change_User_Info.as_view()),
]
