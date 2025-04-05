from PySide6.QtCore import QObject, Slot, QUrl, Signal
from PySide6.QtQml import QQmlComponent
from op_model import opListModel
from statistics_model import StatisticsListModel
from manage_model_data import ModelDataManagement
from utils import Utils
from search_settings import Settings
from op_card_handler import PyHandler
from unique_values import UniqueValues
from search_settings_window import SearchSettingsWindow
from dashboards_window import DashboardsWindow


class Frontend(QObject):
    unique_values: UniqueValues  # Явно указываем тип атрибута
    mainWindowClosed = Signal()  # Сигнал, который будет испускаться при закрытии главного окна
    modelChanged = Signal()  # Сигнал, который будет испускаться при изменении модели

    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self.op_list, self.unique_values = ModelDataManagement.get_op_data(
            Utils.resource_path('Python/small_programs_info_lines.json'))  # self.op_list - список всех объектов Op
        self.settings = Settings()
        self.filtered_op_list = None  # Список объектов Op, которые отображаются в главном окне и подходят по фильтрам
        self.op_model = None
        self.statistics_model = None
        self.search_settings_window = None  # Ссылка на окно настроек
        self.dashboard_window = None  # Ссылка на окно дашбордов
        self.pyHandler = PyHandler(engine, self)  # Создаем экземпляр обработчика (для объектов в ListView)

        self.setup_models()
        self.setup_connections()

    def setup_models(self):
        try:
            # Получаем данные для модели
            op_model_data, statistics_model_data, self.filtered_op_list = ModelDataManagement.get_op_model_data(
                self.op_list, self.settings,
                self.unique_values)
            self.op_model = opListModel(op_model_data)
            self.statistics_model = StatisticsListModel(statistics_model_data)

            # Показываем количество найденных ОП
            root_object = self.engine.rootObjects()[0]
            amount_text = root_object.findChild(QObject, 'resultAmountText')
            if amount_text:
                amount_text.setProperty('text', f'Получено {len(op_model_data)} результатов')
            else:
                print("Элемент с objectName 'resultAmountText' не найден")

            # Передаем данные в модель
            context = self.engine.rootContext()
            context.setContextProperty("opModel", self.op_model)
            context.setContextProperty("statisticsModel", self.statistics_model)

            # Сигнализируем об изменении модели
            self.modelChanged.emit()
        except Exception as e:
            print("Ошибка при создании моделей! Модели не изменены. Текст ошибки:", e)

    def setup_connections(self):
        root_object = self.engine.rootObjects()[0]

        # Регистрируем обработчик в QML, чтобы обращаться к нему по имени "pyHandler"
        context = self.engine.rootContext()
        context.setContextProperty("pyHandler", self.pyHandler)

        # Кнопка настроек
        button = root_object.findChild(QObject, 'searchSettingsButton')
        if button:
            button.clicked.connect(self.search_button_clicked)
        else:
            print('Кнопка не найдена!')

        # Кнопка дашбордов
        dashboard_button = root_object.findChild(QObject, 'dashboardButton')
        if dashboard_button:
            dashboard_button.clicked.connect(self.dashboard_button_clicked)
        else:
            print('Кнопка дашбордов не найдена!')

        # Подключаем событие закрытия главного окна к слоту on_main_window_closed.
        root_object.windowClosed.connect(self.on_main_window_closed)

    @Slot()
    def search_button_clicked(self):
        # Если ссылка на окно отсутствует или само окно закрыто, создаём новое окно
        if self.search_settings_window is None or self.search_settings_window.window is None:
            print('Кнопка настроек поиска нажата!')
            self.search_settings_window = SearchSettingsWindow(self.engine, self.settings, self.unique_values, self)
            self.search_settings_window.updateModels.connect(self.setup_models)
        else:
            try:
                self.search_settings_window.window.show()
                self.search_settings_window.restore_view()
            except Exception as e:
                print("Окно настроек уже открыто, восстановление настроек не выполнено:", e)

    @Slot()
    def dashboard_button_clicked(self):
        # Если ссылка на окно отсутствует или само окно закрыто, создаём новое окно
        if self.dashboard_window is None or self.dashboard_window.window is None:
            print('Кнопка дашбордов нажата!')
            self.dashboard_window = DashboardsWindow(self.engine, self)
        else:
            try:
                self.search_settings_window.window.show()
                self.search_settings_window.restore_view()
            except Exception as e:
                print("Окно дашбордов уже открыто:", e)

    @Slot()
    def on_main_window_closed(self):
        """Слот, вызываемый при закрытии главного окна."""
        print("Главное окно закрыто")
        self.mainWindowClosed.emit()
