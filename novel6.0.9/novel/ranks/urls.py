#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author JourWon
# @date 2021/2/15
# @file urls.py
from django.urls import path, include
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    # http://127.0.0.1:8000/v1/ranks/novel_rank
    path('novel_rank', cache_page(600, cache='ranks')(views.NovelsIndexView.as_view())),


]




