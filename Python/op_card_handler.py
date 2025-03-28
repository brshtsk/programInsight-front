from utils import Utils
from PySide6.QtCore import QObject, Slot
from PySide6.QtQml import QQmlComponent
from PySide6.QtCore import QUrl


class PyHandler(QObject):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine

    @Slot(int, str, str, str, str, str, str, int, int, int, int, int, list, list)
    def handleCardClicked(self, index, op_name, university_name, op_type, length_text,
                          location_text, attendance_text, raex_position, budget_score,
                          paid_score, budget_places, paid_places, single_exams, choice_exams):
        print(f"Клик по карточке: индекс={index}, ОП: {op_name}, университет: {university_name}, "
              f"тип: {op_type}, длина: {length_text}, локация: {location_text}, "
              f"посещаемость: {attendance_text}, raexPosition: {raex_position},\n"
              f"бюджетный балл: {budget_score}, платный балл: {paid_score}, "
              f"бюджетных мест: {budget_places}, платных мест: {paid_places}, "
              f"экзамены без выбора: {single_exams}, экзамены с выбором: {choice_exams}")

        # Открываем окно с информацией об ОП
        self.showOpWidget()

    def showOpWidget(self):
        widget_qml_path = Utils.resource_path('FirstPythonContent/OpWidget.qml')
        component = QQmlComponent(self.engine, QUrl.fromLocalFile(str(widget_qml_path)))
        if component.status() == QQmlComponent.Ready:
            window = component.create()
            if window:
                window.show()
            else:
                print("Failed to create window from the component.")
        else:
            print("Error loading OpWidget.qml:", component.errorString())
