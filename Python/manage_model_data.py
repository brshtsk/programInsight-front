import json
from statistics import Statistics
from op import Op
from search_settings import Settings
from unique_values import UniqueValues
from typing import Optional


class ModelDataManagement:
    def get_op_data(file_name: str) -> (list[Op], UniqueValues):
        """
        Получение объектов ОП из файла
        :param file_name: json-файл
        :return: список с объектами ОП, объект уникальных значений
        """
        with open(file_name, encoding='utf-8') as json_file:
            json_data = json.load(json_file)

        data = []

        unique_values = UniqueValues()

        # ToDo: искать именно вариант поступления на основе 11 классов

        # ОП с ошибками
        bad_ops = set()

        for op_data in json_data:
            op_name = op_data['Программа']
            op_type = op_data['Квалификация']

            if op_type in ['Бакалавриат', 'Специалитет']:
                try:
                    university = None
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

                    exams_amount = len(op_data['ЕГЭ'])
                    city = op_data['Город']
                    length = op_data['Срок обучения']
                    attendance = op_data['Форма обучения']
                    university = op_data['Университет']

                    if exams_amount == 0:
                        raise Exception("Нет экзаменов")

                    exams = []
                    for exam_var in op_data['ЕГЭ']:
                        this_var = []
                        for exam in exam_var:
                            this_var.append(exam)
                        exams.append(this_var)

                    # Самый популярный вариант поступления - 'Очная, на русском, Полный курс, на базе 11 классов'
                    if 'Очная, на русском, Полный курс, на базе 11 классов' in op_data:
                        postup_data = op_data['Очная, на русском, Полный курс, на базе 11 классов']
                        budget_places_amount, budget_ege_score = ModelDataManagement.parse_budget_postup_data(
                            postup_data)
                        paid_places_amount, paid_ege_score, cost = ModelDataManagement.parse_paid_postup_data(
                            postup_data)

                    # Если на вариант 'Очная, на русском, Полный курс, на базе 11 классов' нельзя поступить на бюджет,
                    # то ищем хоть какой-то вариант
                    if budget_ege_score is None and budget_places_amount is None:
                        for variant in op_data['Варианты поступления']:
                            postup_data = op_data['Варианты поступления'][variant]
                            budget_places_amount, budget_ege_score = ModelDataManagement.parse_budget_postup_data(
                                postup_data)
                            if budget_ege_score is not None and budget_places_amount is not None:
                                break

                    # Если на вариант 'Очная, на русском, Полный курс, на базе 11 классов' нельзя поступить на платное,
                    # то ищем хоть какой-то вариант
                    if paid_ege_score is None and paid_places_amount is None and cost is None:
                        for variant in op_data['Варианты поступления']:
                            postup_data = op_data['Варианты поступления'][variant]
                            paid_places_amount, paid_ege_score, cost = ModelDataManagement.parse_paid_postup_data(
                                postup_data)
                            if paid_ege_score is not None and paid_places_amount is not None and cost is not None:
                                break

                    data.append(Op(op_name, university, exams_amount, op_type, budget_ege_score, budget_places_amount,
                                   paid_ege_score, paid_places_amount, cost, city, length, attendance, exams,
                                   raex_position))
                    unique_values.add_op(data[-1])
                    # print(f"Получена ОП: {op_name} в {university}")
                except:
                    # print(f"Ошибка при обработке ОП: {op_name} в {university}")
                    bad_ops.add(("Бакалавриат/Специалитет", op_name))

            if op_type == 'Магистратура':
                try:
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

                    exams_amount = len(op_data['Вступительные'])
                    city = op_data['Город']
                    length = op_data['Срок обучения']
                    attendance = op_data['Форма обучения']

                    if exams_amount == 0:
                        raise Exception("Нет экзаменов")

                    exams = []
                    for exam_var in op_data['Вступительные']:
                        this_var = []
                        for exam in exam_var:
                            this_var.append(exam)
                        exams.append(this_var)

                    # Самый популярный вариант поступления - 'Очная, на русском, 2 года'
                    if 'Очная, на русском, 2 года' in op_data:
                        postup_data = op_data['Очная, на русском, 2 года']
                        budget_places_amount, budget_ege_score = ModelDataManagement.parse_budget_postup_data(
                            postup_data)
                        paid_places_amount, paid_ege_score, cost = ModelDataManagement.parse_paid_postup_data(
                            postup_data)

                    # Если на вариант 'Очная, на русском, 2 года' нельзя поступить на бюджет,
                    # то ищем хоть какой-то вариант
                    if budget_ege_score is None and budget_places_amount is None:
                        for variant in op_data['Варианты поступления']:
                            postup_data = op_data['Варианты поступления'][variant]
                            budget_places_amount, budget_ege_score = ModelDataManagement.parse_budget_postup_data(
                                postup_data)
                            if budget_ege_score is not None and budget_places_amount is not None:
                                break

                    # Если на вариант 'Очная, на русском, 2 года' нельзя поступить на платное,
                    # то ищем хоть какой-то вариант
                    if paid_ege_score is None and paid_places_amount is None and cost is None:
                        for variant in op_data['Варианты поступления']:
                            postup_data = op_data['Варианты поступления'][variant]
                            paid_places_amount, paid_ege_score, cost = ModelDataManagement.parse_paid_postup_data(
                                postup_data)
                            if paid_ege_score is not None and paid_places_amount is not None and cost is not None:
                                break

                    data.append(Op(op_name, university, exams_amount, op_type, budget_ege_score, budget_places_amount,
                                   paid_ege_score, paid_places_amount, cost, city, length, attendance, exams,
                                   raex_position))
                    unique_values.add_op(data[-1])
                    # print(f"Получена ОП: {op_name} в {university}")
                except:
                    # print(f"Ошибка при обработке ОП: {op_name} в {university}")
                    bad_ops.add(("Магистратура", op_name))

        print(f"Количество ОП с ошибками: {len(bad_ops)}")
        print(f"Ошибки: {bad_ops}")

        print()

        print(f"Количество уникальных предметов на бакалавриат/специалитет: {len(unique_values.subjects_bak_or_spec)}")
        print(f"Предметы на бакалавриат/специалитет: {unique_values.subjects_bak_or_spec}")

        print()

        print(f"Количество уникальных предметов на магистратуру: {len(unique_values.subjects_mag)}")
        print(f"Предметы на магистратуру: {unique_values.subjects_mag}")

        return data, unique_values

    def parse_budget_postup_data(postup_data: dict) -> (Optional[int], Optional[int]):
        """
        Парсит данные о бюджетных местах
        :return: количество мест, проходной балл
        """
        budget_places_amount = None
        budget_ege_score = None

        if 'нет' not in postup_data['Бюджет'] and type(postup_data['Бюджет']) is dict:
            for budget_info in postup_data['Бюджет']:
                if 'балл' in budget_info:
                    budget_ege_score = postup_data['Бюджет'][budget_info]
                if 'мест' in budget_info:
                    budget_places_amount = postup_data['Бюджет'][budget_info]
        return budget_places_amount, budget_ege_score

    def parse_paid_postup_data(postup_data: dict) -> (Optional[int], Optional[int], Optional[int]):
        """
        Парсит данные о платных местах
        :return: количество мест, проходной балл, стоимость
        """
        paid_places_amount = None
        paid_ege_score = None
        cost = None

        if 'нет' not in postup_data['Платное'] and type(postup_data['Платное']) is dict:
            for paid_info in postup_data['Платное']:
                if 'балл' in paid_info:
                    paid_ege_score = postup_data['Платное'][paid_info]
                if 'мест' in paid_info:
                    paid_places_amount = postup_data['Платное'][paid_info]
                if 'Стоимость' in paid_info:
                    cost = postup_data['Платное'][paid_info]
        return paid_places_amount, paid_ege_score, cost

    def sort_op_list(op_list: list[Op], settings=Settings()) -> list[Op]:
        """
        Сортирует список ОП по заданным параметрам
        :param op_list: список с объектами ОП
        :param settings: объект настроек
        :return: отсортированный список с объектами ОП
        """
        if settings.sort_by == 'raex':
            op_list.sort(key=lambda x: x.raex_position if x.raex_position else 999,
                         reverse=(not settings.sort_from_high_to_low))
            # Инвертируем, так как чем меньше позиция в RAEX, тем выше рейтинг
        elif settings.sort_by == 'price':
            op_list.sort(key=lambda x: x.cost if x.cost else 0, reverse=settings.sort_from_high_to_low)
        elif settings.sort_by == 'ege_score':
            if settings.show_budget_score:
                op_list.sort(key=lambda x: x.budget_ege_score if x.budget_ege_score else 0,
                             reverse=settings.sort_from_high_to_low)
            else:
                op_list.sort(key=lambda x: x.paid_ege_score if x.paid_ege_score else 0,
                             reverse=settings.sort_from_high_to_low)
        else:
            if not settings.sort_from_high_to_low:
                op_list.reverse()

    def get_op_model_data(op_list: list[Op], settings=Settings(), unique_values=UniqueValues()) -> (
            list[dict], list[dict]):
        """
        Создает данные для модели ОП и статистики
        :param op_list: список с объектами ОП
        :param settings: объект настроек
        :return: данные для модели ОП, данные для модели статистики
        """
        statistics = Statistics()

        # Сортируем список ОП.
        # Создаем новый список, чтобы не менять оригинальный.
        op_list = op_list.copy()
        ModelDataManagement.sort_op_list(op_list, settings)

        op_model_data = []
        for op in op_list:
            if op.suits(settings, unique_values):
                op_model_data.append(op.to_model_dict(settings))
                statistics.add(op)

        statistics_model_data = statistics.to_model_dict(settings)

        return op_model_data, statistics_model_data
