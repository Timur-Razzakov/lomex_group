from django.contrib import admin
from django import forms

from .models import Actor, Writer, Movie


class ActorAdmin(admin.ModelAdmin):
    fields = ('id', 'name')


class WriterAdmin(admin.ModelAdmin):
    fields = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    fields = ('id', 'title', 'imdb_rating', 'genre', 'writers_names', 'director', 'actor_names')


admin.site.register(Actor)
admin.site.register(Writer)
admin.site.register(Movie)

prepopulated_fields = {"Actor ": ("actors",)}
