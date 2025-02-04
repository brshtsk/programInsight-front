import json
from statistics import Statistics
from op import Op
from search_settings import Settings


def get_op_data(file_name: str) -> list[Op]:
    """
    Получение объектов ОП из файла
    :param file_name: json-файл
    :return: список с объектами ОП
    """
    with open(file_name, encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    data = []

    for university in json_data:
        for op_name in json_data[university]:
            if type(json_data[university][op_name]) is dict:
                op_data = json_data[university][op_name]
                op_type = op_data['Квалификация']
                exams_amount = None
                budget_ege_score = None
                budget_places_amount = None
                paid_ege_score = None
                paid_places_amount = None
                cost = None
                city = None

                if op_type in ['Бакалавриат', 'Специалитет']:
                    exams_amount = len(op_data['Предметы ЕГЭ 1'])
                    for postup_data in op_data['Варианты поступления'].values():
                        if 'нет' not in postup_data['Бюджет']:
                            for budget_info in postup_data['Бюджет']:
                                if 'балл' in budget_info:
                                    budget_ege_score = postup_data['Бюджет'][budget_info]
                                if 'мест' in budget_info:
                                    budget_places_amount = postup_data['Бюджет'][budget_info]
                        if 'нет' not in postup_data['Платное']:
                            for budget_info in postup_data['Платное']:
                                if 'балл' in budget_info:
                                    paid_ege_score = postup_data['Платное'][budget_info]
                                if 'мест' in budget_info:
                                    paid_places_amount = postup_data['Платное'][budget_info]
                                if 'Стоимость' in budget_info:
                                    cost = postup_data['Платное'][budget_info]

                elif op_type == 'Магистратура':
                    continue
                    # ToDo
                else:
                    print(f'Не распознана квалификация для {op_name} : {op_type}')

                data.append(Op(op_name, university, exams_amount, op_type, budget_ege_score, budget_places_amount,
                               paid_ege_score, paid_places_amount, cost, city))

    return data


def get_op_model_data(op_list: list[Op], settings=Settings()) -> (list[dict], list[dict]):
    """
    Создает данные для модели ОП и статистики
    :param op_list: список с объектами ОП
    :param settings: объект настроек
    :return: данные для модели ОП, данные для модели статистики
    """
    statistics = Statistics()

    op_model_data = []
    for op in op_list:
        if op.suits(settings):
            op_model_data.append(op.to_model_dict(settings))
            statistics.add(op)

    statistics_model_data = statistics.to_model_dict(settings)

    return op_model_data, statistics_model_data
