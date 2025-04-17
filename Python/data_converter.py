import pandas as pd
from op import Op


class DataConverter:
    def list_op_to_dataframe(op_list: list[Op]) -> pd.DataFrame:
        """
        Преобразует список объектов Op в DataFrame
        :param op_list: список объектов Op
        :return: DataFrame с данными об ОП
        """
        data = []
        for op in op_list:
            data.append({
                'Программа': op.name,
                'Университет': op.university,
                'Кол-во экзаменов': op.exams_amount,
                'Квалификация': op.op_type,
                'Проходной балл на бюджет': op.budget_ege_score,
                'Кол-во бюджетных мест': op.budget_places_amount,
                'Проходной балл на платное': op.paid_ege_score,
                'Кол-во платных мест': op.paid_places_amount,
                'Стоимость (в год)': op.cost,
                'Город': op.city,
                'Срок обучения': op.length,
                'Форма обучения': op.attendance,
                'ЕГЭ': op.exams,
                'Место в топе': op.raex_position,
                'Входит в топ-100': op.raex_position is not None,
                'Ссылка': op.url
            })
        return pd.DataFrame(data)