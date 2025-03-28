from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex

class ExamListModel(QAbstractListModel):
    ExamNameRole = Qt.UserRole + 1

    def __init__(self, exams=None, parent=None):
        super().__init__(parent)
        self._exams = [{"examNameText": str(exam)} for exam in exams] if exams else []

    def rowCount(self, parent=QModelIndex()):
        return len(self._exams)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == self.ExamNameRole:
            return self._exams[index.row()]["examNameText"]
        return None

    def roleNames(self):
        return {self.ExamNameRole: b"examNameText"}

    def updateData(self, exams):
        self.beginResetModel()
        self._exams = [{"examNameText": str(exam)} for exam in exams]
        self.endResetModel()