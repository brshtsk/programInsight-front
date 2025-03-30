from PySide6.QtCore import QObject, Slot, QUrl
from PySide6.QtQml import QQmlComponent
from op_model import opListModel
from statistics_model import StatisticsListModel
from manage_model_data import ModelDataManagement
from utils import Utils
from search_settings import Settings
from op_card_handler import PyHandler


class Frontend(QObject):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self.op_list = ModelDataManagement.get_op_data(Utils.resource_path('Python/big_data.json'))[::-1]
        self.settings = Settings()
        self.op_model = None
        self.statistics_model = None
        self.search_settings_window = None  # Ссылка на окно настроек
        self.dashboard_window = None  # Ссылка на окно дашбордов
        self.pyHandler = PyHandler(engine)  # Создаем экземпляр обработчика (для объектов в ListView)

        self.setup_models()
        self.setup_connections()

    def setup_models(self):
        # Регистрируем обработчик в QML, чтобы обращаться к нему по имени "pyHandler"
        context = self.engine.rootContext()
        context.setContextProperty("pyHandler", self.pyHandler)

        # Получаем данные для модели
        op_model_data, statistics_model_data = ModelDataManagement.get_op_model_data(self.op_list, self.settings)
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

    def setup_connections(self):
        root_object = self.engine.rootObjects()[0]

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

    @Slot()
    # Python
    def search_button_clicked(self):
        if self.search_settings_window is None:
            print('Кнопка настроек поиска нажата!')
            settings_qml_path = Utils.resource_path('FirstPythonContent/SearchSettings.qml')
            component = QQmlComponent(self.engine, QUrl.fromLocalFile(str(settings_qml_path)))
            if component.status() == QQmlComponent.Ready:
                self.search_settings_window = component.create()
                if self.search_settings_window:
                    self.search_settings_window.show()
                    self.connect_to_search_settings(self.search_settings_window)
                    # При закрытии окна вместо уничтожения просто скрываем его
                    self.search_settings_window.windowClosed.connect(self.on_search_settings_closed)
                    # Заполняем окно предыдущими настройками
                    self.restore_search_settings_view(self.search_settings_window)
                else:
                    print("Не удалось создать окно настроек.")
            else:
                print("Ошибка при загрузке SearchSettings.qml:", component.errorString())
        else:
            # Если окно уже существует, показываем его и обновляем значения
            self.search_settings_window.show()
            self.restore_search_settings_view(self.search_settings_window)

    def restore_search_settings_view(self, settings_window):
        # Восстанавливаем значение ComboBox "scoreTypeComboBox"
        combo_box = settings_window.findChild(QObject, 'scoreTypeComboBox')
        if combo_box:
            # 0 - бюджет, 1 - платное
            combo_box.setProperty('currentIndex', 0 if self.settings.show_budget_score else 1)
        # Восстанавливаем состояние CheckBox "onlyWithBudgetCheckBox"
        only_budget_checkbox = settings_window.findChild(QObject, 'onlyWithBudgetCheckBox')
        if only_budget_checkbox:
            only_budget_checkbox.setProperty('checked', self.settings.show_op_only_with_budget)
        # Восстанавливаем состояние CheckBox "applyFilterByPriceCheckBox"
        apply_filter_checkbox = settings_window.findChild(QObject, 'applyFilterByPriceCheckBox')
        if apply_filter_checkbox:
            apply_filter_checkbox.setProperty('checked', self.settings.filter_by_price)
        # Восстанавливаем текстовые поля для цены
        min_price_field = settings_window.findChild(QObject, 'minPriceTextField')
        if min_price_field:
            # Если цена хранится в тысячах, делим на 1000 для отображения пользователю
            if self.settings.min_price > 0:
                min_price_field.setProperty('text', str(self.settings.min_price // 1000))
        max_price_field = settings_window.findChild(QObject, 'maxPriceTextField')
        if max_price_field:
            if self.settings.max_price < 100_000_000:
                max_price_field.setProperty('text', str(self.settings.max_price // 1000))

    @Slot()
    def dashboard_button_clicked(self):
        # Если окно дашбордов уже открыто, выходим из метода
        if self.dashboard_window is not None:
            print("Окно дашбордов уже открыто!")
            return

        print('Кнопка дашбордов нажата!')
        dashboard_qml_path = Utils.resource_path('FirstPythonContent/Dashboards.qml')
        component = QQmlComponent(self.engine, QUrl.fromLocalFile(str(dashboard_qml_path)))
        if component.status() == QQmlComponent.Ready:
            self.dashboard_window = component.create()
            if self.dashboard_window:
                self.dashboard_window.show()
                # Подключаем сигнал закрытия окна, чтобы обнулить ссылку
                self.dashboard_window.destroyed.connect(self.on_dashboard_closed)
            else:
                print("Не удалось создать окно дашбордов.")
        else:
            print("Ошибка при загрузке Dashboard.qml:", component.errorString())

    @Slot()
    def on_dashboard_closed(self):
        """Слот, вызываемый при закрытии окна дашбордов, чтобы очистить ссылку."""
        print("Окно дашбордов закрыто")
        self.dashboard_window = None
        # ToDo: не дает открыть дашборды во второй раз

    def connect_to_search_settings(self, settings_window):
        # Показывать баллы на бюджет или платное
        combo_box = settings_window.findChild(QObject, 'scoreTypeComboBox')
        if combo_box:
            combo_box.currentIndexChanged.connect(self.combobox_index_changed)
        else:
            print("ComboBox 'scoreTypeComboBox' не найден!")

        # Показывать только ОП с бюджетными местами
        only_budget_checkbox = settings_window.findChild(QObject, 'onlyWithBudgetCheckBox')
        if only_budget_checkbox:
            only_budget_checkbox.toggled.connect(self.on_only_budget_checkbox_toggled)
        else:
            print("Checkbox 'onlyWithBudgetCheckBox' не найден")

        # Настройки диапазона минимальной и максимальной стоимости обучения
        apply_filter_by_price_checkbox = settings_window.findChild(QObject, 'applyFilterByPriceCheckBox')
        min_price_text_field = settings_window.findChild(QObject, 'minPriceTextField')
        max_price_text_field = settings_window.findChild(QObject, 'maxPriceTextField')

        if apply_filter_by_price_checkbox:
            apply_filter_by_price_checkbox.toggled.connect(self.apply_filter_by_price_checkbox_toggled)
        else:
            print("Checkbox 'applyFilterByPriceCheckBox' не найден")

        if min_price_text_field:
            min_price_text_field.textChanged.connect(self.on_min_price_changed)
        else:
            print("PriceField 'minPriceTextField' не найден")

        if max_price_text_field:
            max_price_text_field.textChanged.connect(self.on_max_price_changed)
        else:
            print("PriceField 'maxPriceTextField' не найден")

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

    @Slot()
    def on_only_budget_checkbox_toggled(self):
        checkbox = self.sender()
        if checkbox is not None:
            checked = checkbox.property('checked')
            print(f"Состояние чекбокса 'onlyWithBudgetCheckBox': {checked}")
            self.settings.show_op_only_with_budget = checked
            self.setup_models()
        else:
            print("sender() не найден")

    @Slot()
    def apply_filter_by_price_checkbox_toggled(self):
        checkbox = self.sender()
        if checkbox is not None:
            checked = checkbox.property('checked')
            print(f"Состояние чекбокса 'applyFilterByPriceCheckBox': {checked}")
            self.settings.filter_by_price = checked
            try:
                self.setup_models()
            except:
                print("Ошибка при применении фильтра по цене")
                # ToDo: уведомлять пользователя, если по фильтру ничего не найдено
        else:
            print("sender() не найден")

    @Slot()
    def on_min_price_changed(self):
        min_price = self.sender().property('text')  # Получаем текст из поля
        print(f"Минимальная цена введена: {min_price}")
        try:
            min_price = int(min_price) * 1000
            self.settings.min_price = min_price
            if self.settings.filter_by_price and self.settings.price_range_is_ok():
                self.setup_models()
        except:
            print(f"Минимальная цена {min_price} не может быть задана! Сбросим до 0")
            self.settings.min_price = 0
            if self.settings.filter_by_price and self.settings.price_range_is_ok():
                self.setup_models()

    @Slot()
    def on_max_price_changed(self):
        max_price = self.sender().property('text')
        print(f"Максимальная цена введена: {max_price}")
        try:
            max_price = int(max_price) * 1000
            self.settings.max_price = max_price
            if self.settings.filter_by_price and self.settings.price_range_is_ok():
                self.setup_models()
        except:
            print(f"Максимальная цена {max_price} не может быть задана! Сбросим до 100000000")
            self.settings.max_price = 100000000
            if self.settings.filter_by_price and self.settings.price_range_is_ok():
                self.setup_models()
