import json
test = open('test.txt', 'a+')
from django.conf import settings
from typing import List

from django.urls import path
from .views import ArticleView
from .views import ComingSoonView

urlpatterns = [
    path("news", ComingSoonView.as_view(), name="index"),

    path("news/<int:link>/", ArticleView.as_view(), name="view_article"),
]
