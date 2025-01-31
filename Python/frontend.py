from PySide6.QtCore import QObject, Slot
from op_model import opListModel, data
from statistics_model import StatisticsListModel, statistics_data  # Импорт новой модели


class Frontend(QObject):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self.op_model = opListModel(data)  # Создаём модель
        self.statistics_model = StatisticsListModel(statistics_data)
        self.setup_connections()

    def setup_connections(self):
        # Получаем корневой объект
        root_object = self.engine.rootObjects()[0]

        # Передаём модель в контекст QML
        context = self.engine.rootContext()
        context.setContextProperty("opModel", self.op_model)
        context.setContextProperty("statisticsModel", self.statistics_model)

        # Ищем кнопку и подключаем Python-метод
        button = root_object.findChild(QObject, 'button')

        if button:
            button.clicked.connect(self.button_clicked)
        else:
            print('Кнопка не найдена!')

    @Slot()
    def button_clicked(self):
        print('Кнопка нажата!')
