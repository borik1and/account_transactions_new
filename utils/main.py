import os

from utils.functions import process_operations, open_json_file_r

database_user = os.path.expanduser('~/account_transactions/operations.json')
operations_data = open_json_file_r(database_user)

formatted_operations = process_operations(operations_data)
for i, operation in enumerate(formatted_operations, start=1):
    print(operation)
