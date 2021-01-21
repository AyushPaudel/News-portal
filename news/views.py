from django.views import View
from django.shortcuts import redirect, render
from django.conf import settings
import json
from django.http import HttpResponse
from datetime import datetime

with open("/home/ayush007/Documents/HyperNews Portal/HyperNews Portal/task/news.json", "r+") as json_file:
    news_dis = json.load(json_file)


    class MainView(View):
        def get(self, request, *args, **kwargs):
            return redirect("/news/")



    class NewsView(View):
        def get(self, request, number, *args, **kwargs):
            context = {"news_dis": news_dis, "number": int(number)}
            return render(request, "news/index.html", context=context)


    class ListView(View):
        def get(self, request, *args, **kwargs):
            text = request.GET.get("q")
            context = {"news_dis": news_dis, "text": text}
            return render(request, "news/main.html", context=context)


    class CreateView(View):
        newpost = {}

        # def create(self, request):
        #
        #     if request.method == 'GET':
        #         return render(request, "news/create.html")
        #
        #     elif request.method == 'POST':
        #         title = request.POST.get('title')
        #         text = request.POST.get('text')
        #         self.newpost["created"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #         self.newpost["text"] = text
        #         self.newpost["title"] = title
        #         self.newpost["link"] = 4
        #         return redirect('/')

        def get(self, request):

            return render(request, "news/create.html")


        def post(self, request, *args, **kwargs):
            title = request.POST.get('title')
            text = request.POST.get('text')
            self.newpost["created"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.newpost["text"] = text
            self.newpost["title"] = title
            self.newpost["link"] = 4
            news_dis.append(self.newpost)
            return redirect('/news/')





