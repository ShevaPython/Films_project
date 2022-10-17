from django.contrib import admin
from .models import Category, Actor, RatingStar, Rating, Reviews, Genre, Movie, MovieShots


class RewieInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'url': ('title',)}
    list_display = ('id', 'title', 'poster', 'category', 'url', 'draft',)
    list_filter = ('category', 'year',)
    search_fields = ('title', 'category__name')
    inlines = [RewieInline]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    fieldsets = (
        ('Name_Films', {
            "fields": (('title', "tagline"),)
        }),
        ('Description', {
            "fields": (('description', "poster"),)
        }),
        ('Dates_films', {
            "fields": (('year', 'world_premiere', "country"),)
        }),
        ('Produser_Ganre', {
            'classes': ('collapse',),
            "fields": (('actors', 'directors', 'genre'), 'category')
        }),
        ('Money_films', {
            "fields": (('budget', "fees_in_usa", "fees_in_world"),)
        }),
        ('Url_Draft', {
            "fields": (('url', "draft"),)
        }),

    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}
    list_display = ('id', 'name', 'url')
    list_display_links = ('id', 'name')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}
    list_display = ('name', 'url')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'image')


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    ist_display = ('title', 'movie', 'image')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    ist_display = ('star', 'ip',)


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'parent', 'movie')
    readonly_fields = ('id', 'email')


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('value',)
