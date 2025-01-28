import os
import sys
from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from autogen.settings import url, import_paths
from frontend import Frontend


def resource_path(relative_path):
    """Возвращает абсолютный путь к ресурсу, работает как в режиме разработки, так и в собранном .exe"""
    try:
        # PyInstaller временно создает папку и сохраняет путь в _MEIPASS
        base_path = Path(sys._MEIPASS)
    except AttributeError:
        base_path = Path(__file__).parent.parent
    return base_path / relative_path


if __name__ == '__main__':
    # Установка политики масштабирования через переменные окружения
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
    os.environ["QT_FONT_DPI"] = "96"

    # Устанавливаем PassThrough для контроля над DPI **до** создания приложения
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    # Создаём экземпляр приложения
    app = QGuiApplication(sys.argv)

    # Создаём движок QML
    engine = QQmlApplicationEngine()

    # Определяем базовый путь
    app_dir = resource_path("")
    print(f"Base Directory: {app_dir}")  # Отладочный вывод

    # Добавляем пути для импорта QML
    engine.addImportPath(str(app_dir))
    for path in import_paths:
        full_path = app_dir / path
        print(f"Adding Import Path: {full_path}")  # Отладочный вывод
        engine.addImportPath(str(full_path))

    # Загружаем основной QML файл
    main_qml = resource_path(url)
    print(f"Loading QML File: {main_qml}")  # Отладочный вывод
    engine.load(str(main_qml))

    if not engine.rootObjects():
        print("Failed to load QML file.")  # Отладочный вывод
        sys.exit(-1)

    # Инициализируем фронтенд
    frontend = Frontend(engine)

    # Запускаем цикл приложения
    sys.exit(app.exec())
