from utils import Utils
from PySide6.QtCore import QObject, Slot
from PySide6.QtQml import QQmlComponent
from PySide6.QtCore import QUrl
from op_card_models.exam_list_model import ExamListModel


class PyHandler(QObject):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine

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
            "Не в топ-10 RAEX" if (raex_position == 0 or raex_position > 10) else f"Входит в топ-{raex_position} RAEX",
            # opRatingText
            attendance_text,  # opAttendanceText
            price_text + " за год обучения",  # opPriceText (значение можно задать по необходимости)
            budget_score,  # budgetScoreText
            paid_score,  # paidScoreText
            op_type,  # opTypeText
            budget_places,  # budgetPlacesText
            paid_places,  # paidPlacesText
            image_source,  # imageSource
            single_exams # для ListView
        )

    def showOpWidget(self, op_name, op_time, university_name, op_location, op_rating,
                     op_attendance, op_price, budget_score, paid_score, op_type,
                     budget_places, paid_places, image_source, single_exams):
        """
        Создает и показывает QML-виджет с информацией об ОП.
        Все аргументы - str.
        """
        widget_qml_path = Utils.resource_path('FirstPythonContent/OpWidget.qml')
        component = QQmlComponent(self.engine, QUrl.fromLocalFile(str(widget_qml_path)))
        if component.status() == QQmlComponent.Ready:
            window = component.create()
            if window:
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
                    current_model = single_exam_list_view.property("model")
                    if current_model and hasattr(current_model, "updateData"):
                        current_model.updateData(single_exams)
                    else:
                        exam_model = ExamListModel(single_exams)
                        single_exam_list_view.setProperty("model", exam_model)
                else:
                    print("Элемент 'singleExamListView' не найден")

                window.show()
            else:
                print("Не удалось создать окно.")
        else:
            print("Ошибка при загрузке OpWidget.qml:", component.errorString())
