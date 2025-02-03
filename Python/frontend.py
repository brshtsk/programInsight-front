from PySide6.QtCore import QObject, Slot, QUrl
from PySide6.QtQml import QQmlComponent
from op_model import opListModel
from statistics_model import StatisticsListModel
from get_json_data import get_op_model_data
from utils import resource_path  # Импортируем функцию resource_path


class Frontend(QObject):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine

        # Загрузка данных моделей
        op_data, statistics_data = get_op_model_data('op_data.json')
        self.op_model = opListModel(op_data)
        self.statistics_model = StatisticsListModel(statistics_data)

        self.setup_connections()

    def setup_connections(self):
        # Получаем корневой объект QML
        root_object = self.engine.rootObjects()[0]

        # Передаём модели в контекст QML
        context = self.engine.rootContext()
        context.setContextProperty("opModel", self.op_model)
        context.setContextProperty("statisticsModel", self.statistics_model)

        # Ищем кнопку по имени (предполагается, что у кнопки `id: searchSettingsButton`)
        button = root_object.findChild(QObject, 'searchSettingsButton')
        if button:
            button.clicked.connect(self.button_clicked)
        else:
            print('Кнопка не найдена!')

    @Slot()
    def button_clicked(self):
        print('Кнопка нажата!')

        # Определяем путь к файлу SearchSettingsScreen.ui.qml
        settings_qml_path = resource_path('FirstPythonContent/SearchSettings.qml')

        # Создаём компонент QML для окна настроек
        component = QQmlComponent(self.engine, QUrl.fromLocalFile(str(settings_qml_path)))

        # Проверяем статус компонента
        if component.status() == QQmlComponent.Ready:
            # Создаём экземпляр окна настроек
            settings_window = component.create()
            if settings_window:
                settings_window.show()
            else:
                print("Не удалось создать окно настроек.")
        else:
            print("Ошибка при загрузке SearchSettings.qml:", component.errorString())
