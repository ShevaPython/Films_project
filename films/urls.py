from django.urls import path
from .views import MoviesView,MovieDetailViews,AddReview

urlpatterns = [
    path('',MoviesView.as_view(),name = 'show_films'),
    path('<slug:slug>/',MovieDetailViews.as_view(),name = 'film_detail'),
    path('review/<int:pk>/',AddReview.as_view(),name ='add_review')
]