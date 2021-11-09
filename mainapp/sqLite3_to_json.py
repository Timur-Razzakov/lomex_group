import json

import sqlite3


def export_data(place_and_final_name, pale_database_name, table_name):
    def dict_factory(cur, row):
        d = {}
        for idx, col in enumerate(cur.description):
            d[col[0]] = row[idx]
        return d

    conn = sqlite3.connect(pale_database_name)
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM " + table_name)
    json_string = cursor.fetchall()
    with open(place_and_final_name, 'w', encoding='UTF-8') as f:
        json.dump(json_string, f, ensure_ascii=False, indent=4)


#
# # yaml_string = cursor.fetchall()
# # with open('fixtures/art_writers.yaml', 'w', encoding='utf-8') as f:
# #     yaml.dump(yaml_string, f, default_flow_style=False, )

export_data('fixtures/test.json', '../mydata.db', 'actors')
