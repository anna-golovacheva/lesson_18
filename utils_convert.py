import psycopg2
from psycopg2 import Error


def get_data(cursor, req: str) -> list:
    """
    Получает и возвращает данные из базы данных.
    """
    try:
        cursor.execute(req)
        data = cursor.fetchall()
        return data
    except (Exception, Error) as error:
        print(f'uploading failed, {error}')


def make_dict(getter: list) -> dict:
    """
    Создает и возвращает словарь из полученных данных.
    """
    data = getter
    data_dict = {}
    for dt in data:
        data_dict[dt[1]] = dt[0]
    return data_dict
