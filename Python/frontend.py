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
        self.op_list, self.unique_values = ModelDataManagement.get_op_data(Utils.resource_path('Python/big_data.json'))
        self.settings = Settings()
        self.op_model = None
        self.statistics_model = None
        self.search_settings_window = None  # Ссылка на окно настроек
        self.dashboard_window = None  # Ссылка на окно дашбордов
        self.pyHandler = PyHandler(engine)  # Создаем экземпляр обработчика (для объектов в ListView)

        self.setup_models()
        self.setup_connections()

    def setup_models(self):
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
            try:
                # Если окно уже существует, показываем его и обновляем значения
                self.search_settings_window.show()
                self.restore_search_settings_view(self.search_settings_window)
            except:
                print("Окно поиска уже открыто, восстановление настроек не выполнено (не критично)")

    def restore_search_settings_view(self, settings_window):
        # Восстанавливаем состояние ComboBox "qualificationTypeComboBox"
        qualification_combo_box = settings_window.findChild(QObject, 'qualificationTypeComboBox')
        if qualification_combo_box:
            # Индексы ComboBox: 0 - Бакалавриат, 1 - Специалитет, 2 - Бакалавриат/Специалитет, 3 - Магистратура
            index = None
            if self.settings.qualifications == ['Бакалавриат']:
                index = 0
            if self.settings.qualifications == ['Специалитет']:
                index = 1
            if self.settings.qualifications == ['Бакалавриат', 'Специалитет']:
                index = 2
            if self.settings.qualifications == ['Магистратура']:
                index = 3
            qualification_combo_box.setProperty('currentIndex', index)
        else:
            print("ComboBox 'qualificationTypeComboBox' не найден!")

        # Восстанавливаем состояние CheckBox "applyFilterByScoreCheckBox"
        apply_filter_checkbox = settings_window.findChild(QObject, 'applyFilterByScoreCheckBox')
        if apply_filter_checkbox:
            apply_filter_checkbox.setProperty('checked', self.settings.filter_by_score)
        else:
            print("Checkbox 'applyFilterByScoreCheckBox' не найден!")

        # Восстанавливаем текстовые поля для баллов
        min_score_field = settings_window.findChild(QObject, 'minScoreTextField')
        if min_score_field:
            # Если балл хранится в тысячах, делим на 1000 для отображения пользователю
            if self.settings.min_average_score > 0:
                min_score_field.setProperty('text', str(self.settings.min_average_score))
        else:
            print("ScoreField 'minScoreTextField' не найден!")

        max_score_field = settings_window.findChild(QObject, 'maxScoreTextField')
        if max_score_field:
            if self.settings.max_average_score < 100_000_000:
                max_score_field.setProperty('text', str(self.settings.max_average_score))
        else:
            print("ScoreField 'maxScoreTextField' не найден!")

        # Восстанавливаем состояние ComboBox "paymentTypeComboBox"
        payment_combo_box = settings_window.findChild(QObject, 'paymentTypeComboBox')
        if payment_combo_box:
            payment_combo_box.setProperty('currentIndex', 0 if self.settings.show_op_only_with_budget else 1)
        else:
            print("ComboBox 'paymentTypeComboBox' не найден!")

        # Восстанавливаем состояние CheckBox "applyFilterByPriceCheckBox"
        apply_filter_checkbox = settings_window.findChild(QObject, 'applyFilterByPriceCheckBox')
        if apply_filter_checkbox:
            apply_filter_checkbox.setProperty('checked', self.settings.user_chose_filter_by_price)
        else:
            print("Checkbox 'applyFilterByPriceCheckBox' не найден!")

        # Восстанавливаем текстовые поля для цены
        min_price_field = settings_window.findChild(QObject, 'minPriceTextField')
        if min_price_field:
            # Если цена хранится в тысячах, делим на 1000 для отображения пользователю
            if self.settings.min_price > 0:
                min_price_field.setProperty('text', str(self.settings.min_price // 1000))
        else:
            print("PriceField 'minPriceTextField' не найден!")

        max_price_field = settings_window.findChild(QObject, 'maxPriceTextField')
        if max_price_field:
            if self.settings.max_price < 100_000_000:
                max_price_field.setProperty('text', str(self.settings.max_price // 1000))
        else:
            print("PriceField 'maxPriceTextField' не найден!")

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
        # Искать поступление на бюджет или платное
        payment_combo_box = settings_window.findChild(QObject, 'paymentTypeComboBox')
        if payment_combo_box:
            payment_combo_box.currentIndexChanged.connect(self.payment_combobox_index_changed)
        else:
            print("ComboBox 'paymentTypeComboBox' не найден!")

        # Искать поступление на бакалавриат, специалитет или магистратуру
        qualification_combo_box = settings_window.findChild(QObject, 'qualificationTypeComboBox')
        if qualification_combo_box:
            qualification_combo_box.currentIndexChanged.connect(self.qualification_combobox_index_changed)
        else:
            print("ComboBox 'qualificationTypeComboBox' не найден!")

        # Настройки диапазона минимального и максимального балла за один предмет
        apply_filter_by_score_checkbox = settings_window.findChild(QObject, 'applyFilterByScoreCheckBox')
        min_score_text_field = settings_window.findChild(QObject, 'minScoreTextField')
        max_score_text_field = settings_window.findChild(QObject, 'maxScoreTextField')

        if apply_filter_by_score_checkbox:
            apply_filter_by_score_checkbox.toggled.connect(self.apply_filter_by_score_checkbox_toggled)
        else:
            print("Checkbox 'applyFilterByScoreCheckBox' не найден")
        if min_score_text_field:
            min_score_text_field.textChanged.connect(self.on_min_score_changed)
        else:
            print("ScoreField 'minScoreTextField' не найден")
        if max_score_text_field:
            max_score_text_field.textChanged.connect(self.on_max_score_changed)
        else:
            print("ScoreField 'maxScoreTextField' не найден")

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

        # Поиск по названию города

        city_name_text_field = settings_window.findChild(QObject, 'cityNameTextField')
        if city_name_text_field:
            city_name_text_field.textChanged.connect(self.on_city_name_changed)
        else:
            print("TextField 'cityNameTextField' не найден")

    @Slot()
    def payment_combobox_index_changed(self):
        payment_combo_box = self.sender()
        if payment_combo_box is not None:
            index = payment_combo_box.property('currentIndex')
            # 0 - бюджет, 1 - платное
            print(f"Выбранный индекс: {index}. Выбрано поступление на {'бюджет' if not index else 'платное'}")
            if index == 0:
                self.settings.set_settings_for_budget()
            else:
                self.settings.set_settings_for_paid()
            self.setup_models()
        else:
            print("sender() не найден")

    @Slot()
    def qualification_combobox_index_changed(self):
        qualification_combo_box = self.sender()
        if qualification_combo_box is not None:
            index = qualification_combo_box.property('currentIndex')
            # 0 - Бакалавриат, 1 - Специалитет, 2 - Бакалавриат/Специалитет, 3 - Магистратура
            chosen_qualifications = []
            if index == 0:
                chosen_qualifications = ['Бакалавриат']
            if index == 1:
                chosen_qualifications = ['Специалитет']
            if index == 2:
                chosen_qualifications = ['Бакалавриат', 'Специалитет']
            if index == 3:
                chosen_qualifications = ['Магистратура']
            print(f"Выбранный индекс: {index}. Выбрано: {chosen_qualifications}")
            self.settings.qualifications = chosen_qualifications
            self.setup_models()
        else:
            print("sender() не найден")

    @Slot()
    def on_search_settings_closed(self):
        """Слот, вызываемый при закрытии окна настроек, чтобы очистить ссылку."""
        print("Окно настроек закрыто")
        self.search_settings_window = None

    @Slot()
    def apply_filter_by_price_checkbox_toggled(self):
        checkbox = self.sender()
        if checkbox is not None:
            checked = checkbox.property('checked')
            print(f"Состояние чекбокса 'applyFilterByPriceCheckBox': {checked}")
            self.settings.apply_filter_by_price(checked)
            try:
                self.setup_models()
            except:
                print("Ошибка при применении фильтра по цене")
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

    @Slot()
    def apply_filter_by_score_checkbox_toggled(self):
        checkbox = self.sender()
        if checkbox is not None:
            checked = checkbox.property('checked')
            print(f"Состояние чекбокса 'applyFilterByScoreCheckBox': {checked}")
            self.settings.filter_by_score = checked
            try:
                self.setup_models()
            except:
                print("Ошибка при применении фильтра по баллам")
        else:
            print("sender() не найден")

    @Slot()
    def on_min_score_changed(self):
        min_average_score = self.sender().property('text')  # Получаем текст из поля
        print(f"Минимальный балл введен: {min_average_score}")
        try:
            min_average_score = int(min_average_score)
            self.settings.min_average_score = min_average_score
            if self.settings.filter_by_score:
                self.setup_models()
        except:
            print(f"Минимальный балл {min_average_score} не может быть задан! Сбросим до 0")
            self.settings.min_score = 0
            if self.settings.filter_by_score:
                self.setup_models()

    @Slot()
    def on_max_score_changed(self):
        max_average_score = self.sender().property('text')
        print(f"Максимальный балл введен: {max_average_score}")
        try:
            max_average_score = int(max_average_score)
            self.settings.max_score = max_average_score
            if self.settings.filter_by_score:
                self.setup_models()
        except:
            print(f"Максимальный балл {max_average_score} не может быть задан! Сбросим до 100000000")
            self.settings.max_score = 100000000
            if self.settings.filter_by_score:
                self.setup_models()

    @Slot()
    def on_city_name_changed(self):
        city_name = self.sender().property('text')  # Получаем текст из поля
