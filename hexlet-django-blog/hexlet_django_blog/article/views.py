from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import View
from django.urls import reverse

class IndexView(View):
    def get(self, request, tags, article_id):
        context = {
            'app_name': 'article',
            'tags': f"Тег {tags}",
            'article_id': f"Статья номер {article_id}",
        }
        return render(request, 'articles/index.html', context)
    
class HomeView(View):  
    def get(self, request):
        target_url = reverse('article', kwargs={'tags': 'python', 'article_id': 42})
        return redirect(target_url)
