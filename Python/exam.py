from unique_values import UniqueValues


class Exam:
    """
    Класс, представляющий экзамен, который пользователь указал в списке предметов.
    """

    def __init__(self, name, qualification, score, unique_values: UniqueValues):
        if type(name) is not str:
            raise TypeError("name должно быть строкой")
        self.name = name  # Название экзамена ("математика", "физика"...)

        if type(qualification) is not str:
            raise TypeError("qualification должно быть строкой")
        if qualification not in ["ЕГЭ/ДВИ", "Доп баллы ЕГЭ", "Магистратура"]:
            raise ValueError("qualification должно быть 'ЕГЭ/ДВИ', 'Доп баллы ЕГЭ' или 'Магистратура'")
        self.qualification = qualification  # Квалификация ("ЕГЭ/ДВИ", "Доп баллы ЕГЭ", "Магистратура")

        if type(score) is not int and score is not None:
            raise TypeError("score должно быть целым числом или None")
        if type(score) is int:
            if score < 0:
                raise ValueError("score должно быть больше 0")
            # Если это ЕГЭ/ДВИ, то score не больше 100
            if qualification == "ЕГЭ/ДВИ" and score > 100:
                raise ValueError("score для ЕГЭ/ДВИ должно быть меньше 100")
            # Если это Магистратура, то score не больше 999
            if qualification == "Магистратура" and score > 999:
                raise ValueError("score для Магистратуры должно быть меньше 999")
            # Если это Доп баллы ЕГЭ, то score не больше 10
            if qualification == "Доп баллы ЕГЭ" and score > 10:
                raise ValueError("score для Доп баллов ЕГЭ должно быть меньше 10")
        self.score = score

        # Если экзамена с таким названием и типом нет в unique_values, значит его не существует
        if self.qualification == "ЕГЭ/ДВИ":
            exists = False
            for real_exam in unique_values.subjects_bak_or_spec:
                if self.name.lower() == real_exam.lower():
                    self.name = real_exam
                    exists = True
                    break
            if not exists:
                raise ValueError(f"Экзамен '{self.name}' не существует.")
        if self.qualification == "Магистратура":
            exists = False
            for real_exam in unique_values.subjects_mag:
                if self.name.lower() == real_exam.lower():
                    self.name = real_exam
                    exists = True
                    break
            if not exists:
                raise ValueError(f"Экзамен '{self.name}' не существует.")


class UserExamsSet:
    """
    Класс, представляющий набор экзаменов, который пользователь указал в списке предметов.
    """

    def __init__(self):
        self.exams = []

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
            })

        return d

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
