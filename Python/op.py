from data_manipulations import DataManipulations
from search_settings import Settings


class Op:
    def __init__(self, name, university, exams_amount, op_type, budget_ege_score, budget_places_amount,
                 paid_ege_score, paid_places_amount, cost, city):
        self.name = name  # Название образовательной программы
        self.university = university  # Университет

        self.exams_amount = exams_amount  # Количество экзаменов (3/None)
        self.op_type = op_type  # Тип программы ('Бакалавриат'/'Специалитет'/'Магистратура')

        self.budget_ege_score = budget_ege_score  # Проходной балл на бюджет (234/None)
        self.budget_places_amount = budget_places_amount  # Количество бюджетных мест (50/None)

        self.paid_ege_score = paid_ege_score  # Проходной балл на платное (123/None)
        self.paid_places_amount = paid_places_amount  # Количество платных мест (40/None)

        self.cost = cost  # Стоимость обучения 730000/None
        self.city = city  # Город, где находится университет 'Москва'/None

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

        op_dict = {
            "opNameText": DataManipulations.split_line(self.name),
            "info1Text": score_to_str(self.budget_ege_score) if show_budget_score else score_to_str(
                self.paid_ege_score),
            "info2Text": f"{self.cost // 1000}к ₽",
            "universityNameText": self.university if len(self.university) <= 20 else DataManipulations.cut_extra(
                self.university),
            "opCodeText": self.op_type,
            "imageSource": DataManipulations.get_image_source(self.university)
        }
        return op_dict

    def suits(self, settings=Settings()) -> bool:
        """
        Показывает, нужно ли отображать данное ОП при указанных настройках
        :param settings:
        :return:
        """
        if settings.show_op_only_with_budget:
            if self.budget_ege_score:
                pass
            else:
                return False
        if settings.filter_by_price and settings.price_range_is_ok():
            return settings.min_price <= self.cost <= settings.max_price
        return True
