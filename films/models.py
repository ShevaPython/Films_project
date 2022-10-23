from django.db import models
from datetime import date
from django.urls import reverse

class Category(models.Model):
    '''Категории'''
    name = models.CharField('Категория', max_length=200, )
    description = models.TextField('Описане')
    url = models.SlugField(max_length=100, verbose_name='Url категории', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Actor(models.Model):
    '''Актеры и режисеры'''
    name = models.CharField('Имя', max_length=150)
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    description = models.TextField('Описане')
    image = models.ImageField('Изображения', upload_to='actors/%Y/%m/%d')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актер и режиссер'
        verbose_name_plural = 'Актеры и режиссеры'

    def get_absolute_url(self):
        return reverse('actor_detail', kwargs={'slug': self.name})

class Genre(models.Model):
    '''Жанры'''
    name = models.CharField('Жанр', max_length=200, )
    description = models.TextField('Описане')
    url = models.SlugField(max_length=160, verbose_name='Url жанра', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    """Фильмы"""
    title = models.CharField("Названия фильма", max_length=100)
    tagline = models.CharField('Слоган', max_length=100, default='')
    description = models.TextField('Описане')
    poster = models.ImageField('Постер', upload_to='movies/%Y/%m/%d')
    year = models.PositiveSmallIntegerField('Дата выхода', default=2018)
    country = models.CharField('Город', max_length=50)
    actors = models.ManyToManyField(Actor, verbose_name='актеры', related_name='film_actor')
    directors = models.ManyToManyField(Actor, verbose_name='директоры', related_name='film_director')
    genre = models.ManyToManyField(Genre, verbose_name='жанры')
    world_premiere = models.DateField('Премьера в мире', default=date.today)
    budget = models.PositiveIntegerField('Бюджет', default=0, help_text='Укажите сумму в доларах')
    fees_in_usa = models.PositiveIntegerField('Сборы в USA', default=0, help_text='Укажите сумму в доларах')
    fees_in_world = models.PositiveIntegerField('Сборы в Мире', default=0, help_text='Укажите сумму в доларах')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True, blank=True)
    url = models.SlugField(max_length=100, verbose_name='Url Фильма', unique=True)
    draft = models.BooleanField('Черновик', default=False)

    def __str__(self):
        return self.title

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = "Фильмы"

    def get_absolute_url(self):
        return reverse('film_detail', kwargs={'slug': self.url})


class MovieShots(models.Model):
    """Кадры из фильма"""
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описане')
    image = models.ImageField('Изображения', upload_to='movie_shots/%Y/%m/%d')
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'


class RatingStar(models.Model):
    '''Звезды рейтинга'''
    value = models.SmallIntegerField('Значения', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'


class Rating(models.Model):
    '''Рейтинг'''
    ip = models.CharField('IP адресс', max_length=15)
    stat = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='Звезда')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм')

    def __str__(self):
        return F'{self.stat}-{self.movie}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Reviews(models.Model):
    '''Отзывы'''
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Сообщения', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, null=True, blank=True)
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return F'{self.name}-{self.movie}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
