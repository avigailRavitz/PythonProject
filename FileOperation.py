import pandas as pd
import sys
from datetime import datetime


class FileOperation:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'Hi in FileOperator, {self.name}')

    def read_excel(self, file_path: str):
        try:
            data = pd.read_csv(file_path)
            return data
        except FileNotFoundError:
            self.handle_error()
            print(f"Error: File '{file_path}' not found.")
            print("Chani & Avigail")
            return None

    def save_to_csv(self, data, file_name: str):
        try:
            df = pd.DataFrame(data)
            df.to_csv(file_name, mode='a', index=False, header=False)  # הוספת
            print(f"Data successfully saved to {file_name}")
            return True
        except FileNotFoundError:
            self.handle_error()
            print(f"Error: File '{file_name}' not found.")
            print("Chani & Avigail")
            return None

    def handle_error(self):
        exc_type, exc_value, exc_traceback = sys.exc_info()
        error_message = f"<{datetime.now()} - Chani & Avigail - {exc_type.__name__}: {exc_value}>"
        print(error_message)
