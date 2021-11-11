#
# def get_api_directors(request):
#     for director in directors:
#         movie = Movie.objects.filter(director__contains=director).values('director', 'actor_names', 'imdb_rating', 'title')
#     # исп для подсчёта рейтинга
#     all_ratings = 0
#     # исп для показа количества фильмов каждого актёра
#     movies_count = 0
#     # исп для показа количества одного жанра
#     genre_count = 0
#     # перебираем каждого актёра из нашего списка
#     for director in directors:  # 1
#         # for genre in genres: and genre in item["genre"]
#         for item in ratings:
#             if item["director"] in 'N/A':
#                 continue
#             if director in item["director"]:
#                 movies_count += 1
#
#                 genre_count = 0
#         count_film = movies_count
#         movies_count = 0
#
#
#
# def get_api_genres(request):
#     results = []
#     for genre in genres:
#         # берём с бд поля которые нам нужны
#         movie = Movie.objects.filter(genre__contains=genre).values('title', 'imdb_rating')
#         imdb_rating = 0.0
#         movie_count = len(movie)
#         for item in movie:
#             if item["imdb_rating"] in 'N/A':
#                 continue
#             imdb_rating += float(item["imdb_rating"])
#         avg_rating = round(imdb_rating / movie_count, 1)
#
#         data = {
#             "genre": genre,
#             "movies_count": len(movie),
#             "avg_rating": avg_rating
#         }
#         results.append(data)

import operator

dict1 = {'Emilio Janhunen Calderón': 3, 'David Anghel': 4, 'Jonas Svensson': 2, 'Marina Janhunen Calderón': 1, 'Pauli Janhunen Calderón': 3}

sorted_tuples = sorted(dict1.items(), key=operator.itemgetter(1))
print(sorted_tuples)  # [(1, 1), (3, 4), (2, 9)]
for item in sorted_tuples:
    print(item[0][3])
sorted_dict = {k: v for k, v in sorted_tuples}
print(sorted_dict) # {1: 1, 3: 4, 2: 9}