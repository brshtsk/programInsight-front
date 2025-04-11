from utils import Utils
from PySide6.QtCore import QObject, Slot
from PySide6.QtQml import QQmlComponent
from PySide6.QtCore import QUrl


class PyHandler(QObject):
    def __init__(self, engine, frontend_parent):
        super().__init__()
        self.engine = engine
        self.frontend_parent = frontend_parent
        self.components = []
        self.windows = []

        self.frontend_parent.mainWindowClosed.connect(self.on_main_window_closed)

    @Slot(int, str, str, str, str, str, str, str, int, int, int, int, int, list, list, str)
    def handleCardClicked(self, index, op_name, university_name, op_type, length_text,
                          location_text, attendance_text, price_text, raex_position, budget_score,
                          paid_score, budget_places, paid_places, single_exams, choice_exams, image_source):
        print(f"Клик по карточке: индекс={index}, ОП: {op_name}, университет: {university_name}, "
              f"тип: {op_type}, длина: {length_text}, локация: {location_text}, "
              f"посещаемость: {attendance_text}, стоимость: {price_text},\n"
              f"raexPosition: {raex_position},"
              f"бюджетный балл: {budget_score}, платный балл: {paid_score}, "
              f"бюджетных мест: {budget_places}, платных мест: {paid_places}, "
              f"экзамены без выбора: {single_exams}, экзамены с выбором: {choice_exams},\n"
              f"изображение: {image_source}")

        # Открываем окно с информацией об ОП
        self.showOpWidget(
            op_name,  # opNameText
            length_text,  # opTimeText
            university_name,  # universityNameText
            location_text,  # opLocationText
            "Не в топ-100 RAEX" if (raex_position == 0 or raex_position > 100) else f"На {raex_position} месте в RAEX",
            # opRatingText
            attendance_text,  # opAttendanceText
            price_text + " за год обучения",  # opPriceText (значение можно задать по необходимости)
            "-" if (not budget_score) else budget_score,  # budgetScoreText
            "-" if (not paid_score) else paid_score,  # paidScoreText
            op_type,  # opTypeText
            budget_places,  # budgetPlacesText
            paid_places,  # paidPlacesText
            image_source,  # imageSource
            single_exams,  # для ListView
            choice_exams  # для ListView
        )

    def showOpWidget(self, op_name, op_time, university_name, op_location, op_rating,
                     op_attendance, op_price, budget_score, paid_score, op_type,
                     budget_places, paid_places, image_source, single_exams, choice_exams):
        """
        Создает и показывает QML-виджет с информацией об ОП.
        Все аргументы - str, либо список строк (для экзаменов).
        """
        widget_qml_path = Utils.resource_path('FirstPythonContent/OpWidget.qml')
        component = QQmlComponent(self.engine, QUrl.fromLocalFile(str(widget_qml_path)))

        # Сохраняем компонент в списке, чтобы в будущем можно было его удалить
        self.components.append(component)

        if component.status() == QQmlComponent.Ready:
            window = component.create()
            if window:
                # Сохраняем ссылку на окно в списке для предотвращения сборки мусора
                self.windows.append(window)
                text_fields = {
                    "opNameText": op_name,
                    "opTimeText": op_time,
                    "universityNameText": university_name,
                    "opLocationText": op_location,
                    "opRatingText": op_rating,
                    "opAttendanceText": op_attendance,
                    "opPriceText": op_price,
                    "budgetScoreText": budget_score,
                    "paidScoreText": paid_score,
                    "opTypeText": op_type,
                    "budgetPlacesText": budget_places,
                    "paidPlacesText": paid_places,
                }
                for field, text in text_fields.items():
                    element = window.findChild(QObject, field)
                    if element:
                        element.setProperty("text", text)
                    else:
                        print(f"Элемент \'{field}\' не найден")

                university_image = window.findChild(QObject, "universityImage")
                if university_image:
                    university_image.setProperty("source", image_source)
                else:
                    print("Элемент 'universityImage' не найден")

                # Передача single_exams в ListView.
                single_exam_list_view = window.findChild(QObject, "singleExamListView")
                if single_exam_list_view:
                    exams = []
                    for exam in single_exams:
                        exams.append({"examNameText": exam})

                    single_exam_list_view.setProperty("exams", exams)
                else:
                    print("Элемент 'singleExamListView' не найден")

                choice_exam_list_view = window.findChild(QObject, "choiceExamListView")
                if choice_exam_list_view:
                    exam_options = []
                    for var in choice_exams:
                        new_option = {"header": f"Выбор из {len(var)} предметов", "options": []}
                        for exam in var:
                            new_option["options"].append({"optionNameText": exam})
                        exam_options.append(new_option)
                    choice_exam_list_view.setProperty("examOptions", exam_options)
                else:
                    print("Элемент 'choiceExamListView' не найден")

                window.show()
            else:
                print("Не удалось создать окно.")
        else:
            print("Ошибка при загрузке OpWidget.qml:", component.errorString())

    @Slot()
    def on_main_window_closed(self):
        """
        Слот, вызываемый при закрытии главного окна.
        Закрывает все дочерние окна и очищает список компонентов.
        """
        for window in self.windows:
            if window:
                try:
                    window.destroy()
                    print("Карточка ОП закрыта вслед за закрытием главного окна.")
                except:
                    print("Не удалось закрыть карточку ОП. Вероятно, она уже закрыта.")
        self.components.clear()
        self.windows.clear()
