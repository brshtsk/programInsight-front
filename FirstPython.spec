# FirstPython.spec
import sys
import os
from pathlib import Path
from PyInstaller.utils.hooks import collect_all

# Определяем базовую директорию проекта
base_dir = Path(sys.argv[0]).parent

# Собираем все необходимые данные из PySide6
datas = []
binaries = []
hiddenimports = []

# Добавляем QML-файлы и другие ресурсы
def collect_qml_data(folder):
    qml_folder = base_dir / folder
    if qml_folder.exists():
        for root, dirs, files in os.walk(qml_folder):
            for file in files:
                file_path = Path(root) / file
                relative_path = file_path.relative_to(base_dir)
                datas.append((str(file_path), str(relative_path.parent)))

# Добавляем все необходимые папки
collect_qml_data("FirstPython/designer")
collect_qml_data("FirstPython/FirstPythonContent")
collect_qml_data("FirstPython/Python/autogen")
# Добавьте другие папки по необходимости

# Путь к основному скрипту
main_script = "Python/main.py"

# Импортируем необходимые классы для спецификации
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT

a = Analysis(
    [main_script],
    pathex=[str(base_dir)],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name="ProgramInsight",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Установите False, если не хотите консольное окно
)

# Собираем все в один пакет
COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="ProgramInsight",
)