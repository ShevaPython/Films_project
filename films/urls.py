from django.urls import path
from .views import MoviesView,MovieDetailViews,AddReview,ActorView,FilterMoviesView,AddStarRating,Search

urlpatterns = [
    path('',MoviesView.as_view(),name = 'show_films'),
    path("filter/",FilterMoviesView.as_view(), name='filter'),
    path('search/',Search.as_view(),name = 'search'),
    path('add-rating/',AddStarRating.as_view(),name='add_rating'),
    path('<slug:slug>/',MovieDetailViews.as_view(),name = 'film_detail'),
    path('review/<int:pk>/',AddReview.as_view(),name ='add_review'),
    path('actor/<str:slug>/',ActorView.as_view(),name='actor_detail'),

]