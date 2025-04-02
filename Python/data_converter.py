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
                'name': op.name,
                'university': op.university,
                'exams_amount': op.exams_amount,
                'op_type': op.op_type,
                'budget_ege_score': op.budget_ege_score,
                'budget_places_amount': op.budget_places_amount,
                'paid_ege_score': op.paid_ege_score,
                'paid_places_amount': op.paid_places_amount,
                'cost': op.cost,
                'city': op.city,
                'length': op.length,
                'attendance': op.attendance,
                'exams': op.exams,
                'raex_position': op.raex_position
            })
        return pd.DataFrame(data)
