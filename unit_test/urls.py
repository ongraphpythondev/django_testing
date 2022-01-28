from django.urls import path , include
from .views import *


urlpatterns = [
    path('' , home , name = 'home'),
    path('<slug:post>/' , single_post , name = 'single_post'),
]