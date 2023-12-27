from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page),
    path('comments/', comments, name='comments'),
    path('thanks/', thanks_page, name='thanks_page'),
]