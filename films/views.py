from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View

from .models import Movie
from .forms import ReviewsForm


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


class AddReview(View):
    '''Отправка отзывов'''

    def post(self, request, pk):
        form = ReviewsForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent',None):
                form.parent_id = int(request.POST.get('parent'))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
