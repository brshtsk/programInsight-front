import os
import sys
from pathlib import Path

from PySide6.QtCore import Qt, QObject, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from autogen.settings import url, import_paths


class Backend(QObject):
    @Slot()
    def button_clicked(self):
        print('Кнопка нажата!')


if __name__ == '__main__':

    # Установка политики масштабирования
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
    os.environ["QT_FONT_DPI"] = "96"  # Устанавливаем фиксированный DPI для шрифтов
    app = QGuiApplication(sys.argv)

    # Устанавливаем PassThrough для контроля над DPI
    app.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    engine = QQmlApplicationEngine()

    app_dir = Path(__file__).parent.parent

    engine.addImportPath(os.fspath(app_dir))
    for path in import_paths:
        engine.addImportPath(os.fspath(app_dir / path))

    engine.load(os.fspath(app_dir / url))
    if not engine.rootObjects():
        sys.exit(-1)

    # Получаем корневой объект
    root_object = engine.rootObjects()[0]

    # Ищем кнопку и подключаем Python-метод
    button = root_object.findChild(QObject, 'button')
    backend = Backend()

    if button:
        button.clicked.connect(backend.button_clicked)
    else:
        print('Кнопка не найдена!')

    sys.exit(app.exec())
