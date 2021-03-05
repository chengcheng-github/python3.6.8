from django.urls import path
from . import views

#http://127.0.0.1:8000/books/email
urlpatterns = [
    path('<str:mail>/books',views.BooksView.as_view()),

]