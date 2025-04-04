from data_manipulations import DataManipulations
from search_settings import Settings
from typing import Optional, List


class Op:
    def __init__(self,
                 name: str,
                 university: str,
                 exams_amount: Optional[int],
                 op_type: str,
                 budget_ege_score: Optional[int],
                 budget_places_amount: Optional[int],
                 paid_ege_score: Optional[int],
                 paid_places_amount: Optional[int],
                 cost: Optional[int],
                 city: Optional[str],
                 length: Optional[List[float]],
                 attendance: Optional[List[str]],
                 exams: Optional[List[str]],
                 raex_position: Optional[int]):
        # Проверка типа строки через isinstance
        if not isinstance(name, str):
            raise TypeError("name должно быть строкой")
        self.name = name

        if not isinstance(university, str):
            raise TypeError("university должно быть строкой")
        self.university = university

        # Проверка типа числа или None
        if exams_amount is not None and not isinstance(exams_amount, int):
            raise TypeError("exams_amount должно быть целым числом или None")
        if exams_amount is not None and exams_amount <= 0:
            raise ValueError("exams_amount должно быть больше 0")
        self.exams_amount = exams_amount

        if not isinstance(op_type, str):
            raise TypeError("op_type должно быть строкой")
        self.op_type = op_type

        if budget_ege_score is not None and not isinstance(budget_ege_score, int):
            raise TypeError("budget_ege_score должно быть целым числом или None")
        self.budget_ege_score = budget_ege_score

        if budget_places_amount is not None and not isinstance(budget_places_amount, int):
            raise TypeError("budget_places_amount должно быть целым числом или None")
        self.budget_places_amount = budget_places_amount

        if paid_ege_score is not None and not isinstance(paid_ege_score, int):
            raise TypeError("paid_ege_score должно быть целым числом или None")
        self.paid_ege_score = paid_ege_score

        if paid_places_amount is not None and not isinstance(paid_places_amount, int):
            raise TypeError("paid_places_amount должно быть целым числом или None")
        self.paid_places_amount = paid_places_amount

        if cost is not None and not isinstance(cost, int):
            raise TypeError("cost должно быть целым числом или None")
        self.cost = cost

        if city is not None and not isinstance(city, str):
            raise TypeError("city должно быть строкой или None")
        self.city = city

        if length is not None and not isinstance(length, list):
            raise TypeError("length должно быть списком float или None")
        self.length = length

        if attendance is not None and not isinstance(attendance, list):
            raise TypeError("attendance должно быть списком строк или None")
        self.attendance = attendance

        if exams is not None and not isinstance(exams, list):
            raise TypeError("exams должно быть списком строк или None")
        self.exams = exams

        if raex_position is not None and not isinstance(raex_position, int):
            raise TypeError("raex_position должно быть целым числом или None")
        self.raex_position = raex_position

        # Дополнительные проверки:
        # Если некоторые данные о бюджетных местах отсутствуют, все они должны отсутствовать.
        if [self.budget_places_amount, self.budget_ege_score].count(None) not in [0, 2]:
            self.budget_places_amount = None
            self.budget_ege_score = None

        # Если некоторые данные о платных местах отсутствуют, все они должны отсутствовать.
        if [self.paid_places_amount, self.paid_ege_score, self.cost].count(None) not in [0, 3]:
            self.paid_places_amount = None
            self.paid_ege_score = None
            self.cost = None

        # Если нет данных ни о бюджетных, ни о платных местах, такой ОП не подходит.
        if self.budget_places_amount is None and self.paid_places_amount is None:
            raise ValueError("Недостаточно данных о бюджетных и платных местах")

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
            "lengthText": "Срок обучения (лет): " + "; ".join(
                map(str, DataManipulations.suitable_floats_to_int(self.length))),
            "locationText": self.city,
            "attendanceText": "; ".join(self.attendance),
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
