genres = set()
actors = set()
directors = set()

#     #  превращаем QueryString в json format
#     all_movie = serializers.serialize("json", Movie.objects.all(), fields=('genre', 'imdb_rating'))
#     # преобразовывем  в лист
#     first_batch = json.loads(all_movie)

# Указываем модель, откуда будем брать поле
def unique_genres(field_from_table, model):  # передаём модель и поле из этой модели
    # Получаем поле из бд,для дальнейшего его использования
    all_movie = model.objects.all().values(field_from_table)
    all_movie_list = list(all_movie)
    # Получаем значения из списка словарей
    list_genre = set(val.replace(',', '') for dic in all_movie_list for val in dic.values())
    for line in list_genre:
        for word in line.split():
            genres.add(word)
    return genres


def unique_actors(field_from_table, model):
    all_movie = model.objects.all().values(field_from_table)
    all_movie_list = list(all_movie)
    # Получаем уникальные имена
    set_actor = set(val for dic in all_movie_list for val in dic.values())
    for name in set_actor:
        actors.add(name)
    return actors


def unique_directors(field_from_table, model):
    all_movie = model.objects.all().values(field_from_table)
    all_movie_list = list(all_movie)
    # Получаем уникальные имена
    set_directors = set(dic['director'] for dic in all_movie_list)
    for item in set_directors:
        for name in item.split(','):
            directors.add(name)
    return directors
