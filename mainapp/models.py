import uuid

from django.db import models


class Actor(models.Model):
    id = models.CharField(max_length=255,primary_key=True, editable=False, default='')
    # id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255, verbose_name='Имя актёра')

    def __str__(self):
        return self.name


class Writer(models.Model):
    id = models.CharField(max_length=255,primary_key=True, editable=False, default='')
    # id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255, verbose_name='Имя Писателя')

    def __str__(self):
        return self.name


class Movie(models.Model):
    id = models.CharField(max_length=255,primary_key=True, editable=False, default='')
    # id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=255, verbose_name='Название фильма')
    imdb_rating = models.CharField(max_length=255, verbose_name='Рейтинг фильмов')
    genre = models.CharField(max_length=255, verbose_name='Жанры')
    description = models.CharField(max_length=255, verbose_name='Описание фильма')
    writers = models.ManyToManyField(Writer, blank=True, verbose_name='Писатель', related_name='Movie')
    writers_names = models.CharField(verbose_name='Список имён писателей', max_length=255, null=True)
    director = models.CharField(max_length=255, verbose_name='Режисёр')
    actors = models.ManyToManyField(Actor, blank=True, verbose_name='Актёр', related_name='Movie')
    actor_names = models.CharField(verbose_name='Список имён актёров', max_length=255,null=True)

    def __str__(self):
        return self.title
