import psycopg2
from psycopg2 import Error


def create_db(cursor) -> None:
    """
    Создает базу данных.
    """
    req = """
    CREATE DATABASE lesson_18
    """
    try:
        cursor.execute(req)
        print('database created')
    except (Exception, Error) as error:
        print(f'creation failed, {error}')


def create_animal_types_table(cursor) -> None:
    """
    Создает таблицу видов животных.
    """
    req = """
    CREATE TABLE IF NOT EXISTS animal_types (
    type_id SERIAL PRIMARY KEY,
    type VARCHAR
    )
    """
    try:
        cursor.execute(req)
        print('animal_types table created')
    except (Exception, Error) as error:
        print(f'creation failed, {error}')


def create_breeds_table(cursor) -> None:
    """
    Создает таблицу пород.
    """
    req = """
    CREATE TABLE IF NOT EXISTS breeds (
    breed_id SERIAL PRIMARY KEY,
    breed VARCHAR
    )
    """
    try:
        cursor.execute(req)
        print('breed table created')
    except (Exception, Error) as error:
        print(f'creation failed, {error}')


def create_colors_table(cursor) -> None:
    """
    Создает таблицу цветов.
    """
    req = """
    CREATE TABLE IF NOT EXISTS colors (
    color_id SERIAL PRIMARY KEY,
    color VARCHAR
    )
    """
    try:
        cursor.execute(req)
        print('colors table created')
    except (Exception, Error) as error:
        print(f'creation failed, {error}')


def create_animals_table(cursor) -> None:
    """
    Создает таблицу животных
    """
    req = """
    CREATE TABLE IF NOT EXISTS animals (
    id_animal SERIAL PRIMARY KEY,
    animal_code_id VARCHAR,
    name VARCHAR,
    fk_animal_type INTEGER,
    fk_breed INTEGER,
    fk_color_1 INTEGER,
    fk_color_2 INTEGER,
    date_of_birth TIMESTAMP,
    FOREIGN KEY (fk_animal_type) REFERENCES animal_types (type_id),
    FOREIGN KEY (fk_breed) REFERENCES breeds (breed_id),
    FOREIGN KEY (fk_color_1) REFERENCES colors (color_id),
    FOREIGN KEY (fk_color_2) REFERENCES colors (color_id)
    )
    """
    try:
        cursor.execute(req)
        print('animals table created')
    except (Exception, Error) as error:
        print(f'creation failed, {error}')


def create_outcome_types_table(cursor) -> None:
    """
    Создает таблицу данных о том, что сейчас происходит с животным.
    """
    req = """
    CREATE TABLE IF NOT EXISTS outcome_types (
    outcome_type_id SERIAL PRIMARY KEY,
    outcome_type VARCHAR
    )
    """
    try:
        cursor.execute(req)
        print('outcome_types table created')
    except (Exception, Error) as error:
        print(f'creation failed, {error}')


def create_outcome_subtypes_table(cursor) -> None:
    """
    Создает таблицу с данными по программам, в которых участвуют животные.
    """
    req = """
    CREATE TABLE IF NOT EXISTS outcome_subtypes (
    outcome_subtype_id SERIAL PRIMARY KEY,
    outcome_subtype VARCHAR
    )
    """
    try:
        cursor.execute(req)
        print('outcome_subtypes table created')
    except (Exception, Error) as error:
        print(f'creation failed, {error}')


def create_shelter_outcomes_table(cursor) -> None:
    """
    Создает таблицу данных приюта.
    """
    req = """
    CREATE TABLE IF NOT EXISTS shelter_outcomes (
    outcome_id SERIAL PRIMARY KEY,
    fk_animal_id INTEGER,
    fk_outcome_subtype INTEGER,
    fk_outcome_type INTEGER,
    outcome_month INTEGER,
    outcome_year INTEGER,
    age_upon_outcome VARCHAR,
    FOREIGN KEY (fk_animal_id) REFERENCES animals (id_animal),
    FOREIGN KEY (fk_outcome_subtype) REFERENCES outcome_subtypes (outcome_subtype_id),
    FOREIGN KEY (fk_outcome_type) REFERENCES outcome_types (outcome_type_id)
    )
    """
    try:
        cursor.execute(req)
        print('animals table created')
    except (Exception, Error) as error:
        print(f'creation failed, {error}')


def add_user(cursor, privileges: str, username: str) -> None:
    """
    Создает пользователя с именем и правами, переданными в аргументах.
    """
    req_1 = f"""CREATE USER {username} WITH PASSWORD '1111'"""
    req_2 = f"""GRANT {privileges} ON ALL TABLES in SCHEMA public to {username}"""

    try:
        cursor.execute(req_1)
        print('Новый пользователь создан.')
        cursor.execute(req_2)
        print(f'Новому пользователю переданы права.')
    except (Exception, Error) as error:
        print(f'Не получилось создать {username}, {error}')
