import json
from statistics import Statistics
from op import Op
from search_settings import Settings


class ModelDataManagement:
    def get_op_data(file_name: str) -> list[Op]:
        """
        Получение объектов ОП из файла
        :param file_name: json-файл
        :return: список с объектами ОП
        """
        with open(file_name, encoding='utf-8') as json_file:
            json_data = json.load(json_file)

        data = []

        # ToDo: парсинг RAEX

        # Множество всех существующих предметов
        subjects_bak_or_spec = set()
        subjects_mag = set()
        # ОП с ошибками
        bad_ops = set()

        for university in json_data:
            for op_name in json_data[university]['Бакалавриат и специалитет']:
                try:
                    op_data = json_data[university]['Бакалавриат и специалитет'][op_name]
                    op_type = op_data['Квалификация']
                    exams_amount = None
                    budget_ege_score = None
                    budget_places_amount = None
                    paid_ege_score = None
                    paid_places_amount = None
                    cost = None
                    city = None
                    length = None
                    attendance = None
                    exams = None
                    raex_position = None

                    exams_amount = len(op_data['Предметы ЕГЭ 1'])
                    city = op_data['Город']
                    length = op_data['Срок обучения']
                    attendance = op_data['Форма обучения']

                    if exams_amount == 0:
                        raise Exception("Нет экзаменов")

                    exams = []
                    for exam_var in op_data['Предметы ЕГЭ 1']:
                        this_var = []
                        for exam in exam_var:
                            this_var.append(exam)
                            subjects_bak_or_spec.add(exam)
                        exams.append(this_var)

                    for postup_data in op_data['Варианты поступления'].values():
                        if 'нет' not in postup_data['Бюджет'] and type(postup_data['Бюджет']) is dict:
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

                    data.append(Op(op_name, university, exams_amount, op_type, budget_ege_score, budget_places_amount,
                                   paid_ege_score, paid_places_amount, cost, city, length, attendance, exams,
                                   raex_position))
                    # print(f"Получена ОП: {op_name} в {university}")
                except:
                    # print(f"Ошибка при обработке ОП: {op_name} в {university}")
                    bad_ops.add(("Бакалавриат/Специалитет", op_name))

            for op_name in json_data[university]['Магистратура']:
                try:
                    op_data = json_data[university]['Магистратура'][op_name]
                    op_type = op_data['Квалификация']
                    exams_amount = None
                    budget_ege_score = None
                    budget_places_amount = None
                    paid_ege_score = None
                    paid_places_amount = None
                    cost = None
                    city = None
                    length = None
                    attendance = None
                    exams = None
                    raex_position = None

                    exams_amount = len(op_data['Вступительные 1'])
                    city = op_data['Город']
                    length = op_data['Срок обучения']
                    attendance = op_data['Форма обучения']

                    if exams_amount == 0:
                        raise Exception("Нет экзаменов")

                    exams = []
                    for exam_var in op_data['Вступительные 1']:
                        this_var = []
                        for exam in exam_var:
                            this_var.append(exam)
                            subjects_mag.add(exam)
                        exams.append(this_var)

                    for postup_data in op_data['Варианты поступления'].values():
                        if 'нет' not in postup_data['Бюджет'] and type(postup_data['Бюджет']) is dict:
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

                    data.append(Op(op_name, university, exams_amount, op_type, budget_ege_score, budget_places_amount,
                                   paid_ege_score, paid_places_amount, cost, city, length, attendance, exams,
                                   raex_position))
                    # print(f"Получена ОП: {op_name} в {university}")
                except:
                    # print(f"Ошибка при обработке ОП: {op_name} в {university}")
                    bad_ops.add(("Магистратура", op_name))

        print(f"Количество ОП с ошибками: {len(bad_ops)}")
        print(f"Ошибки: {bad_ops}")

        print()

        print(f"Количество уникальных предметов на бакалавриат/специалитет: {len(subjects_bak_or_spec)}")
        print(f"Предметы на бакалавриат/специалитет: {subjects_bak_or_spec}")

        print()

        print(f"Количество уникальных предметов на магистратуру: {len(subjects_mag)}")
        print(f"Предметы на магистратуру: {subjects_mag}")

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
