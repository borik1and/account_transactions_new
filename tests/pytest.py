from utils.functions import open_json_file_r
from utils.functions import mask_card_number

def test_json_file():
    # Укажите путь к вашему JSON-файлу
    file_path = 'test_file.json'
    # Ожидаемые данные
    expected_data = [{
        "key1": "value1",
        "key2": "value2",

    }]
    actual_data = open_json_file_r(file_path)
    assert actual_data == expected_data

def test_mask_card_number():
    assert mask_card_number('1596837868705199') == 'XXXX XX** **** 5199'
