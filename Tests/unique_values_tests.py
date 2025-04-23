import pytest
from Python.unique_values import UniqueValues


class DummyOp:
    def __init__(self, name, university, city, op_type, exams):
        self.name = name
        self.university = university
        self.city = city
        self.op_type = op_type
        self.exams = exams


# Тесты для класса UniqueValues
class TestUniqueValues:
    def test_add_bachelor_or_specialitet(self):
        uv = UniqueValues()
        dummy = DummyOp(
            name="Информатика",
            university="МОСКОВСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ",
            city="Москва",
            op_type="Бакалавриат",
            exams=[["Математика"], ["Физика", "Химия"]]
        )
        uv.add_op(dummy)

        # Проверяем, что названия ОП, университетов, городов добавлены
        assert uv.op_names == {"Информатика"}
        assert uv.universities == {"МОСКОВСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ"}
        assert uv.lowercase_universities == {"московский государственный университет"}
        assert uv.cities == {"Москва"}

        # Для бакалавриата и специалитета subjects_bak_or_spec содержит все предметы из exams
        expected_subjects = {"Математика", "Физика", "Химия"}
        assert uv.subjects_bak_or_spec == expected_subjects
        # subjects_mag остаётся пустым
        assert uv.subjects_mag == set()

    def test_add_magistratura(self):
        uv = UniqueValues()
        dummy = DummyOp(
            name="Экономика",
            university="ВШЭ",
            city="Санкт-Петербург",
            op_type="Магистратура",
            exams=[["Экономика"], ["Финансы"]]
        )
        uv.add_op(dummy)

        # Проверяем общие поля
        assert uv.op_names == {"Экономика"}
        assert uv.universities == {"ВШЭ"}
        assert uv.lowercase_universities == {"вшэ"}
        assert uv.cities == {"Санкт-Петербург"}

        # Для магистратуры subjects_mag содержит все предметы, бакалаврские остаются пустыми
        expected_subjects_mag = {"Экономика", "Финансы"}
        assert uv.subjects_mag == expected_subjects_mag
        assert uv.subjects_bak_or_spec == set()

    def test_adding_multiple_ops_accumulates_values(self):
        uv = UniqueValues()
        op1 = DummyOp(
            name="OP1",
            university="Uni1",
            city="City1",
            op_type="Бакалавриат",
            exams=[["A"], ["B"]]
        )
        op2 = DummyOp(
            name="OP2",
            university="Uni2",
            city="City2",
            op_type="Магистратура",
            exams=[["C"], ["D"]]
        )
        op3 = DummyOp(
            name="OP1",  # повтор имени
            university="Uni1",  # повтор университета
            city="City1",
            op_type="Бакалавриат",
            exams=[["B"], ["E"]]
        )

        uv.add_op(op1)
        uv.add_op(op2)
        uv.add_op(op3)

        # op_names уникальны
        assert uv.op_names == {"OP1", "OP2"}
        # universities
        assert uv.universities == {"Uni1", "Uni2"}
        assert uv.lowercase_universities == {"uni1", "uni2"}
        # cities
        assert uv.cities == {"City1", "City2"}

        # subjects_bak_or_spec суммирует из op1 и op3, без дубликатов
        assert uv.subjects_bak_or_spec == {"A", "B", "E"}
        # subjects_mag из op2
        assert uv.subjects_mag == {"C", "D"}
