from utils import Utils
from PySide6.QtCore import QObject, Slot
from PySide6.QtQml import QQmlComponent
from PySide6.QtCore import QUrl


class PyHandler(QObject):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine

    @Slot(int, str, str, str, str)
    def handleCardClicked(self, index, op_name, university_name, op_type, length_text):
        print(
            f"Клик по карточке: индекс={index}, ОП: {op_name}, университет: {university_name}, тип: {op_type}, длина: {length_text}")

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
