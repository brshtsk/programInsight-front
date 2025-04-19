from PySide6.QtCore import QObject, Slot, Signal
from PySide6.QtQml import QQmlComponent
from utils import Utils
from unique_values import UniqueValues
from new_exam_window import NewExamWindow
from exam import Exam, UserExamsSet
from data_converter import DataConverter
from update_data.export_data import DataFrameExporter
from update_data.import_data import DataImporter


class UserCabinetWindow(QObject):
    newExamParentClosed = Signal()  # Сигнал для уведомления New Exam Window о закрытии окна ЛК
    addExamFailed = Signal()  # Сигнал для уведомления New Exam Window об ошибке при добавлении экзамена

    def __init__(self, engine, unique_values: UniqueValues, frontend_parent):
        super().__init__()
        self.engine = engine
        self.unique_values = unique_values
        self.frontend_parent = frontend_parent
        self.component = None
        self.window = None
        self.new_exam_window = None
        self.exams = UserExamsSet('cabinet')  # Инициализация списка экзаменов

        self.load_window()

        self.frontend_parent.mainWindowClosed.connect(self.on_main_window_closed)

    def load_window(self):
        settings_qml_path = Utils.resource_path('FirstPythonContent/UserCabinet.qml')
        self.component = QQmlComponent(self.engine, str(settings_qml_path))
        if self.component.status() == QQmlComponent.Ready:
            self.window = self.component.create()
            if self.window:
                self.window.show()
                self.connect_signals()
                self.restore_view()
                self.window.windowClosed.connect(self.on_window_closed)
            else:
                print("Не удалось создать окно ЛК.")
        else:
            print("Ошибка при загрузке UserCabinet.qml:", self.component.errorString())

    def connect_signals(self):
        # Кнопка добавления экзамена в список
        add_exam_button = self.window.findChild(QObject, 'addExamButton')
        if add_exam_button:
            add_exam_button.clicked.connect(self.add_exam_button_clicked)
        else:
            print("Button 'addExamButton' не найден")

        # Кнопка сохранения текущего списка экзаменов
        save_profile_exams_button = self.window.findChild(QObject, 'saveProfileExamsButton')
        if save_profile_exams_button:
            save_profile_exams_button.clicked.connect(self.save_profile_exams_button_clicked)
        else:
            print("Button 'saveProfileExamsButton' не найден")

    def restore_view(self):
        """
        Восстанавливает состояние окна, если оно было закрыто.
        """
        try:
            path = Utils.resource_path("user_data/user_exams.json")
            importer = DataImporter(path)
            model_dict = importer.from_json_to_list_of_dicts()
            self.exams.load_from_model_dict(model_dict)
        except Exception as e:
            print("Ошибка при восстановлении состояния ЛК:", e)

        chosen_user_exams_list = self.window.findChild(QObject, 'chosenUserExamsList')
        if chosen_user_exams_list:
            chosen_user_exams_list.setProperty('exams', self.exams.to_model_dict())
        else:
            print("ListView 'chosenUserExamsList' не найден")

    # Вызывается обработчиком сигнала из QML
    def delete_exam(self, exam_name, exam_type):
        # Удаляем экзамен из списка
        self.exams.delete_exam(exam_name, exam_type)
        # Обновляем список экзаменов
        self.update_exams_list()

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

    @Slot(Exam)
    def on_exam_created(self, exam: Exam):
        """
        Слот, вызываемый при создании нового экзамена.
        Добавляет экзамен в список и обновляет модель.
        """
        print(f"Получен новый экзамен: {exam.name}")
        try:
            self.exams.add_exam(exam)
            self.update_exams_list()
        except Exception as e:
            print(f"Ошибка при добавлении экзамена {exam.name} в список:", e)
            self.addExamFailed.emit()

    @Slot()
    def update_exams_list(self):
        """
        Обновляет список экзаменов в QML.
        """
        chosen_user_exams_list = self.window.findChild(QObject, 'chosenUserExamsList')
        if chosen_user_exams_list:
            # Передаем в QML список экзаменов
            exams = self.exams.to_model_dict()
            chosen_user_exams_list.setProperty('exams', exams)
        else:
            print("ListView 'chosenUserExamsList' не найден")

    @Slot()
    def save_profile_exams_button_clicked(self):
        """
        Слот, вызываемый при нажатии кнопки сохранения списка экзаменов.
        """
        print("Сохраняем список экзаменов!")
        df = DataConverter.exams_set_to_dataframe(self.exams)
        path = Utils.resource_path("user_data/user_exams.json")
        try:
            exporter = DataFrameExporter(df, path)
            exporter.to_json()
            print("Список экзаменов успешно сохранен в", path)
        except Exception as e:
            print("Ошибка при сохранении списка экзаменов:", e)

    @Slot()
    def on_window_closed(self):
        print("Окно ЛК закрыто (либо пользователем, либо программно)")
        self.window = None
        self.newExamParentClosed.emit()  # Уведомляем NewExamWindow о закрытии окна настроек

    @Slot()
    def on_main_window_closed(self):
        print("Главное окно закрыто, закрываем окно настроек")
        if self.window is not None:
            self.window.close()
            # self.on_window_closed() - выполняется автоматически
