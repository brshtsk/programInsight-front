class Exam:
    """
    Класс, представляющий экзамен, который пользователь указал в списке предметов.
    """
    def __init__(self, name, qualification, score):
        if type(name) is not str:
            raise TypeError("name должно быть строкой")
        self.name = name # Название экзамена ("математика", "физика"...)

        if type(qualification) is not str:
            raise TypeError("qualification должно быть строкой")
        if qualification not in ["ЕГЭ/ДВИ", "Доп баллы ЕГЭ", "Магистратура"]:
            raise ValueError("qualification должно быть 'ЕГЭ/ДВИ', 'Доп баллы ЕГЭ' или 'Магистратура'")
        self.qualification = qualification # Квалификация ("ЕГЭ/ДВИ", "Доп баллы ЕГЭ", "Магистратура")

        if type(score) is not int and score is not None:
            raise TypeError("score должно быть целым числом или None")
        if score < 0:
            raise ValueError("score должно быть больше 0")
        self.score = score