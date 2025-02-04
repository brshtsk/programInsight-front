from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex


class StatisticsListModel(QAbstractListModel):
    # Определяем роли модели
    StatisticTypeRole = Qt.UserRole + 1
    ImageSourceRole = Qt.UserRole + 2
    StatisticProgressTextRole = Qt.UserRole + 3
    ProgressRole = Qt.UserRole + 4

    def __init__(self, data=None):
        super().__init__()
        self._data = data or []

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < len(self._data)):
            return None

        item = self._data[index.row()]

        if role == self.StatisticTypeRole:
            return item["statisticTypeText"]
        elif role == self.ImageSourceRole:
            return item["imageSource"]
        elif role == self.StatisticProgressTextRole:
            return item["statisticProgressText"]
        elif role == self.ProgressRole:
            return item["progress"]

        return None

    def roleNames(self):
        return {
            self.StatisticTypeRole: b"statisticTypeText",
            self.ImageSourceRole: b"imageSource",
            self.StatisticProgressTextRole: b"statisticProgressText",
            self.ProgressRole: b"progress",
        }


# Данные для модели. Пример
# statistics_data = [
#     {
#         "statisticTypeText": "Средний балл ЕГЭ",
#         "imageSource": "resources/pencil-plain.png",
#         "statisticProgressText": "87.2",
#         "progress": 0.872
#     },
#     {
#         "statisticTypeText": "Средняя стоимость (тыс. ₽)",
#         "imageSource": "resources/money.png",
#         "statisticProgressText": "624",
#         "progress": 1.0
#     },
#     {
#         "statisticTypeText": "Среднее количество мест",
#         "imageSource": "resources/people.png",
#         "statisticProgressText": "76",
#         "progress": 1.0
#     },
#     {
#         "statisticTypeText": "С бюджетными местами",
#         "imageSource": "resources/cap.svg",
#         "statisticProgressText": "57%",
#         "progress": 0.57
#     }
# ]
