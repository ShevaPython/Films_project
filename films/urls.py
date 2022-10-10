from django.urls import path
from .views import MoviesView,MovieDetailViews

urlpatterns = [
    path('',MoviesView.as_view(),name = 'show_films'),
    path('<slug:slug>/',MovieDetailViews.as_view(),name = 'film_detail')
]