from PySide6.QtCore import QObject, Slot, QUrl
from PySide6.QtQml import QQmlComponent
from utils import Utils
from unique_values import UniqueValues
from exam import Exam


class NewExamWindow(QObject):
    def __init__(self, engine, unique_values: UniqueValues, search_settings_window_parent):
        super().__init__()
        self.engine = engine
        self.unique_values = unique_values
        self.search_settings_window_parent = search_settings_window_parent
        self.component = None
        self.window = None
        self.load_window()

        self.search_settings_window_parent.searchSettingsClosed.connect(self.on_search_settings_closed)

    def load_window(self):
        exam_card_path = Utils.resource_path('FirstPythonContent/NewExamProperties.qml')
        self.component = QQmlComponent(self.engine, QUrl.fromLocalFile(str(exam_card_path)))
        if self.component.status() == QQmlComponent.Ready:
            self.window = self.component.create()
            if self.window:
                self.window.show()
                self.connect_signals()
                self.set_properties()
                self.window.windowClosed.connect(self.on_window_closed)
            else:
                print("Не удалось создать окно NewExamProperties.")
        else:
            print("Ошибка при загрузке NewExamProperties.qml:", self.component.errorString())

    @Slot()
    def on_window_closed(self):
        """Слот, вызываемый при закрытии окна, чтобы очистить ссылку."""
        print("Окно NewExamProperties закрыто (либо пользователем, либо программно)")
        self.window = None

    @Slot()
    def connect_signals(self):
        # Ввод названия предмета
        exam_name_text_field = self.window.findChild(QObject, 'examNameTextField')
        if exam_name_text_field:
            exam_name_text_field.userTextChanged.connect(self.on_exam_name_changed)
        else:
            print("Поле ввода названия экзамена не найдено!")

        # Выбор типа экзамена
        exam_type_combobox = self.window.findChild(QObject, 'examTypeComboBox')
        if exam_type_combobox:
            exam_type_combobox.currentIndexChanged.connect(self.exam_type_combobox_index_changed)
        else:
            print("ComboBox 'examTypeComboBox' не найден!")

        # Ввод баллов за экзамен
        exam_score_text_field = self.window.findChild(QObject, 'examScoreTextField')
        if exam_score_text_field:
            exam_score_text_field.textChanged.connect(self.on_exam_score_changed)
        else:
            print("Поле ввода баллов экзамена не найдено!")

        # Сохранение экзамена
        save_exam_button = self.window.findChild(QObject, 'saveExamButton')
        if save_exam_button:
            save_exam_button.clicked.connect(self.on_save_exam_button_clicked)
        else:
            print("Кнопка 'saveExamButton' не найдена!")

    def set_properties(self):
        """
        Устанавливает свойства для элементов интерфейса.
        Например, если пользователь выбирает 'ЕГЭ/ДВИ',
        то в поле ввода будут предложены только экзамены бакалавриата.
        """
        exam_type_index = None

        exam_type_combobox = self.window.findChild(QObject, 'examTypeComboBox')
        if exam_type_combobox is not None:
            exam_type_index = exam_type_combobox.property('currentIndex')
        else:
            print("ComboBox 'examTypeComboBox' не найден!")

        if exam_type_index is not None:
            print('Настройка подсказок в examNameTextField')
            if exam_type_index == 0:
                # 0 - 'ЕГЭ/ДВИ'
                exam_name_text_field = self.window.findChild(QObject, 'examNameTextField')
                if exam_name_text_field:
                    exam_name_text_field.setProperty('editable', True)
                    exam_name_text_field.setProperty('availableValues', list(self.unique_values.subjects_bak_or_spec))
                    exam_name_text_field.setProperty('text', "")
                    print('Успешно установлены значения для examNameTextField (ЕГЭ/ДВИ)')
                else:
                    print("ComboBox 'examNameTextField' не найден!")
            if exam_type_index == 1:
                # 1 - 'Доп баллы ЕГЭ'

                # Если пользователь выбирает 'Доп баллы ЕГЭ',
                # то единственное доступное название - 'Личные достижения'.
                # Его также автоматически добавляем в поле ввода.
                exam_name_text_field = self.window.findChild(QObject, 'examNameTextField')
                if exam_name_text_field:
                    exam_name_text_field.setProperty('editable', False)
                    exam_name_text_field.setProperty('availableValues', ["Личные достижения"])
                    exam_name_text_field.setProperty('disableCompleterNow', True)
                    exam_name_text_field.setProperty('text', "Личные достижения")
                    print('Успешно установлены значения для examNameTextField (Доп баллы ЕГЭ)')
                else:
                    print("ComboBox 'examNameTextField' не найден!")
            if exam_type_index == 2:
                # 2 - 'Магистратура'
                exam_name_text_field = self.window.findChild(QObject, 'examNameTextField')
                if exam_name_text_field:
                    exam_name_text_field.setProperty('editable', True)
                    exam_name_text_field.setProperty('availableValues', list(self.unique_values.subjects_mag))
                    exam_name_text_field.setProperty('text', "")
                    print('Успешно установлены значения для examNameTextField (Магистратура)')
                else:
                    print("ComboBox 'examNameTextField' не найден!")

    @Slot()
    def on_exam_name_changed(self):
        exam_name = self.sender().property('text')  # Получаем текст из поля
        print(f"Введено название экзамена: {exam_name}")

    @Slot()
    def exam_type_combobox_index_changed(self):
        exam_type_combobox = self.sender()
        if exam_type_combobox is not None:
            index = exam_type_combobox.property('currentIndex')
            # 0 - 'ЕГЭ/ДВИ', 1 - 'Доп баллы ЕГЭ', 2 - 'Магистратура'
            print(f"Выбран тип экзамена: {index} ({['ЕГЭ/ДВИ', 'Доп баллы ЕГЭ', 'Магистратура'][index]})")
            window = exam_type_combobox.property('window')
            self.set_properties()
        else:
            print("sender() не найден!")

    @Slot()
    def on_search_settings_closed(self):
        """
        Слот, вызываемый при закрытии окна настроек поиска.
        Закрывает текущее окно NewExamWindow, если оно открыто.
        """
        print("Окно настроек поиска закрыто, закрываем NewExamWindow")
        if self.window is not None:
            self.window.close()

    @Slot()
    def on_exam_score_changed(self):
        """
        Слот, вызываемый при изменении текста в поле ввода баллов экзамена.
        Получает текст из поля и преобразует его в целое число.
        """
        exam_score_text_field = self.sender()
        if exam_score_text_field is not None:
            score_text = exam_score_text_field.property('text')
            try:
                score = int(score_text)
                print(f"Получены баллы экзамена: {score}")
            except ValueError:
                print("Некорректный ввод баллов экзамена!")
        else:
            print("Поле ввода баллов экзамена не найдено!")

    @Slot()
    def on_save_exam_button_clicked(self):
        """
        Слот, вызываемый при нажатии кнопки "Сохранить экзамен".
        Получает данные из полей ввода и создает объект Exam.
        """
        exam_name_text_field = self.window.findChild(QObject, 'examNameTextField')
        if exam_name_text_field is not None:
            exam_name = exam_name_text_field.property('text')
            print(f"Получено название экзамена: {exam_name}")
        else:
            print("Поле ввода названия экзамена не найдено!")

        exam_score_text_field = self.window.findChild(QObject, 'examScoreTextField')
        if exam_score_text_field is not None:
            score_text = exam_score_text_field.property('text')
            try:
                if score_text == "":
                    score = None
                else:
                    score = int(score_text)
                print(f"Получены баллы экзамена: {score}")
            except ValueError:
                print("Некорректный ввод баллов экзамена!")
                return
        else:
            print("Поле ввода баллов экзамена не найдено!")
            return

        exam_type_combobox = self.window.findChild(QObject, 'examTypeComboBox')
        if exam_type_combobox is not None:
            exam_type_index = exam_type_combobox.property('currentIndex')
            print(f"Получен тип экзамена: {exam_type_index}")
        else:
            print("ComboBox 'examTypeComboBox' не найден!")

        # Создаем объект Exam
        try:
            if exam_type_index == 0:
                # 0 - 'ЕГЭ/ДВИ'
                qualification = "ЕГЭ/ДВИ"
            elif exam_type_index == 1:
                # 1 - 'Доп баллы ЕГЭ'
                qualification = "Доп баллы ЕГЭ"
            elif exam_type_index == 2:
                # 2 - 'Магистратура'
                qualification = "Магистратура"
            else:
                raise ValueError("Недопустимый индекс типа экзамена")

            new_exam = Exam(exam_name, qualification, score, self.unique_values)
            print(f"Создан новый экзамен: {new_exam.name}, {new_exam.qualification}, {new_exam.score}")
        except Exception as e:
            print("Ошибка при создании экзамена:", e)
