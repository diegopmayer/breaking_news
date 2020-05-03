from django.shortcuts import render
from .scrap_link import scrap_link


def get_link(request):
    content_news = scrap_link()
    return render(request, 'breaking_news/index.html', {
                            'content_news': content_news})
