import json
import os

database_user = os.path.expanduser('~/account_transactions/operations.json')


def open_json_file_r(database):
    """Загрузка данных из файла operations.json"""
    with open(database, 'r') as file:
        operations_data = json.load(file)
    return operations_data


print(open_json_file_r(database_user))
