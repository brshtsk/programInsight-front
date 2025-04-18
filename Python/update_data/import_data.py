import json

class DataImporter:
    def __init__(self, path):
        self.path = path

    def from_json_to_list_of_dicts(self):
        """
        Загружает данные из JSON файла в список словарей.
        :return: Список словарей
        """
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"Файл {self.path} не найден.")
            return []
        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON в файле {self.path}.")
            return []