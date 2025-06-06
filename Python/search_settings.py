from exam import UserExamsSet


class Settings:
    def __init__(self):
        self.show_budget_score = True  # Показывать баллы на бюджет или на платное
        self.show_op_only_with_budget = True

        self.filter_by_score = False
        self.min_average_score = 0  # Минимальный средний проходной балл за ОДИН предмет.
        self.max_average_score = 100_000_000

        # filter_by_price показывает, нужно ли сейчас фильтровать ОП по цене
        # user_chose_filter_by_price показывает, выбрал ли пользователь фильтр по цене
        # Это две разные переменные, так как пользователь может выбрать фильтр по цене, но рассматривать ОП на бюджет
        # Тогда filter_by_price будет False, а user_chose_filter_by_price - True,
        # так как пользователь выбрал фильтр, но применить его нельзя
        self.filter_by_price = False
        self.user_chose_filter_by_price = False

        self.min_price = 0
        self.max_price = 100_000_000

        self.qualifications = ['Бакалавриат']

        self.city_name = None
        self.op_name = None
        self.university_name = None

        self.exams = UserExamsSet('settings')  # Экзамены, которые указал пользователь

        # Фильтры для работы с вариантами обработки экзаменов: "Выключен", "Включен, без баллов", "Включен, с баллами"
        self.filter_by_exams_not_score = False  # Фильтровать по экзаменам вне зависимости от баллов
        self.filter_by_exams_and_score = False  # Фильтровать по экзаменам и баллам одновременно

        # Способы сортировки
        self.sort_by = "default"  # Принимает значения:
        # "default" - без сортировки, "raex" - по рейтингу RAEX, "price" - по цене,
        # "ege_score" - по проходному баллу на бюджет или платное (в зависимости от show_budget_score)

        self.sort_from_high_to_low = True  # Сортировать от большего к меньшему или наоборот

        self.attendance = None  # Форма обучения (None/"Очная"/"Заочная"/...)

        self.filter_by_cluster = False  # Фильтровать по кластерам
        self.cluster_urls = []  # Список URL-адресов кластеров, которые нужно отобразить

    def price_range_is_ok(self):
        return self.min_price <= self.max_price

    def set_settings_for_budget(self):
        """
        Устанавливает настройки для отображения только бюджетных мест
        :return:
        """
        self.show_budget_score = True
        self.show_op_only_with_budget = True
        self.filter_by_price = False

    def set_settings_for_paid(self):
        """
        Устанавливает настройки для отображения только платных мест
        :return:
        """
        self.show_budget_score = False
        self.show_op_only_with_budget = False
        self.filter_by_price = self.user_chose_filter_by_price

    def apply_filter_by_price(self, apply: bool):
        self.user_chose_filter_by_price = apply
        if not self.show_op_only_with_budget:
            self.filter_by_price = apply
