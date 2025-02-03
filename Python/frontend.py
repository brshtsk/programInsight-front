from PySide6.QtCore import QObject, Slot, QUrl, Signal
from PySide6.QtQml import QQmlComponent
from op_model import opListModel
from statistics_model import StatisticsListModel
from get_json_data import get_op_model_data
from utils import resource_path


class Frontend(QObject):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        op_data, statistics_data = get_op_model_data(resource_path('Python\op_data.json'))
        self.op_model = opListModel(op_data)
        self.statistics_model = StatisticsListModel(statistics_data)
        self.setup_connections()

    def setup_connections(self):
        root_object = self.engine.rootObjects()[0]
        context = self.engine.rootContext()
        context.setContextProperty("opModel", self.op_model)
        context.setContextProperty("statisticsModel", self.statistics_model)

        # Подключаемся к кнопке
        button = root_object.findChild(QObject, 'searchSettingsButton')
        if button:
            button.clicked.connect(self.button_clicked)
        else:
            print('Кнопка не найдена!')

        # Подключаемся к ComboBox
        combo_box = root_object.findChild(QObject, 'scoreTypeComboBox')
        if combo_box:
            combo_box.currentIndexChanged.connect(self.combobox_index_changed)
        else:
            print('ComboBox не найден!')

    @Slot()
    def button_clicked(self):
        print('Кнопка настроек поиска нажата!')
        settings_qml_path = resource_path('FirstPythonContent/SearchSettings.qml')
        component = QQmlComponent(self.engine, QUrl.fromLocalFile(str(settings_qml_path)))
        if component.status() == QQmlComponent.Ready:
            settings_window = component.create()
            if settings_window:
                settings_window.show()
            else:
                print("Не удалось создать окно настроек.")
        else:
            print("Ошибка при загрузке SearchSettings.qml:", component.errorString())

    @Slot(int)
    def combobox_index_changed(self, index):
        print(f"Индекс ComboBox изменен, новый индекс: {index}")
