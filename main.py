import psycopg2
from psycopg2 import Error

import csv

from utils_create import *
from utils_upload import *
from utils_convert import *

def connect_db():
    """
    Устанавливает соединение с базой данных.
    """
    try:
        connection = psycopg2.connect(user='postgres', password='postgres', database='lesson_18', host='127.0.0.1', port='5432')
        connection.autocommit = True
        return connection
    except (Exception, Error) as error:
        print(f'connection failed, {error}')
        return False


def main():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        create_db(cursor)
        create_animal_types_table(cursor)
        create_breeds_table(cursor)
        create_colors_table(cursor)
        create_animals_table(cursor)
        create_outcome_types_table(cursor)
        create_outcome_subtypes_table(cursor)
        create_shelter_outcomes_table(cursor)

        data = []
        with open('main_animals.csv', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                data.append(row)

        del data[0]

        list_of_animal_types = set(["('" + list_of_data[3] + "')" for list_of_data in data])
        animal_types_to_upload = ','.join(map(str, list_of_animal_types))
        upload_animal_types(cursor, animal_types_to_upload)

        list_of_breeds = list(set(["('" + list_of_data[5] + "')" for list_of_data in data]))
        breeds_to_upload = ','.join(map(str, list_of_breeds))
        upload_breeds(cursor, breeds_to_upload)

        list_of_colors_1 = set(["('" + list_of_data[6].strip() + "')" for list_of_data in data])
        list_of_colors_2 = (["('" + list_of_data[7].strip() + "')" for list_of_data in data])
        list_of_colors = list_of_colors_1.union(list_of_colors_2)
        colors_to_upload = ','.join(map(str, list_of_colors))
        upload_colors(cursor, colors_to_upload)

        req_get_animal_types = """
        SELECT *
        FROM animal_types
        """
        animal_types_dict = make_dict(get_data(cursor, req_get_animal_types))

        req_get_breeds = """
        SELECT *
        FROM breeds
        """
        breeds_dict = make_dict(get_data(cursor, req_get_breeds))

        req_get_colors = """
        SELECT *
        FROM colors
        """
        colors_dict = make_dict(get_data(cursor, req_get_colors))

        list_of_animals = [(dt[2], dt[4].replace("'", ""), animal_types_dict[dt[3]], breeds_dict[dt[5]], colors_dict[dt[6].strip()], colors_dict[dt[7]], dt[8]) for dt in data]
        list_of_animals_to_upload = ','.join(map(str, list_of_animals))
        upload_animals(cursor, list_of_animals_to_upload)

        list_of_outcome_types = list(set(["('" + list_of_data[10] + "')" for list_of_data in data]))
        outcome_types_to_upload = ','.join(map(str, list_of_outcome_types))
        upload_outcome_types(cursor, outcome_types_to_upload)

        list_of_outcome_subtypes = list(set(["('" + list_of_data[9] + "')" for list_of_data in data]))
        outcome_subtypes_to_upload = ','.join(map(str, list_of_outcome_subtypes))
        upload_outcome_subtypes(cursor, outcome_subtypes_to_upload)

        req_get_outcome_subtypes = """
         SELECT *
         FROM outcome_subtypes
         """
        outcome_subtypes_dict = make_dict(
            get_data(cursor, req_get_outcome_subtypes))

        req_get_outcome_types = """
         SELECT *
         FROM outcome_types
         """
        outcome_types_dict = make_dict(get_data(cursor, req_get_outcome_types))

        req_get_animal_ids = """
         SELECT id_animal, animal_code_id
         FROM animals
         """
        animal_ids_dict = make_dict(get_data(cursor, req_get_animal_ids))

        list_of_shelter_outcomes = [(animal_ids_dict[dt[2]], outcome_subtypes_dict[dt[9]], outcome_types_dict[dt[10]], dt[11], dt[12], dt[1]) for dt in data]
        list_of_shelter_outcomes_to_upload = ','.join(map(str, list_of_shelter_outcomes))
        upload_shelter_outcomes(cursor, list_of_shelter_outcomes_to_upload)

        add_user(cursor, 'SELECT', 'reading_user')
        add_user(cursor, 'UPDATE, DELETE', 'updating_deleting_user')

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

if __name__ =='__main__':
    main()
