"""novel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.IndexView.as_view()),
    path('democopy24', views.IndexView.as_view()),
    path('v1/ranks/', include('ranks.urls')),
    path('v1/fenlei/', include('fenlei.urls')),
    path('topic/',include('topic.urls')),
    path('content/',include('topic.urls')),
    path('v2/register_and_login/', include("register_and_login.urls")),
    path('v2/show_index_after_login/', include("show_index_after_login.urls")),
    path('v2/user_info/', include("user_info.urls")),
    path('v2/money/', include("money.urls")),
    path('v2/novel1/', include("novel1.urls")),
    path('v1/books/',include('books.urls')),
]
urlpatterns += static(settings.MEDIA_URL,
                    document_root=settings.MEDIA_ROOT)



