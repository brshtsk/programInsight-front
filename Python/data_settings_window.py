from PySide6.QtCore import QObject, Slot, Signal
from PySide6.QtQml import QQmlComponent
from utils import Utils
from update_data.download_db import Downloader


class DataSettingsWindow(QObject):
    def __init__(self, engine, frontend_parent):
        super().__init__()
        self.engine = engine
        self.frontend_parent = frontend_parent
        self.component = None
        self.window = None

        self.load_window()

        self.frontend_parent.mainWindowClosed.connect(self.on_main_window_closed)

    def load_window(self):
        settings_qml_path = Utils.resource_path('FirstPythonContent/DataSettings.qml')
        self.component = QQmlComponent(self.engine, str(settings_qml_path))
        if self.component.status() == QQmlComponent.Ready:
            self.window = self.component.create()
            if self.window:
                self.window.show()
                self.connect_signals()
                self.window.windowClosed.connect(self.on_window_closed)
            else:
                print("Не удалось создать окно настроек.")
        else:
            print("Ошибка при загрузке SearchSettings.qml:", self.component.errorString())

    def connect_signals(self):
        # Обновить данные
        update_button = self.window.findChild(QObject, 'updateButton')
        if update_button:
            update_button.clicked.connect(self.update_button_clicked)
        else:
            print("Кнопка обновления данных не найдена!")

    @Slot()
    def update_button_clicked(self):
        self.inform("Загрузка данных...")
        try:
            path = Utils.resource_path('Python/data_sci_programs.json')
            Downloader.download_from_github(
                "https://github.com/Egor1025/data-sci-analytics/blob/main/data/data-sci-programs.json",
                path)
            print("Данные загружены по пути:", path)
            self.inform("Данные загружены!<br>Перезапустите приложение")
        except Exception as e:
            print("Обновление прервано!<br>Проверьте подключение", e)
            self.inform("Ошибка при загрузке данных!<br>Проверьте подключение")

    def inform(self, text):
        info_text = self.window.findChild(QObject, 'infoText')
        if info_text:
            info_text.setProperty('text', text)
        else:
            print("Не удалось найти элемент infoText для отображения сообщения.")

    @Slot()
    def on_window_closed(self):
        """Слот, вызываемый при закрытии окна, чтобы очистить ссылку."""
        print("Окно DataSettings закрыто (либо пользователем, либо программно)")
        self.window = None

    @Slot()
    def on_main_window_closed(self):
        print("Главное окно закрыто, закрываем окно настроек данных")
        if self.window is not None:
            self.window.close()
            # self.on_window_closed() - выполняется автоматически
