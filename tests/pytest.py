from utils.functions import open_json_file_r


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
