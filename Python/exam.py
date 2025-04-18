from typing import List


class Exam:
    """
    Класс, представляющий экзамен, который пользователь указал в списке предметов.
    """

    def __init__(self, name, qualification, score, subjects_bak_or_spec: List[str], subjects_mag: List[str]):
        # Проверки типов
        if not isinstance(name, str):
            raise TypeError("name должно быть строкой")

        if not isinstance(qualification, str):
            raise TypeError("qualification должно быть строкой")

        # Проверка квалификации
        valid_qualifications = ["ЕГЭ/ДВИ", "Доп баллы ЕГЭ", "Магистратура"]
        if qualification not in valid_qualifications:
            raise ValueError(f"qualification должно быть одним из значений: {', '.join(valid_qualifications)}")

        # Проверка баллов
        max_scores = {"ЕГЭ/ДВИ": 100, "Доп баллы ЕГЭ": 10, "Магистратура": 999}

        if score is not None:
            if not isinstance(score, int):
                raise TypeError("score должно быть целым числом или None")
            if score < 0:
                raise ValueError("score должно быть больше 0")
            if score > max_scores[qualification]:
                raise ValueError(f"score для {qualification} должно быть меньше {max_scores[qualification]}")

        # Сохраняем базовые свойства
        self.qualification = qualification
        self.score = score

        # Проверка и нормализация названия экзамена
        if qualification == "ЕГЭ/ДВИ":
            self._verify_exam_exists(name, subjects_bak_or_spec)
        elif qualification == "Магистратура":
            self._verify_exam_exists(name, subjects_mag)
        else:  # "Доп баллы ЕГЭ" - проверка не требуется
            self.name = name

    def _verify_exam_exists(self, name, exam_list):
        """Вспомогательный метод для проверки существования экзамена в списке."""
        for real_exam in exam_list:
            if name.lower() == real_exam.lower():
                self.name = real_exam  # Нормализуем название
                return

        raise ValueError(f"Экзамен '{name}' не существует.")


class UserExamsSet:
    """
    Класс, представляющий набор экзаменов, который пользователь указал в списке предметов.
    """

    def __init__(self, parent_nickname: str):
        self.exams = []
        if parent_nickname not in ["settings", "cabinet"]:
            raise ValueError("parent_nickname должно быть 'settings' или 'cabinet'")
        self.parent_nickname = parent_nickname

    def add_exam(self, exam: Exam):
        """
        Добавляет экзамен в список экзаменов.
        :param exam: Экзамен
        :return:
        """
        if not isinstance(exam, Exam):
            raise TypeError("exam должно быть экземпляром класса Exam")

        # Если в UserExamsSet уже есть экзамен с таким названием и типом, не добавляем
        for existing_exam in self.exams:
            if existing_exam.name == exam.name and existing_exam.qualification == exam.qualification:
                raise ValueError(f"Экзамен '{exam.name}' типа '{exam.qualification}' уже добавлен.")

        # Если все проверки прошли, добавляем экзамен в список
        self.exams.append(exam)

    def to_model_dict(self) -> list[dict]:
        """
        Создает словарь с информацией об экзаменах для модели exams
        :return:
        """
        d = []

        for exam in self.exams:
            d.append({
                'examNameText': exam.name,
                'examTypeText': exam.qualification,
                'scoreText': exam.score if exam.score is not None else '-',
                'parent': self.parent_nickname
            })

        return d

    def load_from_model_dict(self, data: list[dict]):
        """
        Загружает экзамены из словаря в список экзаменов.
        :param data: Словарь с данными об экзаменах
        :return:
        """
        self.exams = []  # Очищаем текущий список экзаменов

        for exam_data in data:
            exam = Exam(
                name=exam_data['examNameText'],
                qualification=exam_data['examTypeText'],
                score=exam_data['scoreText'] if exam_data['scoreText'] != '-' else None,
                subjects_bak_or_spec=[exam_data['examNameText']],
                subjects_mag=[exam_data['examNameText']]
            )
            self.add_exam(exam)

    def delete_exam(self, exam_name, exam_type):
        """
        Удаляет экзамен из списка экзаменов.
        :param exam_name: Название экзамена
        :param exam_type: Тип экзамена
        :return:
        """
        for exam in self.exams:
            if exam.name == exam_name and exam.qualification == exam_type:
                self.exams.remove(exam)
                return

    def __iter__(self):
        """
        Возвращает итератор для перебора экзаменов.
        """
        return iter(self.exams)
