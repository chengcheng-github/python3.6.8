from django.urls import path

from . import views

urlpatterns = [
    # http://127.0.0.1:8000/v1/ranks/novel_rank
    path('', views.FenleiView.as_view()),
    path('<str:url>', views.FenleiView.as_view()),
]