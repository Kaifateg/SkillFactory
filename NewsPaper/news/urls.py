from django.urls import path
from .views import *


urlpatterns = [
    path('news/', PostNews.as_view()),
    path('news/<int:pk>', PostNW.as_view()),
]