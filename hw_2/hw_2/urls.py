from django.contrib import admin
from django.urls import path
from movie.views import MovieListView, MovieDetailView
from blog.views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', MovieListView.as_view(), name='movie_list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
]