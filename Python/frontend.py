from PySide6.QtCore import QObject, Slot
from op_list_data import CustomListModel, data  # Импорт модели и данных


class Frontend(QObject):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self.model = CustomListModel(data)  # Создаём модель
        self.setup_connections()

    def setup_connections(self):
        # Получаем корневой объект
        root_object = self.engine.rootObjects()[0]

        # Передаём модель в контекст QML
        context = self.engine.rootContext()
        context.setContextProperty("customModel", self.model)

        # Ищем кнопку и подключаем Python-метод
        button = root_object.findChild(QObject, 'button')

        if button:
            button.clicked.connect(self.button_clicked)
        else:
            print('Кнопка не найдена!')

    @Slot()
    def button_clicked(self):
        print('Кнопка нажата!')
