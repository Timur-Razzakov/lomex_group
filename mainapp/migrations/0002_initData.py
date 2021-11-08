from django.db import migrations

import json


def movies_data(apps, schema_editor):
    with open('mainapp/fixtures/movies.json', 'r', encoding='UTF-8') as f:
        read = f.read()
        data = json.loads(read)
        art = apps.get_model('mainapp', 'Movie')
        writer_2 = apps.get_model('mainapp', 'Writer')
        actor = apps.get_model('mainapp', 'Actor')

        for item in data:
            ac = []
            wr = []
            # убираем лишние пробелы
            if item['writers'].strip():
                # преобразуем в json
                new_item = json.loads(item['writers'])
                wr = [item['id'] for item in new_item]
            else:
                # если верхний список пуст добавляем этот
                wr.append(item['writer'])
            # берёт объекты писателей из бд
            writers_objects = [writer_2.objects.get(id=x) for x in wr]
            movies = art(
                id=item['id'],
                title=item["title"],
                genre=item["genre"],
                director=item["director"],
                writers_names='',
                description=item["plot"],
                imdb_rating=item["imdb_rating"],
            )
            # берём каждое значение и проверяем его на None
            for writer in writers_objects:
                if writer.name == 'N/A':
                    movies.writers_names = None
                else:
                    # если имя последнее в списке, то запятую не ставим
                    if writer == writers_objects[-1]:
                        movies.writers_names += writer.name
                    else:
                        # ставим запятые после одного полного имени
                        name = writer.name + ", "
                        movies.writers_names += name
            movies.save()
            # Добавляем имена в модель
            for writer in writers_objects:
                movies.writers.add(writer)


def actor_data(apps, schema_editor):
    with open('mainapp/fixtures/art_actors.json', 'r', encoding='UTF-8') as f:
        read = f.read()
        data = json.loads(read)
        actor = apps.get_model('mainapp', 'Actor')
        for item in data:
            actor(
                id=item['id'],
                name=item["name"]
            ).save()


def writers_data(apps, schema_editor):
    with open('mainapp/fixtures/art_writers.json', 'r', encoding='UTF-8') as f:
        read = f.read()
        data = json.loads(read)
        writer = apps.get_model('mainapp', 'Writer')
        for item in data:
            writer(
                id=item['id'],
                name=item["name"]
            ).save()


class Migration(migrations.Migration):
    dependencies = [
        ('mainapp', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(actor_data),
        migrations.RunPython(writers_data),
        migrations.RunPython(movies_data),
    ]
