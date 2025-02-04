from PySide6.QtCore import QObject, Slot, QUrl
from PySide6.QtQml import QQmlComponent
from op_model import opListModel
from statistics_model import StatisticsListModel
from manage_model_data import get_op_model_data, get_op_data
from utils import resource_path
from op_statistics_class import Statistics, Op
from search_settings import Settings


class Frontend(QObject):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self.op_list = get_op_data(resource_path('Python/op_data.json'))
        self.settings = Settings()
        self.op_model = None
        self.statistics_model = None
        self.search_settings_window = None  # Ссылка на окно настроек
        self.setup_models()
        self.setup_connections()

    def setup_models(self):
        # Получаем данные для модели
        op_model_data, statistics_model_data = get_op_model_data(self.op_list, self.settings)
        self.op_model = opListModel(op_model_data)
        self.statistics_model = StatisticsListModel(statistics_model_data)

        # Показываем количество найденных ОП
        root_object = self.engine.rootObjects()[0]
        amount_text = root_object.findChild(QObject, 'resultAmountText')
        if amount_text:
            amount_text.setProperty('text', f'Получено {len(op_model_data)} результатов')
        else:
            print("Элемент с objectName 'resultAmountText' не найден")

        # Переадем данные в модель
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
        # ToDo: сохранять настройки, чтобы при следующем открытии окна поля не сбрасывались

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
            self.setup_models()
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
            print(f"Минимальная цена {min_price} не может быть задана!")


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
            print(f"Максимальная цена {max_price} не может быть задана!")
