from pathlib import Path
import sys


def resource_path(relative_path):
    """
    Возвращает абсолютный путь к ресурсу,
    работает как в режиме разработки, так и в собранном .exe
    """
    try:
        # PyInstaller временно создает папку и сохраняет путь в _MEIPASS
        base_path = Path(sys._MEIPASS)
    except AttributeError:
        base_path = Path(__file__).parent.parent
    return base_path / relative_path
