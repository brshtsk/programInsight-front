from PySide6.QtCore import QObject, Slot
from PySide6.QtQml import QQmlComponent
from utils import Utils
from typing import List
from op import Op
from plots.graph_builder import GraphBuilder
from data_converter import DataConverter
import os


class DashboardsWindow(QObject):
    def __init__(self, engine, op_list: List[Op], frontend_parent):
        super().__init__()
        self.engine = engine
        self.op_list = op_list
        self.frontend_parent = frontend_parent
        self.component = None
        self.window = None

        self.load_window()

        self.frontend_parent.mainWindowClosed.connect(self.on_main_window_closed)

    def load_window(self):
        settings_qml_path = Utils.resource_path('FirstPythonContent/Dashboards.qml')
        self.component = QQmlComponent(self.engine, str(settings_qml_path))
        if self.component.status() == QQmlComponent.Ready:
            self.window = self.component.create()
            if self.window:
                self.window.show()
                self.build_plots()
                self.window.windowClosed.connect(self.on_window_closed)
            else:
                print("Не удалось создать окно настроек.")
        else:
            print("Ошибка при загрузке SearchSettings.qml:", self.component.errorString())

    def build_plots(self):
        """Создаёт графики на основе данных из op_list."""
        # Преобразуем список объектов Op в DataFrame
        df = DataConverter.list_op_to_dataframe(self.op_list)

        # Сохраним donut_chart
        output_path = Utils.resource_path('FirstPythonContent/plots_images/donut_chart.png')
        os.makedirs(output_path.parent, exist_ok=True)
        fig = GraphBuilder.donut_chart(df)
        fig.savefig(output_path)

    @Slot()
    def on_window_closed(self):
        """Слот, вызываемый при закрытии окна, чтобы очистить ссылку."""
        print("Окно Dashboards закрыто (либо пользователем, либо программно)")
        self.window = None

    @Slot()
    def on_main_window_closed(self):
        print("Главное окно закрыто, закрываем окно настроек")
        if self.window is not None:
            self.window.close()
            # self.on_window_closed() - выполняется автоматически
