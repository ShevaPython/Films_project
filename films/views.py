from django.shortcuts import render
from django.views.generic import ListView,DetailView

from .models import Movie


class MoviesView(ListView):
    '''Список фильмов'''
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    context_object_name = 'films'
    template_name = 'films/movies_list.html'


class MovieDetailViews(DetailView):
    '''Полное описания фильма'''
    model = Movie
    slug_field = 'url'
    context_object_name = 'film'
    template_name = 'films/movie_detail.html'
