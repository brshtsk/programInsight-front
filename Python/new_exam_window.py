from PySide6.QtCore import QObject, Slot, QUrl
from PySide6.QtQml import QQmlComponent
from utils import Utils
from unique_values import UniqueValues

class NewExamWindow(QObject):
    def __init__(self, engine, unique_values: UniqueValues):
        super().__init__()
        self.engine = engine
        self.unique_values = unique_values
        self.component = None
        self.window = None
        self.load_window()

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
        print("Окно NewExamProperties закрыто")
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
