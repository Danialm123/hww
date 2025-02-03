from django.views.generic import ListView, DetailView
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'  # Путь к вашему шаблону списка статей

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'  # Путь к вашему шаблону деталей статьи
