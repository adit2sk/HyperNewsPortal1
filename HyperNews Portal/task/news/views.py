import json

from django.conf import settings
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from typing import List

with open(settings.NEWS_JSON_PATH, "r") as file_in:
    NEWS: List[dict] = json.load(file_in)


class ComingSoonView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return HttpResponse("Coming soon")


class ArticleView(View):
    template_name = "news/article.html"

    def get(self, request: HttpRequest, article_id: int, *args, **kwargs) -> HttpResponse:
        for article in NEWS:
            if article.get("link") == article_id:
                return render(request, "news/article.html", {"article": article})
        raise Http404


class ArticleViewList(View):
    template_name = "news/article2.html"

    def get(self, request: HttpRequest, article_id: int, *args, **kwargs) -> HttpResponse:
        for article in NEWS:
            if article.get("link") == article_id:
                return render(request, "news/article.html", {"article": article})
        raise Http404

