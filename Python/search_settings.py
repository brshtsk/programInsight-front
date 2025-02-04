class Settings:
    def __init__(self):
        self.show_budget_score = True  # Показывать баллы на бюджет или на платное
        self.show_op_only_with_budget = False
        self.filter_by_price = False
        self.min_price = 0
        self.max_price = 100000000

    def price_range_is_ok(self):
        return self.min_price <= self.max_price
