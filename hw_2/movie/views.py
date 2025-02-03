from django.views.generic import ListView, DetailView
from .models import Movie

class MovieListView(ListView):
    model = Movie
    template_name = 'movie/movie_list.html'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie/movie_detail.html'