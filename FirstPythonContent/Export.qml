import QtQuick
import QtQuick.Window
import FirstPython

Window {
    width: exportScreen.width
    height: exportScreen.height

    // Фиксированные размеры
    minimumWidth: width
    maximumWidth: width
    minimumHeight: height
    maximumHeight: height

    visible: true
    title: "Export"

    signal windowClosed()  // Пользовательский сигнал закрытия

    // Отслеживаем изменение свойства visible:
    onVisibleChanged: {
        if (!visible) {
            windowClosed()
        }
    }

    ExportScreen {
        id: exportScreen
    }

}
