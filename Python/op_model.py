from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex


class opListModel(QAbstractListModel):
    # Определяем роли модели для всех полей
    OpNameRole = Qt.UserRole + 1
    Info1TextRole = Qt.UserRole + 2
    Info2TextRole = Qt.UserRole + 3
    UniversityNameRole = Qt.UserRole + 4
    OpCodeRole = Qt.UserRole + 5
    ImageSourceRole = Qt.UserRole + 6
    LengthTextRole = Qt.UserRole + 7

    def __init__(self, data=None):
        super().__init__()
        self._data = data or []

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < len(self._data)):
            return None

        item = self._data[index.row()]

        if role == self.OpNameRole:
            return item["opNameText"]
        elif role == self.Info1TextRole:
            return item["info1Text"]
        elif role == self.Info2TextRole:
            return item["info2Text"]
        elif role == self.UniversityNameRole:
            return item["universityNameText"]
        elif role == self.OpCodeRole:
            return item["opCodeText"]
        elif role == self.ImageSourceRole:
            return item["imageSource"]
        elif role == self.LengthTextRole:
            return item["lengthText"]

        return None

    def roleNames(self):
        return {
            self.OpNameRole: b"opNameText",
            self.Info1TextRole: b"info1Text",
            self.Info2TextRole: b"info2Text",
            self.UniversityNameRole: b"universityNameText",
            self.OpCodeRole: b"opCodeText",
            self.ImageSourceRole: b"imageSource",
            self.LengthTextRole: b"lengthText"
        }

# Данные для списка ОП. Пример
# data = [
#     {
#         "opNameText": "Дизайн и разработка<br>информационных продуктов",
#         "info1Text": "268",
#         "info2Text": "740к ₽",
#         "universityNameText": "НИУ ВШЭ",
#         "opCodeText": "26.01.04",
#         "imageSource": "resources/hselogo.svg"
#     },
#     {
#         "opNameText": "Программная<br>инженерия",
#         "info1Text": "289",
#         "info2Text": "700к ₽",
#         "universityNameText": "НИУ ВШЭ",
#         "opCodeText": "09.03.04",
#         "imageSource": "resources/hselogo.svg"
#     },
#     {
#         "opNameText": "Прикладная математика<br>и информатика",
#         "info1Text": "300",
#         "info2Text": "720к ₽",
#         "universityNameText": "НИУ ВШЭ",
#         "opCodeText": "01.03.02",
#         "imageSource": "resources/hselogo.svg"
#     },
#     {
#         "opNameText": "Анализ данных<br>в экономике",
#         "info1Text": "272",
#         "info2Text": "470к ₽",
#         "universityNameText": "МФТИ",
#         "opCodeText": "38.03.01",
#         "imageSource": "resources/mfti-logo.png"
#     },
#     {
#         "opNameText": "Физика<br>и нанотехнологии",
#         "info1Text": "280",
#         "info2Text": "500к ₽",
#         "universityNameText": "МФТИ",
#         "opCodeText": "16.03.01",
#         "imageSource": "resources/mfti-logo.png"
#     },
#     {
#         "opNameText": "Информационная<br>безопасность",
#         "info1Text": "260",
#         "info2Text": "450к ₽",
#         "universityNameText": "МИРЭА",
#         "opCodeText": "10.03.01",
#         "imageSource": "resources/other-logo.svg"
#     }
# ]
