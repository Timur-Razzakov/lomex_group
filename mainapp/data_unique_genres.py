genre = set()


#     #  превращаем QueryString в json format
#     all_movie = serializers.serialize("json", Movie.objects.all(), fields=('genre', 'imdb_rating'))
#     # преобразовывем  в лист
#     first_batch = json.loads(all_movie)

# Указываем модель, откуда будем брать поле
def unique_genres(field_from_table, model): # передаём модель и поле из этой модели
    # Получаем поле из бд,для дальнейшего его использования
    all_movie = model.objects.all().values(field_from_table)
    all_movie_list = list(all_movie)
    # Получаем значения из списка словарей
    list_genre = set(val.replace(',', '') for dic in all_movie_list for val in dic.values())
    for line in list_genre:
        for word in line.split():
            genre.add(word)
    return genre

