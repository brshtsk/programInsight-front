from PySide6.QtCore import QObject, Slot, Signal
from PySide6.QtQml import QQmlComponent
from utils import Utils
from search_settings import Settings
from unique_values import UniqueValues
from new_exam_window import NewExamWindow
from exam import Exam


class ClustersWindow(QObject):
    updateModels = Signal()  # Сигнал для уведомления Frontend об изменениях

    def __init__(self, engine, frontend_parent):
        super().__init__()
        self.engine = engine
        self.frontend_parent = frontend_parent
        self.component = None
        self.window = None
        self.new_exam_window = None

        self.load_window()

        self.frontend_parent.mainWindowClosed.connect(self.on_main_window_closed)

    def load_window(self):
        clusters_qml_path = Utils.resource_path('FirstPythonContent/Clusters.qml')
        self.component = QQmlComponent(self.engine, str(clusters_qml_path))
        if self.component.status() == QQmlComponent.Ready:
            self.window = self.component.create()
            if self.window:
                self.window.show()
                # ToDo: имплемент
                # self.set_default_properties()
                # self.build_plots()
                self.window.windowClosed.connect(self.on_window_closed)
            else:
                print("Не удалось создать окно кластеров.")
        else:
            print("Ошибка при загрузке Clusters.qml:", self.component.errorString())

    @Slot()
    def on_main_window_closed(self):
        print("Главное окно закрыто, закрываем окно кластеров")
        if self.window is not None:
            self.window.close()
            # self.on_window_closed() - выполняется автоматически

    @Slot()
    def on_window_closed(self):
        print("Окно кластеров закрыто (либо пользователем, либо программно)")
        self.window = None
