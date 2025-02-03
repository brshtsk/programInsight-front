from data_manipulations import split_line, cut_extra, get_image_source
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
            "opNameText": split_line(self.name),
            "info1Text": score_to_str(self.budget_ege_score) if show_budget_score else score_to_str(
                self.paid_ege_score),
            "info2Text": f"{self.cost // 1000}к ₽",
            "universityNameText": self.university if len(self.university) <= 20 else cut_extra(self.university),
            "opCodeText": self.op_type,
            "imageSource": get_image_source(self.university)
        }
        return op_dict


class Statistics:
    def __init__(self):
        self.op_amount = 0
        self.have_budget = 0  # Количество ОП с бюджетными местами

        self.sum_price = 0  # Общая сумма стоимости обучения
        self.sum_budget_places = 0  # Общее количество бюджетных мест
        self.sum_paid_places = 0  # Общее количество платных мест

        self.sum_budget_ege_scores = 0  # Суммарный проходной балл на бюджет
        self.sum_paid_ege_scores = 0  # Суммарный проходной балл на платное

        self.sum_budget_ege_subjects = 0  # Количество предметов ЕГЭ для бюджета
        self.sum_paid_ege_subjects = 0  # Количество предметов ЕГЭ для платного

    def add(self, op: Op) -> None:
        """
        Засчитывает новую ОП в статистику
        :param op:
        :return:
        """
        self.op_amount += 1
        if op.budget_ege_score:
            self.have_budget += 1
            self.sum_budget_places += op.budget_places_amount
            self.sum_budget_ege_scores += op.budget_ege_score
            self.sum_budget_ege_subjects += op.exams_amount
        self.sum_price += op.cost
        self.sum_paid_places += op.paid_places_amount
        self.sum_paid_ege_scores += op.paid_ege_score
        self.sum_paid_ege_subjects += op.exams_amount

    def to_model_dict(self, settings=Settings()) -> dict:
        """
        Создает словарь с информацией о статистике для statistics_model
        :return:
        """

        show_budget_score = settings.show_budget_score

        def get_average_score():
            if show_budget_score:
                return self.sum_budget_ege_scores / self.sum_budget_ege_subjects
            return self.sum_paid_ege_scores / self.sum_paid_ege_subjects

        statistics_data = [
            {
                "statisticTypeText": "Средний балл ЕГЭ",
                "imageSource": "resources/pencil-plain.png",
                "statisticProgressText": str(round(get_average_score(), 1)),
                "progress": get_average_score() / 100
            },
            {
                "statisticTypeText": "Средняя стоимость (тыс. ₽)",
                "imageSource": "resources/money.png",
                "statisticProgressText": str(round(self.sum_price / self.op_amount / 1000)),
                "progress": 1.0
            },
            {
                "statisticTypeText": "Среднее количество мест",
                "imageSource": "resources/people.png",
                "statisticProgressText": str(round(self.sum_budget_places / self.have_budget)),
                "progress": 1.0
            },
            {
                "statisticTypeText": "С бюджетными местами",
                "imageSource": "resources/cap.svg",
                "statisticProgressText": f"{round(self.have_budget / self.op_amount * 100)}%",
                "progress": self.have_budget / self.op_amount
            }
        ]
        return statistics_data
