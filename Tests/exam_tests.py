import pytest
from Python.exam import Exam, UserExamsSet

BAK_SPEC_SUBJECTS = ["Математика", "Физика"]
MAG_SUBJECTS = ["История", "Экономика"]


# Тесты для класса Exam
class TestExam:
    def test_exam_creation_normalization(self):
        # Проверяем нормализацию имени экзамена для квалификации "ЕГЭ/ДВИ"
        exam = Exam(
            name="математика",
            qualification="ЕГЭ/ДВИ",
            score=90,
            subjects_bak_or_spec=BAK_SPEC_SUBJECTS,
            subjects_mag=MAG_SUBJECTS
        )
        assert exam.name == "Математика"
        assert exam.qualification == "ЕГЭ/ДВИ"
        assert exam.score == 90

    def test_exam_creation_for_dop(self):
        # Для квалификации "Доп баллы ЕГЭ" нормализация не производится
        exam = Exam(
            name="Физика",
            qualification="Доп баллы ЕГЭ",
            score=8,
            subjects_bak_or_spec=BAK_SPEC_SUBJECTS,
            subjects_mag=MAG_SUBJECTS
        )
        assert exam.name == "Физика"
        assert exam.qualification == "Доп баллы ЕГЭ"
        assert exam.score == 8

    def test_exam_creation_invalid_qualification(self):
        # Неверное значение квалификации должно вызывать ValueError
        with pytest.raises(ValueError):
            Exam(
                name="Экономика",
                qualification="Неверная",
                score=50,
                subjects_bak_or_spec=BAK_SPEC_SUBJECTS,
                subjects_mag=MAG_SUBJECTS
            )

    def test_exam_score_boundaries(self):
        # Проверка верхней границы баллов для "ЕГЭ/ДВИ" (макс 100)
        with pytest.raises(ValueError):
            Exam(
                name="Математика",
                qualification="ЕГЭ/ДВИ",
                score=101,
                subjects_bak_or_spec=BAK_SPEC_SUBJECTS,
                subjects_mag=MAG_SUBJECTS
            )
        # Проверка отрицательного балла
        with pytest.raises(ValueError):
            Exam(
                name="Математика",
                qualification="ЕГЭ/ДВИ",
                score=-1,
                subjects_bak_or_spec=BAK_SPEC_SUBJECTS,
                subjects_mag=MAG_SUBJECTS
            )


# Тесты для класса UserExamsSet
class TestUserExamsSet:
    def test_add_exam_success(self):
        exams_set = UserExamsSet(parent_nickname="settings")
        exam = Exam(
            name="Математика",
            qualification="ЕГЭ/ДВИ",
            score=95,
            subjects_bak_or_spec=BAK_SPEC_SUBJECTS,
            subjects_mag=MAG_SUBJECTS
        )
        exams_set.add_exam(exam)
        assert len(list(exams_set)) == 1

    def test_add_duplicate_exam(self):
        exams_set = UserExamsSet(parent_nickname="settings")
        exam = Exam(
            name="Физика",
            qualification="ЕГЭ/ДВИ",
            score=80,
            subjects_bak_or_spec=BAK_SPEC_SUBJECTS,
            subjects_mag=MAG_SUBJECTS
        )
        exams_set.add_exam(exam)
        # Добавление экзамена с такими же именем и квалификацией должно вызывать ошибку
        with pytest.raises(ValueError):
            exams_set.add_exam(exam)

    def test_to_model_dict(self):
        exams_set = UserExamsSet(parent_nickname="cabinet")
        exam1 = Exam(
            name="Математика",
            qualification="ЕГЭ/ДВИ",
            score=90,
            subjects_bak_or_spec=BAK_SPEC_SUBJECTS,
            subjects_mag=MAG_SUBJECTS
        )
        exam2 = Exam(
            name="История",
            qualification="Магистратура",
            score=750,
            subjects_bak_or_spec=BAK_SPEC_SUBJECTS,
            subjects_mag=MAG_SUBJECTS
        )
        exams_set.add_exam(exam1)
        exams_set.add_exam(exam2)
        model = exams_set.to_model_dict()
        assert isinstance(model, list)
        assert len(model) == 2
        assert model[0]['parent'] == "cabinet"

    def test_load_from_model_dict(self):
        exams_set = UserExamsSet(parent_nickname="settings")
        data = [
            {
                "examNameText": "Математика",
                "examTypeText": "ЕГЭ/ДВИ",
                "scoreText": 88,
                "parent": "settings"
            },
            {
                "examNameText": "Физика",
                "examTypeText": "ЕГЭ/ДВИ",
                "scoreText": "-",
                "parent": "settings"
            }
        ]
        exams_set.load_from_model_dict(data)
        exams = list(exams_set)
        assert len(exams) == 2
        # score второго экзамена должен быть None, так как из "-" получается None
        assert exams[1].score is None

    def test_delete_exam(self):
        exams_set = UserExamsSet(parent_nickname="settings")
        exam = Exam(
            name="Математика",
            qualification="ЕГЭ/ДВИ",
            score=85,
            subjects_bak_or_spec=BAK_SPEC_SUBJECTS,
            subjects_mag=MAG_SUBJECTS
        )
        exams_set.add_exam(exam)
        assert len(list(exams_set)) == 1
        exams_set.delete_exam("Математика", "ЕГЭ/ДВИ")
        assert len(list(exams_set)) == 0
