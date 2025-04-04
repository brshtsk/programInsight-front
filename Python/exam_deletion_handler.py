from utils import Utils
from PySide6.QtCore import QObject, Slot
from PySide6.QtQml import QQmlComponent
from PySide6.QtCore import QUrl


class ExamHandler(QObject):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine

    @Slot(str, str)
    def handleExamDeleted(self, exam_name, exam_type):
        print(f"Нажата кнопка удаления экзамена: {exam_name}, тип: {exam_type}")
