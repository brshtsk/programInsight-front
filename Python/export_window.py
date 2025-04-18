from PySide6.QtCore import QObject, Slot, Signal
from PySide6.QtQml import QQmlComponent
from utils import Utils
from data_converter import DataConverter
from update_data.export_data import DataFrameExporter


class ExportWindow(QObject):
    def __init__(self, engine, frontend_parent):
        super().__init__()
        self.engine = engine
        self.frontend_parent = frontend_parent
        self.component = None
        self.window = None
        self.format = "XLSX"

        self.load_window()

        self.frontend_parent.mainWindowClosed.connect(self.on_main_window_closed)

    def load_window(self):
        settings_qml_path = Utils.resource_path('FirstPythonContent/Export.qml')
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
        # Выбор формата для экспорта
        format_type_combobox = self.window.findChild(QObject, 'formatTypeComboBox')
        if format_type_combobox:
            format_type_combobox.currentIndexChanged.connect(self.format_type_combobox_index_changed)
        else:
            print("Комбобокс формата не найден!")

        # Кнопка экспорта
        export_button = self.window.findChild(QObject, 'exportButton')
        if export_button:
            export_button.clicked.connect(self.export_button_clicked)
        else:
            print("Кнопка экспорта не найдена!")

    @Slot()
    def format_type_combobox_index_changed(self):
        format_type_combobox = self.window.findChild(QObject, 'formatTypeComboBox')
        if format_type_combobox:
            index = format_type_combobox.property('currentIndex')
            v = ["XLSX", "CSV", "JSON"]
            print("Выбранный формат:", v[index])
            self.format = v[index]
        else:
            print("Комбобокс формата не найден!")

    @Slot()
    def export_button_clicked(self):
        print("Кнопка выгрузки данных нажата!")
        # Здесь можно добавить логику для обработки нажатия кнопки экспорта
        # Например, вызвать метод для экспорта данных в выбранном формате
        self.export_data()

    def export_data(self):
        df = DataConverter.list_op_to_dataframe(self.frontend_parent.filtered_op_list)
        if df.empty:
            # Информируем пользователя, что нет данных для экспорта
            self.inform("Нет данных для экспорта")
            self.hide_path()
            return

        try:
            if self.format == "XLSX":
                path = Utils.resource_path("export/export.xlsx")
                exporter = DataFrameExporter(df, path)
                exporter.to_excel()
                self.inform(f"Данные экспортированы в")
                self.show_path(path)
            if self.format == "CSV":
                path = Utils.resource_path("export/export.csv")
                exporter = DataFrameExporter(df, path)
                exporter.to_csv()
                self.inform(f"Данные экспортированы в")
                self.show_path(path)
            if self.format == "JSON":
                path = Utils.resource_path("export/export.json")
                exporter = DataFrameExporter(df, path)
                exporter.to_json()
                self.inform(f"Данные экспортированы в")
                self.show_path(path)
        except Exception as e:
            print("Ошибка при экспорте данных:", e)
            self.inform("Ошибка при экспорте данных")
            self.hide_path()

    def inform(self, text):
        info_text = self.window.findChild(QObject, 'infoText')
        if info_text:
            info_text.setProperty('text', text)
        else:
            print("Не удалось найти элемент infoText для отображения сообщения.")

    def show_path(self, path):
        path_text_flickable = self.window.findChild(QObject, 'pathTextFlickable')
        if path_text_flickable:
            path_text_flickable.setProperty('visible', True)
        else:
            print("Не удалось найти элемент pathTextFlickable для отображения пути.")

        path_text = self.window.findChild(QObject, 'pathText')
        if path_text:
            path_text.setProperty('text', str(path))
        else:
            print("Не удалось найти элемент pathText для отображения пути.")

    def hide_path(self):
        path_text_flickable = self.window.findChild(QObject, 'pathTextFlickable')
        if path_text_flickable:
            path_text_flickable.setProperty('visible', False)
        else:
            print("Не удалось найти элемент pathTextFlickable для скрытия пути.")

    @Slot()
    def on_window_closed(self):
        """Слот, вызываемый при закрытии окна, чтобы очистить ссылку."""
        print("Окно ExportWindow закрыто (либо пользователем, либо программно)")
        self.window = None

    @Slot()
    def on_main_window_closed(self):
        print("Главное окно закрыто, закрываем окно экспорта")
        if self.window is not None:
            self.window.close()
            # self.on_window_closed() - выполняется автоматически
