from PySide6.QtCore import QObject, Slot, QUrl
from PySide6.QtQml import QQmlComponent
from op_model import opListModel
from statistics_model import StatisticsListModel
from manage_model_data import get_op_model_data, load_op_and_statistics
from utils import resource_path
from op_statistics_class import Statistics, Op
from search_settings import Settings


class Frontend(QObject):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self.op_list, self.statistics = load_op_and_statistics(resource_path('Python/op_data.json'))
        self.settings = Settings()
        self.op_model = None
        self.statistics_model = None
        self.search_settings_window = None  # Ссылка на окно настроек
        self.setup_models()
        self.setup_connections()

    def setup_models(self):
        op_model_data, statistics_model_data = get_op_model_data(self.op_list, self.statistics, self.settings)
        self.op_model = opListModel(op_model_data)
        self.statistics_model = StatisticsListModel(statistics_model_data)
        context = self.engine.rootContext()
        context.setContextProperty("opModel", self.op_model)
        context.setContextProperty("statisticsModel", self.statistics_model)

    def setup_connections(self):
        root_object = self.engine.rootObjects()[0]
        button = root_object.findChild(QObject, 'searchSettingsButton')
        if button:
            button.clicked.connect(self.button_clicked)
        else:
            print('Кнопка не найдена!')

    @Slot()
    def button_clicked(self):
        # Если окно уже открыто, выходим из метода
        if self.search_settings_window is not None:
            return

        print('Кнопка настроек поиска нажата!')
        settings_qml_path = resource_path('FirstPythonContent/SearchSettings.qml')
        component = QQmlComponent(self.engine, QUrl.fromLocalFile(str(settings_qml_path)))
        if component.status() == QQmlComponent.Ready:
            self.search_settings_window = component.create()  # Создаем окно и сохраняем ссылку
            if self.search_settings_window:
                self.search_settings_window.show()
                self.connect_to_search_settings(self.search_settings_window)
                # Подключаем пользовательский сигнал закрытия из QML
                try:
                    self.search_settings_window.windowClosed.connect(self.on_search_settings_closed)
                except Exception as e:
                    print("Не удалось подключить сигнал windowClosed:", e)
            else:
                print("Не удалось создать окно настроек.")
        else:
            print("Ошибка при загрузке SearchSettings.qml:", component.errorString())

    def connect_to_search_settings(self, settings_window):
        combo_box = settings_window.findChild(QObject, 'scoreTypeComboBox')
        if combo_box:
            combo_box.currentIndexChanged.connect(self.combobox_index_changed)
        else:
            print('ComboBox не найден!')

    @Slot()
    def combobox_index_changed(self):
        combo_box = self.sender()
        if combo_box is not None:
            index = combo_box.property('currentIndex')
            print(f"Выбранный индекс: {index}")
            # 0 - бюджет, 1 - платное
            self.settings.show_budget_score = (index == 0)
            self.setup_models()
        else:
            print("sender() не найден")

    @Slot()
    def on_search_settings_closed(self):
        """Слот, вызываемый при закрытии окна настроек, чтобы очистить ссылку."""
        print("Окно настроек закрыто")
        self.search_settings_window = None
        # ToDo: сохранять настройки, чтобы при следующем открытии окна поля не сбрасывались

