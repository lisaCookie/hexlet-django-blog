from django.urls import path

from hexlet_django_blog.article import views
from .views import IndexView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('articles/<str:tags>/<int:article_id>/',
          IndexView.as_view(), name='article'),
]