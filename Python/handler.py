from PySide6.QtCore import QObject, Slot

class PyHandler(QObject):
    @Slot(int, str, str)
    def handleCardClicked(self, index, opName, universityName):
        print(f"Клик по карточке: индекс={index}, ОП: {opName}, университет: {universityName}")
