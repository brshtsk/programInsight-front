from data_manipulations import DataManipulations
from search_settings import Settings


class Op:
    def __init__(self, name, university, exams_amount, op_type, budget_ege_score, budget_places_amount,
                 paid_ege_score, paid_places_amount, cost, city, length, attendance, exams, raex_position):
        if type(name) is not str:
            raise TypeError("name должно быть строкой")
        self.name = name  # Название образовательной программы

        if type(university) is not str:
            raise TypeError("university должно быть строкой")
        self.university = university  # Университет

        if type(exams_amount) is not int and exams_amount is not None:
            raise TypeError("exams_amount должно быть целым числом или None")
        if exams_amount <= 0:
            raise ValueError("exams_amount должно быть больше 0")
        self.exams_amount = exams_amount  # Количество экзаменов (3/None)

        if type(op_type) is not str:
            raise TypeError("op_type должно быть строкой")
        self.op_type = op_type  # Тип программы ('Бакалавриат'/'Специалитет'/'Магистратура')

        if type(budget_ege_score) is not int and budget_ege_score is not None:
            raise TypeError("budget_ege_score должно быть целым числом или None")
        self.budget_ege_score = budget_ege_score  # Проходной балл на бюджет (234/None)

        if type(budget_places_amount) is not int and budget_places_amount is not None:
            raise TypeError("budget_places_amount должно быть целым числом или None")
        self.budget_places_amount = budget_places_amount  # Количество бюджетных мест (50/None)

        if type(paid_ege_score) is not int and paid_ege_score is not None:
            raise TypeError("paid_ege_score должно быть целым числом или None")
        self.paid_ege_score = paid_ege_score  # Проходной балл на платное (123/None)

        if type(paid_places_amount) is not int and paid_places_amount is not None:
            raise TypeError("paid_places_amount должно быть целым числом или None")
        self.paid_places_amount = paid_places_amount  # Количество платных мест (40/None)

        if type(cost) is not int and cost is not None:
            raise TypeError("cost должно быть целым числом или None")
        self.cost = cost  # Стоимость обучения 730000/None

        if type(city) is not str and city is not None:
            raise TypeError("city должно быть строкой или None")
        self.city = city  # Город, где находится университет 'Москва'/None

        if type(length) is not str and length is not None:
            raise TypeError("length должно быть строкой или None")
        self.length = length  # Длина программы ("4 года"/None)

        if type(attendance) is not str and attendance is not None:
            raise TypeError("attendance должно быть строкой или None")
        self.attendance = attendance  # Форма обучения ('Очная'/None)

        if type(exams) is not list and exams is not None:
            raise TypeError("exams должно быть списком или None")
        self.exams = exams  # Список экзаменов ([['математика'], ['физика', 'химия'], ['информатика']]/None)

        if type(raex_position) is not int and raex_position is not None:
            raise TypeError("raex_position должно быть целым числом или None")
        self.raex_position = raex_position  # Позиция в рейтинге RAEX (1/None)

    def to_model_dict(self, settings=Settings()) -> dict:
        """
        Создает словарь с информацией об объекте для op_model
        :return:
        """

        show_budget_score = settings.show_budget_score

        def score_to_str(score):
            if score is None:
                return '-'
            return str(score)

        if self.cost is None:
            cost_text = '-'
        else:
            cost_text = f"{self.cost // 1000}к ₽"

        single_exams = []
        choice_exams = []

        for exam in self.exams:
            if len(exam) == 1:
                single_exams.append(exam[0])
            else:
                choice_exams.append(exam)

        op_dict = {
            "opNameText": DataManipulations.split_line(self.name),
            "info1Text": score_to_str(self.budget_ege_score) if show_budget_score else score_to_str(
                self.paid_ege_score),
            "info2Text": cost_text,
            "universityNameText": self.university if len(self.university) <= 20 else DataManipulations.cut_extra(
                self.university),
            "opCodeText": self.op_type,
            "imageSource": DataManipulations.get_image_source(self.university),
            "lengthText": self.length,
            "locationText": self.city,
            "attendanceText": self.attendance,
            "raexPosition": self.raex_position,
            "budgetScore": self.budget_ege_score,
            "paidScore": self.paid_ege_score,
            "budgetPlaces": self.budget_places_amount,
            "paidPlaces": self.paid_places_amount,
            "singleExams": single_exams,
            "choiceExams": choice_exams,
            "fullUniversityNameText": DataManipulations.split_line(self.university),
        }
        return op_dict

    def suits(self, settings=Settings()) -> bool:
        """
        Показывает, нужно ли отображать данное ОП при указанных настройках
        :param settings:
        :return:
        """
        if settings.city_name:
            if settings.city_name.lower() != self.city.lower():
                return False

        if settings.op_name:
            if settings.op_name.lower() != self.name.lower():
                return False

        if settings.university_name:
            if settings.university_name.lower() not in self.university.lower():
                return False

        if self.op_type not in settings.qualifications:
            return False

        if settings.filter_by_score:
            if not self.exams_amount:
                return False

            if settings.show_budget_score:
                if not self.budget_ege_score:
                    return False
                average_budget_score = self.budget_ege_score / self.exams_amount

                if not self.budget_ege_score:
                    return False
                return settings.min_average_score <= average_budget_score <= settings.max_average_score
            else:
                if not self.paid_ege_score:
                    return False
                average_paid_score = self.paid_ege_score / self.exams_amount

                if not self.paid_ege_score:
                    return False
                return settings.min_average_score <= average_paid_score <= settings.max_average_score

        if settings.show_op_only_with_budget:
            if self.budget_ege_score:
                return True
            else:
                return False

        if settings.filter_by_price and settings.price_range_is_ok() and self.cost:
            return settings.min_price <= self.cost <= settings.max_price

        if not self.cost:
            return False
        return True
