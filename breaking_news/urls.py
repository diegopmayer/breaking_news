from django.urls import path
from .views import get_link

urlpatterns = [
    path('', get_link, name='get_link'),
]