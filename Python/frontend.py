from PySide6.QtCore import QObject, Slot, Signal
from op_model import opListModel
from statistics_model import StatisticsListModel
from manage_model_data import ModelDataManagement
from utils import Utils
from search_settings import Settings
from op_card_handler import PyHandler
from unique_values import UniqueValues
from search_settings_window import SearchSettingsWindow
from dashboards_window import DashboardsWindow
from clusters_window import ClustersWindow
from export_window import ExportWindow
from data_settings_window import DataSettingsWindow
from user_cabinet_window import UserCabinetWindow
from statistics import Statistics
from data_converter import DataConverter
from plots.graph_builder import GraphBuilder
import os
from time import time


class Frontend(QObject):
    unique_values: UniqueValues  # Явно указываем тип атрибута
    mainWindowClosed = Signal()  # Сигнал, который будет испускаться при закрытии главного окна
    modelChanged = Signal()  # Сигнал, который будет испускаться при изменении модели
    notByClustersModelChanged = Signal()  # Сигнал, который будет испускаться, если модель изменена не по кластерам

    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self.op_list, self.unique_values = ModelDataManagement.get_op_data(
            Utils.resource_path('Python/data_sci_programs.json'))  # self.op_list - список всех объектов Op
        self.settings = Settings()
        self.statistics = Statistics()  # Экземпляр класса Statistics для хранения статистики
        self.df = None  # DataFrame для графиков
        self.filtered_op_list = None  # Список объектов Op, которые отображаются в главном окне и подходят по фильтрам
        self.op_model = None
        self.statistics_model = None
        self.search_settings_window = None  # Ссылка на окно настроек
        self.dashboard_window = None  # Ссылка на окно дашбордов
        self.clusters_window = None  # Ссылка на окно кластеров
        self.export_window = None  # Ссылка на окно экспорта
        self.user_cabinet_window = None  # Ссылка на окно личного кабинета
        self.data_settings_window = None  # Ссылка на окно настроек данных
        self.pyHandler = PyHandler(engine, self)  # Создаем экземпляр обработчика (для объектов в ListView)

        self.setup_models()
        self.setup_connections()

    def setup_models(self):
        try:
            print("Обновление моделей...")

            # Получаем данные для модели
            op_model_data, statistics_model_data, self.filtered_op_list, self.statistics = ModelDataManagement.get_op_model_data(
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

            # Работа с графиками. Для начала нужен df
            try:
                # Преобразуем список объектов Op в DataFrame
                self.df = DataConverter.list_op_to_dataframe(self.filtered_op_list)
            except:
                print('Новые графики построить не получится')

            self.update_price_plot()

            # Сигнализируем об изменении модели
            self.modelChanged.emit()

            if self.settings.filter_by_cluster:
                # Если был применен фильтр по кластеру, то в будущем его быть не должно
                self.settings.filter_by_cluster = False
                self.settings.cluster_urls = []
            else:
                # Сигнализируем об изменении модели, если фильтр не по кластерам
                self.notByClustersModelChanged.emit()
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

        # Кнопка кластеров
        clusters_button = root_object.findChild(QObject, 'clustersButton')
        if clusters_button:
            clusters_button.clicked.connect(self.clusters_button_clicked)
        else:
            print('Кнопка кластеров не найдена!')

        # Кнопка экспорта
        export_button = root_object.findChild(QObject, 'exportButton')
        if export_button:
            export_button.clicked.connect(self.export_button_clicked)
        else:
            print('Кнопка экспорта не найдена!')

        # Кнопка настроек данных (обновления)
        data_settings_button = root_object.findChild(QObject, 'dataSettingsButton')
        if data_settings_button:
            data_settings_button.clicked.connect(self.data_settings_button_clicked)
        else:
            print('Кнопка настроек данных не найдена!')

        # Кнопка личного кабинета
        user_cabinet_button = root_object.findChild(QObject, 'userCabinetButton')
        if user_cabinet_button:
            user_cabinet_button.clicked.connect(self.user_cabinet_button_clicked)
        else:
            print('Кнопка личного кабинета не найдена!')

        # Этот класс является обработчиком сигналов из QML
        # Обработкой занимается handleExamDeleted
        context = self.engine.rootContext()
        context.setContextProperty("examHandler", self)

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
                self.search_settings_window.window.raise_()
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
                self.dashboard_window.window.raise_()
            except Exception as e:
                print("Окно дашбордов уже открыто:", e)

    @Slot()
    def clusters_button_clicked(self):
        # Если ссылка на окно отсутствует или само окно закрыто, создаём новое окно
        if self.clusters_window is None or self.clusters_window.window is None:
            print('Кнопка кластеров нажата!')
            self.clusters_window = ClustersWindow(self.engine, self)
            self.clusters_window.updateModels.connect(self.setup_models)
        else:
            try:
                self.clusters_window.window.raise_()
            except Exception as e:
                print("Окно кластеров уже открыто:", e)

    @Slot()
    def export_button_clicked(self):
        # Если ссылка на окно отсутствует или само окно закрыто, создаём новое окно
        if self.export_window is None or self.export_window.window is None:
            print('Кнопка экспорта нажата!')
            self.export_window = ExportWindow(self.engine, self)
        else:
            try:
                self.export_window.window.raise_()
            except Exception as e:
                print("Окно экспорта уже открыто:", e)

    @Slot()
    def data_settings_button_clicked(self):
        # Если ссылка на окно отсутствует или само окно закрыто, создаём новое окно
        if self.data_settings_window is None or self.data_settings_window.window is None:
            print('Кнопка настроек данных нажата!')
            self.data_settings_window = DataSettingsWindow(self.engine, self)
        else:
            try:
                self.data_settings_window.window.raise_()
            except Exception as e:
                print("Окно настроек данных уже открыто:", e)

    @Slot()
    def user_cabinet_button_clicked(self):
        # Если ссылка на окно отсутствует или само окно закрыто, создаём новое окно
        if self.user_cabinet_window is None or self.user_cabinet_window.window is None:
            print('Кнопка личного кабинета нажата!')
            self.user_cabinet_window = UserCabinetWindow(self.engine, self.unique_values, self)
        else:
            try:
                self.user_cabinet_window.window.raise_()
            except Exception as e:
                print("Окно личного кабинета уже открыто:", e)

    @Slot(str, str, str)
    def handleExamDeleted(self, exam_name, exam_type, exam_parent_window):
        print(
            f"Нажата кнопка удаления экзамена: {exam_name}, тип: {exam_type}, родительское окно: {exam_parent_window}")
        if exam_parent_window == "settings":
            try:
                self.search_settings_window.delete_exam(exam_name, exam_type)
            except Exception as e:
                print("Ошибка при удалении экзамена из окна настроек", e)
        if exam_parent_window == "cabinet":
            try:
                self.user_cabinet_window.delete_exam(exam_name, exam_type)
            except Exception as e:
                print("Ошибка при удалении экзамена из окна личного кабинета", e)

    def update_price_plot(self):
        """
        Обновляем график цен/проходных баллов в зависимости от выбранного фильтра.
        """
        try:
            output_path = Utils.resource_path('FirstPythonContent/plots_images/price_to_points_scatter.png')
            os.makedirs(output_path.parent, exist_ok=True)
            fig = GraphBuilder.price_to_points_scatter(self.df, self.settings.show_op_only_with_budget)
            fig.savefig(output_path, bbox_inches='tight')

            root_object = self.engine.rootObjects()[0]
            score_price_image = root_object.findChild(QObject, 'scorePriceImage')
            if score_price_image:
                score_price_image.setProperty('headerVisible', False)
                score_price_image.setProperty('source', f'plots_images/price_to_points_scatter.png?cacheBust={time()}')
            else:
                print("Элемент 'scorePriceImage' не найден")
        except Exception as e:
            print("Ошибка при обновлении графика цен:", e)
            root_object = self.engine.rootObjects()[0]
            score_price_image = root_object.findChild(QObject, 'scorePriceImage')
            if score_price_image:
                score_price_image.setProperty('headerVisible', True)
                score_price_image.setProperty('source', f'')
                score_price_image.setProperty('headerText', 'По указанным фильтром<br>нет ОП в топ-100 RAEX')
            else:
                print("Элемент 'scorePriceImage' не найден")

    @Slot()
    def on_main_window_closed(self):
        """Слот, вызываемый при закрытии главного окна."""
        print("Главное окно закрыто")
        self.mainWindowClosed.emit()
