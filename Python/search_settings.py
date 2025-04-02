class Settings:
    def __init__(self):
        self.show_budget_score = True  # Показывать баллы на бюджет или на платное
        self.show_op_only_with_budget = True

        self.filter_by_score = False
        self.min_average_score = 0 # Минимальный средний проходной балл за ОДИН предмет.
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
