from django.contrib import admin
from .models import Category, Actor, RatingStar, Rating, Reviews, Genre, Movie, MovieShots


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    pass


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    pass


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    pass


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    pass
