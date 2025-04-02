from PySide6.QtCore import QObject, Slot, Signal
from PySide6.QtQml import QQmlComponent
from utils import Utils
from search_settings import Settings
from unique_values import UniqueValues

class SearchSettingsWindow(QObject):
    updateModels = Signal()  # Сигнал для уведомления Frontend об изменениях

    def __init__(self, engine, settings: Settings, unique_values: UniqueValues):
        super().__init__()
        self.engine = engine
        self.settings = settings
        self.unique_values = unique_values
        self.window = None
        self.load_window()

    def load_window(self):
        settings_qml_path = Utils.resource_path('FirstPythonContent/SearchSettings.qml')
        component = QQmlComponent(self.engine, str(settings_qml_path))
        if component.status() == QQmlComponent.Ready:
            self.window = component.create()
            if self.window:
                self.window.show()
                self.connect_signals()
                self.restore_view()
                self.window.windowClosed.connect(self.on_window_closed)
            else:
                print("Не удалось создать окно настроек.")
        else:
            print("Ошибка при загрузке SearchSettings.qml:", component.errorString())

    def connect_signals(self):
        # Искать поступление на бюджет или платное
        payment_combo_box = self.window.findChild(QObject, 'paymentTypeComboBox')
        if payment_combo_box:
            payment_combo_box.currentIndexChanged.connect(self.payment_combobox_index_changed)
        else:
            print("ComboBox 'paymentTypeComboBox' не найден!")

        # Искать поступление на бакалавриат, специалитет или магистратуру
        qualification_combo_box = self.window.findChild(QObject, 'qualificationTypeComboBox')
        if qualification_combo_box:
            qualification_combo_box.currentIndexChanged.connect(self.qualification_combobox_index_changed)
        else:
            print("ComboBox 'qualificationTypeComboBox' не найден!")

        # Настройки диапазона минимального и максимального балла за один предмет
        apply_filter_by_score_checkbox = self.window.findChild(QObject, 'applyFilterByScoreCheckBox')
        min_score_text_field = self.window.findChild(QObject, 'minScoreTextField')
        max_score_text_field = self.window.findChild(QObject, 'maxScoreTextField')

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
        apply_filter_by_price_checkbox = self.window.findChild(QObject, 'applyFilterByPriceCheckBox')
        min_price_text_field = self.window.findChild(QObject, 'minPriceTextField')
        max_price_text_field = self.window.findChild(QObject, 'maxPriceTextField')

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
        city_name_text_field = self.window.findChild(QObject, 'cityNameTextField')
        if city_name_text_field:
            city_name_text_field.userTextChanged.connect(self.on_city_name_changed)
            # Список всех городов в completer
            city_name_text_field.setProperty('availableValues', list(self.unique_values.cities))
        else:
            print("TextField 'cityNameTextField' не найден")

    def restore_view(self):
        # Восстанавливаем состояние ComboBox "qualificationTypeComboBox"
        qualification_combo_box = self.window.findChild(QObject, 'qualificationTypeComboBox')
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
        apply_filter_checkbox = self.window.findChild(QObject, 'applyFilterByScoreCheckBox')
        if apply_filter_checkbox:
            apply_filter_checkbox.setProperty('checked', self.settings.filter_by_score)
        else:
            print("Checkbox 'applyFilterByScoreCheckBox' не найден!")

        # Восстанавливаем текстовые поля для баллов
        min_score_field = self.window.findChild(QObject, 'minScoreTextField')
        if min_score_field:
            # Если балл хранится в тысячах, делим на 1000 для отображения пользователю
            if self.settings.min_average_score > 0:
                min_score_field.setProperty('text', str(self.settings.min_average_score))
        else:
            print("ScoreField 'minScoreTextField' не найден!")

        max_score_field = self.window.findChild(QObject, 'maxScoreTextField')
        if max_score_field:
            if self.settings.max_average_score < 100_000_000:
                max_score_field.setProperty('text', str(self.settings.max_average_score))
        else:
            print("ScoreField 'maxScoreTextField' не найден!")

        # Восстанавливаем состояние ComboBox "paymentTypeComboBox"
        payment_combo_box = self.window.findChild(QObject, 'paymentTypeComboBox')
        if payment_combo_box:
            payment_combo_box.setProperty('currentIndex', 0 if self.settings.show_op_only_with_budget else 1)
        else:
            print("ComboBox 'paymentTypeComboBox' не найден!")

        # Восстанавливаем состояние CheckBox "applyFilterByPriceCheckBox"
        apply_filter_checkbox = self.window.findChild(QObject, 'applyFilterByPriceCheckBox')
        if apply_filter_checkbox:
            apply_filter_checkbox.setProperty('checked', self.settings.user_chose_filter_by_price)
        else:
            print("Checkbox 'applyFilterByPriceCheckBox' не найден!")

        # Восстанавливаем текстовые поля для цены
        min_price_field = self.window.findChild(QObject, 'minPriceTextField')
        if min_price_field:
            # Если цена хранится в тысячах, делим на 1000 для отображения пользователю
            if self.settings.min_price > 0:
                min_price_field.setProperty('text', str(self.settings.min_price // 1000))
        else:
            print("PriceField 'minPriceTextField' не найден!")

        max_price_field = self.window.findChild(QObject, 'maxPriceTextField')
        if max_price_field:
            if self.settings.max_price < 100_000_000:
                max_price_field.setProperty('text', str(self.settings.max_price // 1000))
        else:
            print("PriceField 'maxPriceTextField' не найден!")

        # Восстанавливаем текстовое поле для названия города
        city_name_field = self.window.findChild(QObject, 'cityNameTextField')
        if city_name_field:
            if self.settings.city_name is not None:
                city_name_field.setProperty('text', self.settings.city_name)
        else:
            print("TextField 'cityNameTextField' не найден!")

    @Slot()
    def on_window_closed(self):
        print("Окно настроек закрыто")
        self.window = None

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
            self.updateModels.emit()
        else:
            print("sender() не найден")

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
            self.updateModels.emit()
        else:
            print("sender() не найден")

    @Slot()
    def apply_filter_by_score_checkbox_toggled(self):
        checkbox = self.sender()
        if checkbox is not None:
            checked = checkbox.property('checked')
            print(f"Состояние чекбокса 'applyFilterByScoreCheckBox': {checked}")
            self.settings.filter_by_score = checked
            self.updateModels.emit()
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
                self.updateModels.emit()
        except:
            print(f"Минимальный балл {min_average_score} не может быть задан! Сбросим до 0")
            self.settings.min_score = 0
            if self.settings.filter_by_score:
                self.updateModels.emit()

    @Slot()
    def on_max_score_changed(self):
        max_average_score = self.sender().property('text')
        print(f"Максимальный балл введен: {max_average_score}")
        try:
            max_average_score = int(max_average_score)
            self.settings.max_score = max_average_score
            if self.settings.filter_by_score:
                self.updateModels.emit()
        except:
            print(f"Максимальный балл {max_average_score} не может быть задан! Сбросим до 100000000")
            self.settings.max_score = 100000000
            if self.settings.filter_by_score:
                self.updateModels.emit()

    @Slot()
    def apply_filter_by_price_checkbox_toggled(self):
        checkbox = self.sender()
        if checkbox is not None:
            checked = checkbox.property('checked')
            print(f"Состояние чекбокса 'applyFilterByPriceCheckBox': {checked}")
            self.settings.apply_filter_by_price(checked)
            self.updateModels.emit()
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
                self.updateModels.emit()
        except:
            print(f"Минимальная цена {min_price} не может быть задана! Сбросим до 0")
            self.settings.min_price = 0
            if self.settings.filter_by_price and self.settings.price_range_is_ok():
                self.updateModels.emit()

    @Slot()
    def on_max_price_changed(self):
        max_price = self.sender().property('text')
        print(f"Максимальная цена введена: {max_price}")
        try:
            max_price = int(max_price) * 1000
            self.settings.max_price = max_price
            if self.settings.filter_by_price and self.settings.price_range_is_ok():
                self.updateModels.emit()
        except:
            print(f"Максимальная цена {max_price} не может быть задана! Сбросим до 100000000")
            self.settings.max_price = 100000000
            if self.settings.filter_by_price and self.settings.price_range_is_ok():
                self.updateModels.emit()

    @Slot()
    def on_city_name_changed(self):
        city_name = self.sender().property('text')  # Получаем текст из поля
        print(f"Название города введено: {city_name}")
        try:
            if city_name == "":
                self.settings.city_name = None
            else:
                self.settings.city_name = city_name
            self.updateModels.emit()
        except:
            print(f"Название города {city_name} не может быть задано! Сбросим до None")
            self.settings.city_name = None
            self.updateModels.emit()