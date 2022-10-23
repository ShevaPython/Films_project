from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View

from .models import Movie, Category, Actor, Genre
from .forms import ReviewsForm


class GenreYear:
    """Жанры и года выхода фильмов"""
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values("year")


class MoviesView(GenreYear, ListView):
    '''Список фильмов'''
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    context_object_name = 'films'
    template_name = 'films/movies_list.html'


class MovieDetailViews(GenreYear, DetailView):
    '''Полное описания фильма'''
    model = Movie
    slug_field = 'url'
    context_object_name = 'film'
    template_name = 'films/movie_detail.html'


class AddReview(View):
    '''Отправка отзывов'''

    def post(self, request, pk):
        form = ReviewsForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class ActorView(GenreYear, DetailView):
    """Вывод информации о актере"""
    model = Actor
    template_name = 'films/actor.html'
    slug_field = 'name'


class FilterMoviesView(GenreYear, ListView):
    """Фильтр фильмов"""
    template_name = 'films/movies_list.html'
    context_object_name = 'films'
    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genre__in=self.request.GET.getlist("genre"))
        )
        return queryset
