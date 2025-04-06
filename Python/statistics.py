from search_settings import Settings
from op import Op


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

        self.university_count = {}  # Сколько ОП в каждом университете

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
        if op.cost:
            self.sum_price += op.cost
            self.sum_paid_places += op.paid_places_amount
            self.sum_paid_ege_scores += op.paid_ege_score
            self.sum_paid_ege_subjects += op.exams_amount

        if op.university not in self.university_count:
            self.university_count[op.university] = 0
        self.university_count[op.university] += 1

    def to_model_dict(self, settings=Settings()) -> list[dict]:
        """
        Создает словарь с информацией о статистике для statistics_model
        :return:
        """

        show_budget_score = settings.show_budget_score

        def get_average_score():
            try:
                if show_budget_score:
                    return self.sum_budget_ege_scores / self.sum_budget_ege_subjects
                return self.sum_paid_ege_scores / self.sum_paid_ege_subjects
            except ZeroDivisionError:
                return 0

        def get_average_places_amount():
            try:
                if show_budget_score:
                    return self.sum_budget_places / self.have_budget
                return self.sum_paid_places / self.op_amount
            except ZeroDivisionError:
                return 0

        try:

            statistics_data = [
                {
                    "statisticTypeText": "Средний проходной балл",
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
                    "statisticProgressText": str(round(get_average_places_amount())),
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

        except ZeroDivisionError:

            statistics_data = [
                {
                    "statisticTypeText": "Средний проходной балл",
                    "imageSource": "resources/pencil-plain.png",
                    "statisticProgressText": "-",
                    "progress": 0
                },
                {
                    "statisticTypeText": "Средняя стоимость (тыс. ₽)",
                    "imageSource": "resources/money.png",
                    "statisticProgressText": "-",
                    "progress": 0
                },
                {
                    "statisticTypeText": "Среднее количество мест",
                    "imageSource": "resources/people.png",
                    "statisticProgressText": "-",
                    "progress": 0
                },
                {
                    "statisticTypeText": "С бюджетными местами",
                    "imageSource": "resources/cap.svg",
                    "statisticProgressText": "-",
                    "progress": 0
                }
            ]
            return statistics_data

    def get_top_3_universities(self) -> list[tuple]:
        """
        Возвращает список из 3 наиболее популярных университетов в формате (университет, количество ОП).
        Если университетов меньше 3, возвращает столько, сколько доступно.
        """
        # Сортировка словаря по значению в обратном порядке и получение первых 3 элементов
        sorted_universities = sorted(self.university_count.items(), key=lambda item: item[1], reverse=True)
        return sorted_universities[:3]

    def top_3_universities_to_model_dict(self) -> list[dict]:
        """
        Создает словарь с информацией о количестве ОП в каждо�� университете для statistics_model
        :return:
        """
        university_data = []
        sorted_universities = self.get_top_3_universities()
        for university, count in sorted_universities:
            university_data.append({
                "universityNameText": university,
                "thisOpAmountStr": str(count),
                "thisOpAmountInt": count,
                "maxOpAmountInt": sorted_universities[0][1],
            })
        return university_data
