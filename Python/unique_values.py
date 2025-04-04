from op import Op


class UniqueValues:
    '''
    Хранит информацию обо всех:
    - экзаменах (отдельно для магистратуры и бакалавриата/специалитета)
    - городах обучения
    - названиях ОП
    - названиях ВУЗов
    '''

    def __init__(self):
        self.subjects_bak_or_spec = set()
        self.subjects_mag = set()
        self.cities = set()
        self.universities = set()
        self.lowercase_universities = set()  # Для бытрого поиска по ВУЗам
        self.op_names = set()

    def add_op(self, op: Op):
        '''
        Добавляет ОП в уникальные значения
        :param op:
        :return:
        '''
        self.op_names.add(op.name)
        self.universities.add(op.university)
        self.lowercase_universities.add(op.university.lower())
        self.cities.add(op.city)

        if op.op_type == 'Бакалавриат' or op.op_type == 'Специалитет':
            for exam in op.exams:
                for subject in exam:
                    self.subjects_bak_or_spec.add(subject)
        elif op.op_type == 'Магистратура':
            for exam in op.exams:
                for subject in exam:
                    self.subjects_mag.add(subject)
