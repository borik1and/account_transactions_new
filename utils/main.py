import os
from utils.functions import mask_account_number
from utils.functions import mask_card_number
from utils.functions import open_json_file_r

database_user = os.path.expanduser('~/account_transactions/operations.json')
operations_data = open_json_file_r(database_user)

# Фильтрация и сортировка операций
executed_operations = [operation for operation in operations_data if operation.get('state') == 'EXECUTED']
sorted_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)

# Выбор последних 5 операций
latest_operations = sorted_operations[:5]

# Форматирование и вывод операций
for operation in latest_operations:
    date = operation['date'].split('T')[0]
    description = operation['description']
    from_account = mask_card_number(operation.get('from', ''))
    to_account = mask_account_number(operation['to'])
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']

    formatted_operation = f"{date} {description}\n{from_account} -> {to_account}\n{amount} {currency}\n"

    print(formatted_operation)
