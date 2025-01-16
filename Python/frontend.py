from PySide6.QtCore import QObject, Slot


class Frontend(QObject):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self.setup_connections()

    def setup_connections(self):
        # Получаем корневой объект
        root_object = self.engine.rootObjects()[0]

        # Ищем кнопку и подключаем Python-метод
        button = root_object.findChild(QObject, 'button')

        if button:
            button.clicked.connect(self.button_clicked)
        else:
            print('Кнопка не найдена!')

    @Slot()
    def button_clicked(self):
        print('Кнопка нажата!')
