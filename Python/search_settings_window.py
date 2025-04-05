from PySide6.QtCore import QObject, Slot, Signal
from PySide6.QtQml import QQmlComponent
from utils import Utils
from search_settings import Settings
from unique_values import UniqueValues
from new_exam_window import NewExamWindow
from exam import Exam


class SearchSettingsWindow(QObject):
    updateModels = Signal()  # Сигнал для уведомления Frontend об изменениях
    searchSettingsClosed = Signal()  # Сигнал для уведомления New Exam Window о закрытии окна настроек

    # ToDo: можно сделать ползунок для выбора диапазона баллов и стоимости

    def __init__(self, engine, settings: Settings, unique_values: UniqueValues, frontend_parent):
        super().__init__()
        self.engine = engine
        self.settings = settings
        self.unique_values = unique_values
        self.frontend_parent = frontend_parent
        self.component = None
        self.window = None
        self.new_exam_window = None

        self.load_window()

        self.frontend_parent.mainWindowClosed.connect(self.on_main_window_closed)

    def load_window(self):
        settings_qml_path = Utils.resource_path('FirstPythonContent/SearchSettings.qml')
        self.component = QQmlComponent(self.engine, str(settings_qml_path))
        if self.component.status() == QQmlComponent.Ready:
            self.window = self.component.create()
            if self.window:
                self.window.show()
                self.connect_signals()
                self.restore_view()
                self.window.windowClosed.connect(self.on_window_closed)
            else:
                print("Не удалось создать окно настроек.")
        else:
            print("Ошибка при загрузке SearchSettings.qml:", self.component.errorString())

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

        # Поиск по названию ОП
        op_name_text_field = self.window.findChild(QObject, 'opNameTextField')
        if op_name_text_field:
            op_name_text_field.userTextChanged.connect(self.on_op_name_changed)
            # Список всех ОП в completer
            op_name_text_field.setProperty('availableValues', list(self.unique_values.op_names))
        else:
            print("TextField 'opNameTextField' не найден")

        # Поиск по названию университета
        university_name_text_field = self.window.findChild(QObject, 'universityNameTextField')
        if university_name_text_field:
            university_name_text_field.userTextChanged.connect(self.on_university_name_changed)
            # Список всех университетов в completer
            university_name_text_field.setProperty('availableValues', list(self.unique_values.universities))
        else:
            print("TextField 'universityNameTextField' не найден")

        # Кнопка добавления экзамена в список
        add_exam_button = self.window.findChild(QObject, 'addExamButton')
        if add_exam_button:
            add_exam_button.clicked.connect(self.add_exam_button_clicked)
        else:
            print("Button 'addExamButton' не найден")

        # Изначально список экзаменов пустой
        chosen_user_exams_list = self.window.findChild(QObject, 'chosenUserExamsList')
        if chosen_user_exams_list:
            # Передаем в QML пустой список экзаменов
            chosen_user_exams_list.setProperty('exams', [])
        else:
            print("ListView 'chosenUserExamsList' не найден")

        # Выбор способа фильтрации по своим предметам
        filter_by_exams_combobox = self.window.findChild(QObject, 'filterByExamsComboBox')
        if filter_by_exams_combobox:
            filter_by_exams_combobox.currentIndexChanged.connect(self.filter_by_exams_combobox_index_changed)
        else:
            print("ComboBox 'filterByExamsComboBox' не найден")

        # Выбор типа фильтрации
        sort_op_var_combobox = self.window.findChild(QObject, 'sortOpVarComboBox')
        if sort_op_var_combobox:
            sort_op_var_combobox.currentIndexChanged.connect(self.sort_op_var_combobox_index_changed)
        else:
            print("ComboBox 'sortOpVarComboBox' не найден")

        # Фильтрация сверху вниз или снизу вверх
        sort_up_down_button = self.window.findChild(QObject, 'sortUpDownButton')
        if sort_up_down_button:
            sort_up_down_button.clicked.connect(self.sort_up_down_button_clicked)
        else:
            print("Button 'sortUpDownButton' не найден")

        # Этот класс является обработчиком сигналов из QML
        # Обработкой занимается handleExamDeleted
        context = self.engine.rootContext()
        context.setContextProperty("examHandler", self)

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
                # После восстановления не нужно показывать Completer
                city_name_field.setProperty('disableCompleterNow', True)
                city_name_field.setProperty('text', self.settings.city_name)
        else:
            print("TextField 'cityNameTextField' не найден!")

        # Восстанавливаем текстовое поле для названия ОП
        op_name_field = self.window.findChild(QObject, 'opNameTextField')
        if op_name_field:
            if self.settings.op_name is not None:
                # После восстановления не нужно показывать Completer
                op_name_field.setProperty('disableCompleterNow', True)
                op_name_field.setProperty('text', self.settings.op_name)
        else:
            print("TextField 'opNameTextField' не найден!")

        # Восстанавливаем текстовое поле для названия университета
        university_name_field = self.window.findChild(QObject, 'universityNameTextField')
        if university_name_field:
            if self.settings.university_name is not None:
                # После восстановления не нужно показывать Completer
                university_name_field.setProperty('disableCompleterNow', True)
                university_name_field.setProperty('text', self.settings.university_name)
        else:
            print("TextField 'universityNameTextField' не найден!")

        # Восстанавливаем состояние ComboBox "filterByExamsComboBox"
        filter_by_exams_combobox = self.window.findChild(QObject, 'filterByExamsComboBox')
        if filter_by_exams_combobox:
            # Значения: 0 - "Выключен", 1 - "Включен, без баллов", 2 - "Включен, с баллами"
            if self.settings.filter_by_exams_not_score:
                idx = 1
            elif self.settings.filter_by_exams_and_score:
                idx = 2
            else:
                idx = 0
            filter_by_exams_combobox.setProperty('currentIndex', idx)
        else:
            print("ComboBox 'filterByExamsComboBox' не найден!")

        # Восстанавливаем состояние ComboBox "sortOpVarComboBox"
        sort_op_var_combobox = self.window.findChild(QObject, 'sortOpVarComboBox')
        if sort_op_var_combobox:
            # Значения: 0 - "Без сортировки", 1 - "По рейтингу RAEX", 2 - "По цене", 3 - "По баллам"
            if self.settings.sort_by == 'raex':
                idx = 1
            elif self.settings.sort_by == 'price':
                idx = 2
            elif self.settings.sort_by == 'ege_score':
                idx = 3
            else:
                idx = 0
            sort_op_var_combobox.setProperty('currentIndex', idx)
        else:
            print("ComboBox 'sortOpVarComboBox' не найден!")

        # Восстанавливаем состояние Button "sortUpDownButton"
        sort_up_down_button = self.window.findChild(QObject, 'sortUpDownButton')
        if sort_up_down_button:
            if self.settings.sort_from_high_to_low:
                sort_up_down_button.setProperty('iconSource', 'resources/sort-from-bottom.png')
            else:
                sort_up_down_button.setProperty('iconSource', 'resources/sort-from-top.png')
        else:
            print("Button 'sortUpDownButton' не найден!")

        # Восстанавливаем список экзаменов
        self.update_exams_list()

    @Slot()
    def on_window_closed(self):
        print("Окно настроек закрыто (либо пользователем, либо программно)")
        self.window = None
        self.searchSettingsClosed.emit()  # Уведомляем NewExamWindow о закрытии окна настроек

    @Slot(Exam)
    def on_exam_created(self, exam: Exam):
        """
        Слот, вызываемый при создании нового экзамена.
        Добавляет экзамен в список и обновляет модель.
        """
        print(f"Создан новый экзамен: {exam.name}")
        try:
            self.settings.exams.add_exam(exam)
            self.update_exams_list()
            self.updateModels.emit()  # Уведомляем Frontend об изменениях
        except Exception as e:
            print(f"Ошибка при добавлении экзамена {exam.name} в список:", e)

    @Slot()
    def update_exams_list(self):
        """
        Обновляет список экзаменов в QML.
        """
        chosen_user_exams_list = self.window.findChild(QObject, 'chosenUserExamsList')
        if chosen_user_exams_list:
            # Передаем в QML список экзаменов
            exams = self.settings.exams.to_model_dict()
            chosen_user_exams_list.setProperty('exams', exams)
        else:
            print("ListView 'chosenUserExamsList' не найден")

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

    @Slot()
    def on_op_name_changed(self):
        op_name = self.sender().property('text')  # Получаем текст из поля
        print(f"Название ОП введено: {op_name}")
        try:
            if op_name == "":
                self.settings.op_name = None
            else:
                self.settings.op_name = op_name
            self.updateModels.emit()
        except:
            print(f"Название ОП {op_name} не может быть задано! Сбросим до None")
            self.settings.op_name = None
            self.updateModels.emit()

    @Slot()
    def on_university_name_changed(self):
        university_name = self.sender().property('text')
        print(f"Название университета введено: {university_name}")
        try:
            if university_name == "":
                self.settings.university_name = None
            else:
                self.settings.university_name = university_name
            self.updateModels.emit()
        except:
            print(f"Название университета {university_name} не может быть задано! Сбросим до None")
            self.settings.university_name = None
            self.updateModels.emit()

    @Slot()
    def add_exam_button_clicked(self):
        print("Кнопка добавления экзамена нажата!")
        # Если окно уже создано и отображается, просто поднимаем его наверх
        if self.new_exam_window is None or self.new_exam_window.window is None:
            self.new_exam_window = NewExamWindow(self.engine, self.unique_values, self)
            self.new_exam_window.examCreated.connect(self.on_exam_created)
        else:
            try:
                self.new_exam_window.show()
            except Exception as e:
                print("Окно нового экзамена уже открыто:", e)

    @Slot()
    def on_main_window_closed(self):
        print("Главное окно закрыто, закрываем окно настроек")
        if self.window is not None:
            self.window.close()
            # self.on_window_closed() - выполняется автоматически

    # Обработчик сигнала из QML
    @Slot(str, str)
    def handleExamDeleted(self, exam_name, exam_type):
        print(f"Нажата кнопка удаления экзамена: {exam_name}, тип: {exam_type}")
        # Удаляем экзамен из списка
        self.settings.exams.delete_exam(exam_name, exam_type)
        # Обновляем список экзаменов
        self.update_exams_list()
        # Обновляем модели
        self.updateModels.emit()

    @Slot()
    def filter_by_exams_combobox_index_changed(self):
        filter_by_exams_combobox = self.sender()
        if filter_by_exams_combobox is not None:
            index = filter_by_exams_combobox.property('currentIndex')
            # Варианты: "Выключен", "Включен, без баллов", "Включен, с баллами"
            v = ["Выключен", "Включен, без баллов", "Включен, с баллами"]
            print(f"Выбранный индекс: {index}. Выбрано: {v[index]}")
            if index == 0:
                self.settings.filter_by_exams_and_score = False
                self.settings.filter_by_exams_not_score = False
            if index == 1:
                self.settings.filter_by_exams_and_score = False
                self.settings.filter_by_exams_not_score = True
            if index == 2:
                self.settings.filter_by_exams_and_score = True
                self.settings.filter_by_exams_not_score = False
            self.updateModels.emit()

    @Slot()
    def sort_op_var_combobox_index_changed(self):
        sort_op_var_combobox = self.sender()
        if sort_op_var_combobox is not None:
            index = sort_op_var_combobox.property('currentIndex')
            # Варианты: ["По умолчанию", "По рейтингу RAEX", "По стоимости", "По проходным"]
            v = ["По умолчанию", "По рейтингу RAEX", "По стоимости", "По проходным"]
            print(f"Выбранный индекс: {index}. Выбрано: {v[index]}")
            # "default" - без сортировки, "raex" - по рейтингу RAEX, "price" - по цене,
            # "ege_score" - по проходному баллу на бюджет или платное (в зависимости от show_budget_score)
            if index == 0:
                self.settings.sort_by = "default"
            if index == 1:
                self.settings.sort_by = "raex"
            if index == 2:
                self.settings.sort_by = "price"
            if index == 3:
                self.settings.sort_by = "ege_score"
            self.updateModels.emit()

    @Slot()
    def sort_up_down_button_clicked(self):
        print("Кнопка сортировки нажата!")
        sort_up_down_button = self.sender()
        if sort_up_down_button is not None:
            # Переключаем направление сортировки
            self.settings.sort_from_high_to_low = not self.settings.sort_from_high_to_low
            # Меняем иконку кнопки
            if self.settings.sort_from_high_to_low:
                sort_up_down_button.setProperty('iconSource', 'resources/sort-from-bottom.png')
                print("Выбрана сортировка от большего к меньшему")
            else:
                sort_up_down_button.setProperty('iconSource', 'resources/sort-from-top.png')
                print("Выбрана сортировка от меньшего к большему")
            self.updateModels.emit()
        else:
            print("sender() не найден")
