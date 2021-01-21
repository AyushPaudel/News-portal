from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings


from news.views import MainView, NewsView, ListView, CreateView

urlpatterns = [
    path("", MainView.as_view()),
    path("news/", ListView.as_view()),
    path("news/create/", CreateView.as_view()),
    re_path("news/(?P<number>[0-9]+)/?", NewsView.as_view()),

]

urlpatterns += static(settings.STATIC_URL)