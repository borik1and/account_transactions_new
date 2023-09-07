import os

from utils.functions import convert_date, mask_account_number, mask_card_number, open_json_file_r, process_operations


# from utils.functions import mask_account_number
# from utils.functions import mask_card_number
# from utils.functions import open_json_file_r


def test_json_file():
    # Укажите путь к вашему JSON-файлу
    file_test = os.path.expanduser('~/account_transactions/tests/file_test.json')
    # Ожидаемые данные
    expected_data = [{
        "key1": "value1",
        "key2": "value2",
    }]
    actual_data = open_json_file_r(file_test)
    assert actual_data == expected_data


def test_mask_card_number():
    assert mask_card_number('1596837868705199') == 'XXXX XX** **** 5199'


def test_mask_account_number():
    assert mask_account_number('1596837868705199') == '**5199'


def test_convert_date():
    date_amer = "2010-10-02"
    assert convert_date(date_amer) == '02-10-2010'


def test_process_operations():
    operations_data = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },

    ]

    formatted_operations = process_operations(operations_data)

    """Проверяем ожидаемый результат"""
    assert len(formatted_operations) == 1
