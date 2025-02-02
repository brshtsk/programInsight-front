import json
from functools import lru_cache


def get_op_data(file_name: str) -> list[dict]:
    """
    Формат вывода: [{'Название': 'Программная инженерия', 'Университет': 'ВШЭ', 'Количество предметов ЕГЭ': 3,
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
                    parced_data['Количество предметов ЕГЭ'] = len(op_data['Предметы ЕГЭ 1'])
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


def split_line(op_name: str) -> str:
    """
    Добавляет html-перенос строки для 2 и более слов
    :param op_name: название ОП в 1 строку
    :return: название с переносом через <br>
    """
    op_split = op_name.split()
    if len(op_split) == 1:
        return op_name
    med_idx = len(op_split) // 2
    # Если строка не слишком длинная
    if len(op_name) < 35:
        # Исключим перенос после союзов
        if len(op_split) % 2 == 0 and len(op_split[med_idx - 1]) <= 2:
            med_idx -= 1
        elif len(op_split) % 2 == 1 and len(op_split[med_idx + 1]) <= 2:
            med_idx += 1
    # Если строка длинная
    else:
        left_ln = sum(map(len, op_split[:med_idx]))
        right_ln = sum(map(len, op_split[med_idx:]))
        k = 3
        while abs(right_ln - left_ln) > 8 and k != 0:
            if med_idx < 2 or med_idx > len(op_split) - 2:
                break
            if right_ln > left_ln:
                med_idx += 1
                left_ln = sum(map(len, op_split[:med_idx]))
                right_ln = sum(map(len, op_split[med_idx:]))
            else:
                med_idx -= 1
                left_ln = sum(map(len, op_split[:med_idx]))
                right_ln = sum(map(len, op_split[med_idx:]))
            k -= 1

    op_split[med_idx] = '<br>' + op_split[med_idx]
    return ' '.join(op_split)


@lru_cache
def cut_extra(university_name: str) -> str:
    """
    Добавляет на конец '...', чтобы название университета уместилось в 20 символов
    :param university_name: полная строка
    :return: название длиной не более 35 символов (лишние слова справа удалены)
    """
    name_split = university_name.split()
    idx = -1
    while sum(map(len, name_split[:idx])) > 20 and idx > 1:
        idx -= 1
    return ' '.join(name_split[:idx]) + '...'


def get_op_model_data(file_name: str) -> (list[dict], list[dict]):
    """
    Получает данные из json для загрузки в модели
    :param file_name: json для получения данных
    :param need_statistics: нужен ли список для statistics_model
    :return: данные для op_model, statistics_model
    """
    op_list = get_op_data(file_name)
    result_model_list = []
    have_budget = 0
    sum_price = 0
    sum_budget_places = 0
    sum_paid_places = 0
    sum_budget_ege_scores = 0
    sum_paid_ege_scores = 0
    sum_budget_ege_subjects = 0
    sum_paid_ege_subjects = 0
    for op in op_list:
        op_dict = {
            "opNameText": split_line(op['Название']),
            "info1Text": str(op['Балл бюджет']),
            "info2Text": f"{op['Стоимость'] // 1000}к ₽",
            "universityNameText": op['Университет'] if len(op['Университет']) <= 20 else cut_extra(op['Университет']),
            "opCodeText": op['Квалификация'],
            "imageSource": get_image_source(op['Университет'])
        }
        result_model_list.append(op_dict)

        if op['Балл бюджет']:
            have_budget += 1
            sum_budget_places += op['Мест бюджет']
            sum_budget_ege_scores += op['Балл бюджет']
            sum_budget_ege_subjects += op['Количество предметов ЕГЭ']
        sum_price += op['Стоимость']
        sum_paid_places += op['Мест платное']
        sum_paid_ege_scores += op['Балл платное']
        sum_paid_ege_subjects += op['Количество предметов ЕГЭ']

    statistics_data = [
        {
            "statisticTypeText": "Средний балл ЕГЭ",
            "imageSource": "resources/pencil-plain.png",
            "statisticProgressText": str(round(sum_budget_ege_scores / sum_budget_ege_subjects, 1)),
            "progress": sum_budget_ege_scores / sum_budget_ege_subjects / 100
        },
        {
            "statisticTypeText": "Средняя стоимость (тыс. ₽)",
            "imageSource": "resources/money.png",
            "statisticProgressText": str(round(sum_price / len(op_list) / 1000)),
            "progress": 1.0
        },
        {
            "statisticTypeText": "Среднее количество мест",
            "imageSource": "resources/people.png",
            "statisticProgressText": str(round(sum_budget_places / have_budget)),
            "progress": 1.0
        },
        {
            "statisticTypeText": "С бюджетными местами",
            "imageSource": "resources/cap.svg",
            "statisticProgressText": f"{round(have_budget / len(op_list) * 100)}%",
            "progress": have_budget / len(op_list)
        }
    ]

    return result_model_list, statistics_data
