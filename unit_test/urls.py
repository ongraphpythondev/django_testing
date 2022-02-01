from django.urls import path , include
from .views import *


urlpatterns = [
    path('' , home , name = 'home'),
    path('<str:s>/' , single_post , name = 'single_post'),
    path('f/<str:s>/' , single_dj , name = 'single_dj'),
]