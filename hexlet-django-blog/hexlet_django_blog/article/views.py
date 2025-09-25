from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View


class IndexView(View):
    def get(self, request):
        context = {
            'app_name': 'article',
        }
        return render(request, 'articles/index.html', context)
