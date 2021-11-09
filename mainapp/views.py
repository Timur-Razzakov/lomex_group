import re
from django.shortcuts import render
from .models import Actor, Writer, Movie

from .data_unique_genres import unique_genres

# получаем уникальные жанры
genres = unique_genres('genre', Movie)


def get_api_genres(request):
    ratings = Movie.objects.all().values('title', 'imdb_rating', 'genre')
    all_ratings = 0
    movies_count = 0
    # перебираем каждый жанр из нашего списка
    for genre in genres:
        for item in ratings:
            if genre in item["genre"]:
                movies_count += 1
                if item["imdb_rating"] in 'N/A':
                    continue
                all_ratings += float(item["imdb_rating"])
        avg_rating = all_ratings / movies_count
        print('-------------------',genre, movies_count, avg_rating, sep='\n')
    return render(request, 'mainapp/index.html', )

#
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
