from django.shortcuts import render
from .scrap_link import scrap_link
import pandas as pd


def get_link(request):
    
    posts = scrap_link()

    return render(request, 'breaking_news/index.html', 
                            context={'posts':posts})
