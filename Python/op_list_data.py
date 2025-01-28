from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex


class CustomListModel(QAbstractListModel):
    # Роли модели
    OpTextRole = Qt.UserRole + 1
    Info1TextRole = Qt.UserRole + 2
    Info2TextRole = Qt.UserRole + 3

    def __init__(self, data=None):
        super().__init__()
        self._data = data or []

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < len(self._data)):
            return None

        item = self._data[index.row()]

        if role == self.OpTextRole:
            return item['opText']
        elif role == self.Info1TextRole:
            return item['info1Text']
        elif role == self.Info2TextRole:
            return item['info2Text']

        return None

    def roleNames(self):
        return {
            self.OpTextRole: b'opText',
            self.Info1TextRole: b'info1Text',
            self.Info2TextRole: b'info2Text'
        }


# Пример данных
data = [
    {
        'opText': "Программная инженерия<br/>НИУ ВШЭ",
        'info1Text': "289<br/>баллов ЕГЭ",
        'info2Text': "700к ₽<br/>стоимость"
    },
    {
        'opText': "Прикладная математика и<br/>информатика<br/>НИУ ВШЭ",
        'info1Text': "298<br/>баллов ЕГЭ",
        'info2Text': "999к ₽<br/>стоимость"
    },
    {
        'opText': "Егооооор",
        'info1Text': "298<br/>баллов ЕГЭ",
        'info2Text': "999к ₽<br/>стоимость"
    },
    {
        'opText': "У меня получилось",
        'info1Text': "298<br/>баллов ЕГЭ",
        'info2Text': "999к ₽<br/>стоимость"
    },
    {
        'opText': "Добавлять эти данные",
        'info1Text': "298<br/>баллов ЕГЭ",
        'info2Text': "999к ₽<br/>стоимость"
    },
    {
        'opText': "Через питон",
        'info1Text': "298<br/>баллов ЕГЭ",
        'info2Text': "999к ₽<br/>стоимость"
    },
    {
        'opText': "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧",
        'info1Text': "298<br/>баллов ЕГЭ",
        'info2Text': "999к ₽<br/>стоимость"
    },
    {
        'opText': "Добавляю новую<br/>строку",
        'info1Text': "000<br/>баллов ЕГЭ",
        'info2Text': "55к ₽<br/>стоимость"
    },
    {
        'opText': "Приветик<br/>пистолетик",
        'info1Text': "000<br/>баллов ЕГЭ",
        'info2Text': "55к ₽<br/>стоимость"
    }
]
