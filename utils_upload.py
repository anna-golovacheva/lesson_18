import psycopg2
from psycopg2 import Error


def upload_animal_types(cursor, data_to_upload: str) -> None:
    """
    Загружает данные в таблицу animal_types.
    """
    req = f"""
    INSERT INTO public.animal_types (type)
    VALUES {data_to_upload}
    """
    try:
        cursor.execute(req)
        print('animal types data uploaded')
    except (Exception, error) as error:
        print(f'uploading failed, {error}')


def upload_breeds(cursor, data_to_upload: str) -> None:
    """
    Загружает данные в таблицу breeds.
    """
    req = f"""
    INSERT INTO breeds (breed)
    VALUES {data_to_upload}
    """
    try:
        cursor.execute(req)
        print('breeds data uploaded')
    except (Exception, error) as error:
        print(f'uploading failed, {error}')


def upload_colors(cursor, data_to_upload: str) -> None:
    """
    Загружает данные в таблицу colors.
    """
    req = f"""
    INSERT INTO colors (color)
    VALUES {data_to_upload}
    """
    try:
        cursor.execute(req)
        print('colors data uploaded')
    except (Exception, error) as error:
        print(f'uploading failed, {error}')


def upload_animals(cursor, data_to_upload: str) -> None:
    """
    Загружает данные в таблицу animals.
    """
    req = f"""
    INSERT INTO animals (animal_code_id, name, fk_animal_type, fk_breed, fk_color_1, fk_color_2, date_of_birth)
    VALUES {data_to_upload}
    """
    try:
        cursor.execute(req)
        print('animals data uploaded')
    except (Exception, error) as error:
        print(f'uploading failed, {error}')


def upload_outcome_types(cursor, data_to_upload: str) -> None:
    """
    Загружает данные в таблицу outcome_types.
    """
    req = f"""
    INSERT INTO outcome_types (outcome_type)
    VALUES {data_to_upload}
    """
    try:
        cursor.execute(req)
        print('outcome types data uploaded')
    except (Exception, error) as error:
        print(f'uploading failed, {error}')


def upload_outcome_subtypes(cursor, data_to_upload: str) -> None:
    """
    Загружает данные в таблицу outcome_subtypes.
    """
    req = f"""
    INSERT INTO outcome_subtypes (outcome_subtype)
    VALUES {data_to_upload}
    """
    try:
        cursor.execute(req)
        print('outcome subtypes data uploaded')
    except (Exception, error) as error:
        print(f'uploading failed, {error}')


def upload_shelter_outcomes(cursor, data_to_upload: str) -> None:
    """
    Загружает данные в таблицу shelter_outcomes.
    """
    req = f"""
    INSERT INTO shelter_outcomes (fk_animal_id, fk_outcome_subtype, fk_outcome_type, outcome_month, outcome_year, age_upon_outcome)
    VALUES {data_to_upload}
    """
    try:
        cursor.execute(req)
        print('shelter outcomes data uploaded')
    except (Exception, error) as error:
        print(f'uploading failed, {error}')