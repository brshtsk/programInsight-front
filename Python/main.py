import os
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from autogen.settings import url, import_paths
from frontend import Frontend
from utils import Utils

# Чтобы Nuitka сгенерировал зависимость от этих C-расширений:
import sklearn.neighbors._quad_tree
import sklearn.tree._partitioner

if __name__ == '__main__':
    # Кнопки не в стиле Windows
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Basic"
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
    app_dir = Utils.resource_path("")
    print(f"Base Directory: {app_dir}")  # Отладочный вывод

    # Добавляем пути для импорта QML
    engine.addImportPath(str(app_dir))
    for path in import_paths:
        full_path = app_dir / path
        print(f"Adding Import Path: {full_path}")  # Отладочный вывод
        engine.addImportPath(str(full_path))

    # Загружаем основной QML файл
    main_qml = Utils.resource_path(url)
    print(f"Loading QML File: {main_qml}")  # Отладочный вывод
    engine.load(str(main_qml))

    if not engine.rootObjects():
        print("Failed to load QML file.")  # Отладочный вывод
        sys.exit(-1)

    # Инициализируем фронтенд
    frontend = Frontend(engine)

    # Запускаем цикл приложения
    sys.exit(app.exec())
