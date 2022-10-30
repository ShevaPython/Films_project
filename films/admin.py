from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Actor, RatingStar, Rating, Reviews, Genre, Movie, MovieShots


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание',widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


class RewieInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


class MovieShordsLine(admin.StackedInline):
    model = MovieShots
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(F'<img src={obj.image.url} width="100" height = "110"')

    get_image.short_description = 'Изображения'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'url': ('title',)}
    list_display = ('id', 'title', 'get_poster', 'category', 'url', 'draft',)
    list_filter = ('category', 'year',)
    list_display_links = ('id','title')
    search_fields = ('title', 'category__name')
    inlines = [MovieShordsLine, RewieInline]
    save_on_top = True
    save_as = True
    readonly_fields = ('get_poster',)
    list_editable = ('draft',)
    form = MovieAdminForm
    fieldsets = (
        ('Name_Films', {
            "fields": (('title', "tagline"),)
        }),
        ('Description', {
            "fields": ('description', ("get_poster", 'poster'))
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

    def get_poster(self, obj):
        return mark_safe(F'<img src={obj.poster.url} width="50" height = "60"')

    get_poster.short_description = 'Постер'


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
    list_display = ('name', 'age', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(F'<img src={obj.image.url} width="50" height = "60"')

    get_image.short_description = 'Изображения'


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'movie', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(F'<img src={obj.image.url} width="50" height = "60"')

    get_image.short_description = 'Изображения'


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('ip','star','movie')


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'parent', 'movie')
    readonly_fields = ('id', 'email')


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('value',)


admin.site.site_title = 'Django Moview'
admin.site.site_header = 'Django Moview'
