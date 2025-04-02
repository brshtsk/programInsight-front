from PySide6.QtCore import QObject, Slot, QUrl
from PySide6.QtQml import QQmlComponent
from utils import Utils

class NewExamWindow(QObject):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self.window = None
        self.load_window()

    def load_window(self):
        exam_card_path = Utils.resource_path('FirstPythonContent/NewExamProperties.qml')
        component = QQmlComponent(self.engine, QUrl.fromLocalFile(str(exam_card_path)))
        if component.status() == QQmlComponent.Ready:
            self.window = component.create()
            if self.window:
                self.window.show()
                self.window.windowClosed.connect(self.on_window_closed)
            else:
                print("Не удалось создать окно NewExamProperties.")
        else:
            print("Ошибка при загрузке NewExamProperties.qml:", component.errorString())

    @Slot()
    def on_window_closed(self):
        """Слот, вызываемый при закрытии окна, чтобы очистить ссылку."""
        print("Окно NewExamProperties закрыто")
        self.window = None