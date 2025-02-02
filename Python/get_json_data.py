import json
from functools import lru_cache


def get_op_data(file_name: str) -> list[dict]:
    """
    Формат вывода: [{'Название': 'Программная инженерия', 'Университет': 'ВШЭ',
    'Квалификация': 'Бакалавриат'/'Специалитет'/'Магистратура', 'Балл бюджет': 234/None, 'Мест бюджет': 50/None,
    'Балл платное': 123, 'Мест платное': 40/None, 'Стоимость': 730000, 'Город': 'Москва'}, ...]
    :param file_name: json-файл
    :return: список словарей с информацией об ОП
    """
    with open(file_name, encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    data = []

    for university in json_data:
        for op_name in json_data[university]:
            if type(json_data[university][op_name]) is dict:
                op_data = json_data[university][op_name]

                parced_data = {'Название': op_name, 'Университет': university, 'Квалификация': op_data['Квалификация']}

                if parced_data['Квалификация'] in ['Бакалавриат', 'Специалитет']:
                    for postup_data in op_data['Варианты поступления'].values():
                        if 'нет' in postup_data['Бюджет']:
                            parced_data['Балл бюджет'] = None
                            parced_data['Мест бюджет'] = None
                        else:
                            for budget_info in postup_data['Бюджет']:
                                if 'балл' in budget_info:
                                    parced_data['Балл бюджет'] = postup_data['Бюджет'][budget_info]
                                if 'мест' in budget_info:
                                    parced_data['Мест бюджет'] = postup_data['Бюджет'][budget_info]
                        if 'нет' in postup_data['Платное']:
                            parced_data['Балл платное'] = None
                            parced_data['Мест платное'] = None
                            parced_data['Стоимость'] = None
                        else:
                            for budget_info in postup_data['Платное']:
                                if 'балл' in budget_info:
                                    parced_data['Балл платное'] = postup_data['Платное'][budget_info]
                                if 'мест' in budget_info:
                                    parced_data['Мест платное'] = postup_data['Платное'][budget_info]
                                if 'Стоимость' in budget_info:
                                    parced_data['Стоимость'] = postup_data['Платное'][budget_info]

                elif parced_data['Квалификация'] == 'Магистратура':
                    continue
                    # ToDo
                else:
                    print(f'Не распознана квалификация для {op_name} : {parced_data["Квалификация"]}')

                data.append(parced_data)

    return data


@lru_cache
def get_image_source(university_name: str) -> str:
    """
    Для названия университета возвращает расположение файла с лого
    :param university_name: str название (краткое)
    :return: str расположение
    """
    patterns = {'ВШЭ': 'resources/hselogo.svg', 'МФТИ': 'resources/mfti-logo.png'}
    default = 'resources/other-logo.svg'
    for pattern in patterns:
        if pattern in university_name:
            return patterns[pattern]
    return default


def split_op_name(op_name: str) -> str:
    """
    Добавляет html-перенос строки для 2 и более слов
    :param op_name: название ОП в 1 строку
    :return: название ОП с переносом через <br>
    """
    op_split = op_name.split()
    if len(op_split) == 1:
        return op_name
    med_idx = len(op_split) // 2
    # Исключим перенос после союзов
    if len(op_split) % 2 == 0 and len(op_split[med_idx - 1]) <= 2:
        op_split[med_idx - 1] = '<br>' + op_split[med_idx - 1]
    elif len(op_split) % 2 == 1 and len(op_split[med_idx + 1]) <= 2:
        op_split[med_idx + 1] = '<br>' + op_split[med_idx + 1]
    else:
        op_split[med_idx] = '<br>' + op_split[med_idx]
    return ' '.join(op_split)


def get_op_model_data(file_name: str) -> list[dict]:
    op_list = get_op_data(file_name)
    result_model_list = []
    for op in op_list:
        op_dict = {
            "opNameText": split_op_name(op['Название']),
            "info1Text": str(op['Балл бюджет']),
            "info2Text": f"{op['Стоимость'] // 1000}к ₽",
            "universityNameText": op['Университет'],
            "opCodeText": op['Квалификация'],
            "imageSource": get_image_source(op['Университет'])
        }
        result_model_list.append(op_dict)
    return result_model_list
