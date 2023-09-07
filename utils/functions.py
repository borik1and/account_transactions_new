import json
import os

database_user = os.path.expanduser('~/account_transactions/operations.json')


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


def convert_date(converting_date):
    """функция преобразования даты из американского стандарта в стандарт ДД.ММ.ГГГГ"""
    date_parts = converting_date.split('-')
    formatted_date = '-'.join(date_parts[::-1])
    return formatted_date


def process_operations(data):
    """Фильтрация и сортировка операций"""
    executed_operations = [operation for operation in data if operation.get('state') == 'EXECUTED']
    sorted_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)
    """Выбор последних 5 операций"""
    latest_operations = sorted_operations[:5]
    """создание списка последних 5 операций"""
    formatted_operations = []
    for operation in latest_operations:
        date = operation['date'].split('T')[0]
        description = operation['description']
        from_account = mask_card_number(operation.get('from', ''))
        to_account = mask_account_number(operation['to'])
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']
        formatted_operation = (f"{convert_date(date)} {description}\n"
                               f"{from_account} -> {to_account}\n{amount} {currency}\n")
        formatted_operations.append(formatted_operation)

    return formatted_operations
