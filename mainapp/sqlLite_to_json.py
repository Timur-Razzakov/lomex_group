import json

import sqlite3


def dict_factory(cur, row):
    d = {}
    for idx, col in enumerate(cur.description):
        d[col[0]] = row[idx]
    return d


conn = sqlite3.connect("../mydata.db")
conn.row_factory = dict_factory
cursor = conn.cursor()
cursor.execute("SELECT * FROM actors ")
json_string = cursor.fetchall()
print(json_string)
# # with open('fixtures/art_actors.json', 'w', encoding='UTF-8') as f:
# #     json.dump(json_string, f, ensure_ascii=False, indent=4)
#
# # yaml_string = cursor.fetchall()
# # with open('fixtures/art_writers.yaml', 'w', encoding='utf-8') as f:
# #     yaml.dump(yaml_string, f, default_flow_style=False, )
