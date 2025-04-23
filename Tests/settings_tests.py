import sys
import types
import pytest

# Подменяем модуль exam
sys.modules['exam'] = types.SimpleNamespace(UserExamsSet=lambda ctx: [])

from search_settings import Settings

# Тесты для класса Settings
class TestSettings:
    def test_default_values(self):
        s = Settings()
        # Флаги
        assert s.show_budget_score is True
        assert s.show_op_only_with_budget is True
        assert s.filter_by_score is False

        # Диапазоны по умолчанию
        assert s.min_average_score == 0
        assert s.max_average_score == 100_000_000
        assert s.min_price == 0
        assert s.max_price == 100_000_000

        # Фильтры по цене
        assert s.filter_by_price is False
        assert s.user_chose_filter_by_price is False

        # Квалификации и прочие поля
        assert s.qualifications == ['Бакалавриат']
        assert s.city_name is None
        assert s.op_name is None
        assert s.university_name is None

        # exams подменённый в виде списка
        assert isinstance(s.exams, list)

        assert s.filter_by_exams_not_score is False
        assert s.filter_by_exams_and_score is False

        # Сортировка
        assert s.sort_by == 'default'
        assert s.sort_from_high_to_low is True

        # Обучение и кластеры
        assert s.attendance is None
        assert s.filter_by_cluster is False
        assert s.cluster_urls == []

    def test_price_range_is_ok(self):
        s = Settings()
        # корректный диапазон
        assert s.price_range_is_ok() is True

        # перекошенный диапазон
        s.min_price = 500
        s.max_price = 100
        assert s.price_range_is_ok() is False

    def test_set_settings_for_budget_resets_price_filter(self):
        s = Settings()
        # эмулируем предыдущие значения
        s.user_chose_filter_by_price = True
        s.filter_by_price = True
        s.show_budget_score = False
        s.show_op_only_with_budget = False

        s.set_settings_for_budget()

        # Переключено на бюджетный режим
        assert s.show_budget_score is True
        assert s.show_op_only_with_budget is True
        # filter_by_price сброшен, user_chose_filter_by_price сохраняется
        assert s.filter_by_price is False
        assert s.user_chose_filter_by_price is True

    def test_set_settings_for_paid_applies_user_choice(self):
        s = Settings()
        # по умолчанию user_chose_filter_by_price == False
        s.set_settings_for_paid()
        assert s.show_budget_score is False
        assert s.show_op_only_with_budget is False
        assert s.filter_by_price is False

        # если пользователь заранее выбрал фильтр по цене
        s.user_chose_filter_by_price = True
        s.set_settings_for_paid()
        assert s.show_budget_score is False
        assert s.show_op_only_with_budget is False
        assert s.filter_by_price is True

    @pytest.mark.parametrize("apply_flag, initially_paid, expected_filter", [
        (True, True, True),    # платный режим + apply=True -> filter_by_price=True
        (False, True, False),  # платный режим + apply=False -> filter_by_price=False
        (True, False, False),  # бюджетный режим игнорирует apply -> filter_by_price=False
        (False, False, False), # бюджетный режим игнорирует apply
    ])
    def test_apply_filter_by_price_behaviour(self, apply_flag, initially_paid, expected_filter):
        s = Settings()
        # установим режим
        s.show_op_only_with_budget = not initially_paid
        # применяем
        s.apply_filter_by_price(apply_flag)
        # user_chose_filter_by_price всегда копируется
        assert s.user_chose_filter_by_price is apply_flag
        # а filter_by_price зависит от режима
        assert s.filter_by_price is expected_filter
