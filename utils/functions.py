import json


def open_json_file_r(database):
    """Загрузка данных из файла operations.json"""
    with open(database, 'r') as file:
        operations_data = json.load(file)
    return operations_data


def mask_card_number(card_number):
    """ Функция для маскирования номера карты"""
    return f'XXXX XX** **** {card_number[-4:]}'


#
def mask_account_number(account_number):
    """Функция для маскирования номера счета"""
    return f'**{account_number[-4:]}'
