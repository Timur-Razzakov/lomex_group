import json
import re

from django.core import serializers
from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import render
from .models import Actor, Writer, Movie

from .data_unique import unique_genres, unique_actors, unique_directors

# TODO: преобразовать каждую функцию в Json
# TODO: вывести на фронт
# TODO: Дописать функцию Director
# получаем уникальные жанры

genres = unique_genres('genre', Movie)
actors = unique_actors('name', Actor)
directors = unique_directors('director', Movie)


def index(request):
    return render(request, 'mainapp/index.html')


def get_api_genres(request):
    for genre in genres:
        # берём с бд поля которые нам нужны
        movie = Movie.objects.filter(genre__contains=genre).values('title', 'imdb_rating')
        imdb_rating = 0.0
        movie_count = len(movie)
        for item in movie:
            if item["imdb_rating"] in 'N/A':
                continue
            imdb_rating += float(item["imdb_rating"])
        avg_rating = round(imdb_rating / movie_count, 1)

        print(genre, movie_count, avg_rating, '\n--------------------')
    return render(request, 'mainapp/genres.html', )


def get_api_actors(request):
    results = []
    for actor in actors:
        try:
            movie = Movie.objects.filter(actor_names__contains=actor) \
                .order_by('-imdb_rating') \
                .values('genre')
        except Exception:
            movie = None

        if movie is None:
            continue
        print(movie, actor)
        movie_list = list(movie)
        try:
             m = movie_list[0]['genre']
        except Exception:
            print(movie_list)
        data = {
            "actor_name": actor,
            "movies_count": len(movie),
            "best_genre": movie_list[0]['genre']
        }
        results.append(data)

    # return json.dumps(results)
    return HttpResponse(json.dumps(results), content_type='application/json')


def get_api_directors(request):
    ratings = Movie.objects.all().values('director', 'actor_names', 'imdb_rating', 'title')
    # исп для подсчёта рейтинга
    all_ratings = 0
    # исп для показа количества фильмов каждого актёра
    movies_count = 0
    # исп для показа количества одного жанра
    genre_count = 0
    # перебираем каждого актёра из нашего списка
    for director in directors:  # 1
        # for genre in genres: and genre in item["genre"]
        for item in ratings:
            if item["director"] in 'N/A':
                continue
            if director in item["director"]:
                movies_count += 1

                genre_count = 0
        count_film = movies_count
        movies_count = 0

    # if item["imdb_rating"] in 'N/A':
    #     continue
    # all_ratings += float(item["imdb_rating"])
    #
    # print(actor, movies_count, all_ratings, )

    return render(request, 'mainapp/directors.html')

# def index(request):
#     #  превращаем QueryString в json format
#     all_movie = serializers.serialize("json", Movie.objects.all(), fields=('genre', 'imdb_rating'))
#     # преобразовывем  в лист
#     first_batch = json.loads(all_movie)
#     # s =set(var for dic in first_batch for var in dic.values())
#     # print(s)
#     # перебирем каждую таблицу
#     # for items in first_batch:
#     #     if items is 'genre':
#     #         print(items['genre'])
#     # genre_1 = [item['genre'] for item in all_movie]
#     print((all_movie))
#     print(type(first_batch))
#
#     # print(type(first_batch))
#     # for item in all_movie:
#     #     m = item.objects.get(genre=item['genre'])
#     #     print(m)
#     return render(request, 'mainapp/index.html', {'all_movie': all_movie})
