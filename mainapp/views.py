import json
from django.http import HttpResponse
from django.shortcuts import render
from icecream import ic

from .models import Actor, Movie

from .data_unique import unique_genres, unique_actors, unique_directors

# TODO: получаем уникальные жанры

genres = unique_genres('genre', Movie)
actors = unique_actors('name', Actor)
directors = unique_directors('director', Movie)


def index(request):
    return render(request, 'mainapp/index.html')


def get_api_genres(request):
    results = []
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

        data = {
            "genre": genre,
            "movies_count": len(movie),
            "avg_rating": avg_rating
        }
        results.append(data)

    return HttpResponse(json.dumps(results), content_type='application/json')


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

        movie_list = list(movie)
        data = {
            "actor_name": actor,
            "movies_count": len(movie),
            "best_genre": movie_list[0]['genre']
        }
        results.append(data)

    return HttpResponse(json.dumps(results), content_type='application/json')


def get_api_directors(request):
    results = []
    for director in directors:
        if director in "N/A" or director is None:
            continue

        movies = Movie.objects.filter(director__contains=director) \
            .order_by('-imdb_rating') \
            .values('actor_names', 'title')

        movies = list(movies)
        actors_set = set(item['actor_names'] for item in movies)
        actors_list = set()

        for item in actors_set:
            if item is None:
                continue
            for it in item.split(','):
                actors_list.add(it.strip())
        # из списка создаём словарь, для подсчёта количества фильмов у актёра
        actors_count = dict.fromkeys(actors_list, 0)

        for movie in movies:
            if movie['actor_names'] is None:
                movies.remove(movie)
                continue
            for act_name, _ in actors_count.items():
                if act_name in movie['actor_names']:
                    actors_count[act_name] += 1

        sorted_list = [{"name": k, "movie_count": v}
                       for k, v in sorted(actors_count.items(), key=lambda item: item[1], reverse=True)]

        data = {
            "director_name": director,
            "favorite_actors": sorted_list[:3],
            "best_movies": movies[:3]
        }

        results.append(data)
    return HttpResponse(json.dumps(results), content_type='application/json')
