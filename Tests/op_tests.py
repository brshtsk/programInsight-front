import pytest
from Python.op import Op

class DummyExam:
    def __init__(self, name, qualification, score):
        self.name = name
        self.qualification = qualification
        self.score = score

class DummySettings:
    def __init__(self,
                 exams=None,
                 show_budget_score=True,
                 show_op_only_with_budget=True,
                 filter_by_exams_not_score=False,
                 filter_by_exams_and_score=False,
                 filter_by_cluster=False,
                 cluster_urls=None,
                 attendance="очное",
                 city_name="Москва",
                 op_name="Информатика",
                 university_name="МГУ",
                 filter_by_score=False,
                 min_average_score=80,
                 max_average_score=100,
                 filter_by_price=False,
                 min_price=100000,
                 max_price=200000,
                 qualifications=None):
        self.exams = exams or []
        self.show_budget_score = show_budget_score
        self.show_op_only_with_budget = show_op_only_with_budget
        self.filter_by_exams_not_score = filter_by_exams_not_score
        self.filter_by_exams_and_score = filter_by_exams_and_score
        self.filter_by_cluster = filter_by_cluster
        self.cluster_urls = cluster_urls or []
        self.attendance = attendance
        self.city_name = city_name
        self.op_name = op_name
        self.university_name = university_name
        self.filter_by_score = filter_by_score
        self.min_average_score = min_average_score
        self.max_average_score = max_average_score
        self.filter_by_price = filter_by_price
        self.min_price = min_price
        self.max_price = max_price
        # Добавляем поддержку qualifications
        self.qualifications = qualifications or []

    def price_range_is_ok(self):
        # для тестов всегда возвращаем True
        return True

@pytest.fixture
def valid_op_params():
    return {
        "name": "Информатика",
        "university": "МГУ",
        "exams_amount": 3,
        "op_type": "Бакалавриат",
        "budget_ege_score": 170,
        "budget_places_amount": 50,
        "paid_ege_score": 140,
        "paid_places_amount": 100,
        "cost": 150000,
        "city": "Москва",
        "length": [4.0],
        "attendance": ["очное"],
        "exams": [["Математика"], ["Физика", "Химия"]],
        "raex_position": 1,
        "url": "http://example.com/op"
    }

# Тесты для класса Op
class TestOp:
    def test_op_creation_valid(self, valid_op_params):
        op = Op(**valid_op_params)
        assert op.name == "Информатика"
        assert op.university == "МГУ"
        assert op.exams_amount == 3
        assert op.op_type in ["Бакалавриат", "Специалитет", "Магистратура"]
        assert op.id > 0

    def test_op_invalid_name_type(self, valid_op_params):
        valid_op_params["name"] = 123  # неверный тип
        with pytest.raises(TypeError):
            Op(**valid_op_params)

    def test_op_missing_budget_and_paid(self, valid_op_params):
        valid_op_params["budget_places_amount"] = None
        valid_op_params["paid_places_amount"] = None
        with pytest.raises(ValueError):
            Op(**valid_op_params)

    def test_is_possible_to_pass(self, valid_op_params):
        op = Op(**valid_op_params)
        dummy_exams = [
            DummyExam("Математика", "ЕГЭ/ДВИ", 90),
            DummyExam("Физика", "ЕГЭ/ДВИ", 80),
            DummyExam("Личные достижения", "Доп баллы ЕГЭ", 5)
        ]
        settings = DummySettings(exams=dummy_exams,
                                 filter_by_exams_not_score=False,
                                 filter_by_exams_and_score=True)
        assert op.is_possible_to_pass(settings) is True

    def test_suits(self, valid_op_params):
        op = Op(**valid_op_params)
        settings = DummySettings(
            qualifications=["Бакалавриат", "Специалитет"],
            attendance="очное",
            cluster_urls=["http://example.com/op"],
            city_name="Москва",
            op_name="Информатика",
            university_name="МГУ"
        )
        class DummyUniqueValues:
            def __init__(self, lowercase_universities):
                self.lowercase_universities = lowercase_universities
        unique_values = DummyUniqueValues(lowercase_universities="мгу")
        assert op.suits(settings, unique_values) is True