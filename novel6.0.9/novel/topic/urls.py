from django.urls import path
from . import views

urlpatterns = [
    #127.0.0.1:8000/content/<book_id>
    path('<int:book_id>',views.TopicView.as_view()),
    # path('con_id',views.ConView.as_view()),
    path('con_id',views.ConView.as_view()),

]