from functools import lru_cache


class DataManipulations:
    def split_line(op_name: str) -> str:
        """
        Добавляет html-перенос строки для 2 и более слов
        :param op_name: название ОП в 1 строку
        :return: название с переносом через <br>
        """
        if '&' in op_name:
            # Заменяем амперсанд на html-символ для корректного отображения
            op_name = op_name.replace('&', '&amp;')

        op_split = op_name.split()
        if len(op_split) == 1:
            return op_name
        med_idx = len(op_split) // 2
        # Если строка не слишком длинная
        if len(op_name) < 35:
            # Исключим перенос после союзов
            if len(op_split) % 2 == 0 and len(op_split[med_idx - 1]) <= 2:
                med_idx -= 1
            elif len(op_split) % 2 == 1 and len(op_split[med_idx + 1]) <= 2:
                med_idx += 1
        # Если строка длинная
        else:
            left_ln = sum(map(len, op_split[:med_idx]))
            right_ln = sum(map(len, op_split[med_idx:]))
            k = 3
            while abs(right_ln - left_ln) > 8 and k != 0:
                if med_idx < 2 or med_idx > len(op_split) - 2:
                    break
                if right_ln > left_ln:
                    med_idx += 1
                    left_ln = sum(map(len, op_split[:med_idx]))
                    right_ln = sum(map(len, op_split[med_idx:]))
                else:
                    med_idx -= 1
                    left_ln = sum(map(len, op_split[:med_idx]))
                    right_ln = sum(map(len, op_split[med_idx:]))
                k -= 1

        op_split[med_idx] = '<br>' + op_split[med_idx]
        return ' '.join(op_split)

    @lru_cache
    def cut_extra(university_name: str) -> str:
        """
        Добавляет на конец '...', чтобы название университета уместилось в 20 символов
        :param university_name: полная строка
        :return: название длиной не более 35 символов (лишние слова справа удалены)
        """
        name_split = university_name.split()
        idx = -1
        while sum(map(len, name_split[:idx])) > 20 and idx > 1:
            idx -= 1
        return ' '.join(name_split[:idx]) + '...'

    @lru_cache
    def get_image_source(university_name: str) -> str:
        """
        Для названия университета возвращает расположение файла с лого
        :param university_name: str название (краткое)
        :return: str расположение
        """
        patterns = {'ВШЭ': 'resources/hselogo.svg', 'МФТИ': 'resources/mfti-logo.png'}
        default = 'resources/other-logo.svg'
        for pattern in patterns:
            if pattern in university_name:
                return patterns[pattern]
        return default
