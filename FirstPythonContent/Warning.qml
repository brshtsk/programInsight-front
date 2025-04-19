import QtQuick
import QtQuick.Window
import FirstPython

Window {
    width: warningScreen.width
    height: warningScreen.height

    // Фиксированные размеры
    minimumWidth: width
    maximumWidth: width
    minimumHeight: height
    maximumHeight: height

    visible: true
    title: "Warning"

    signal windowClosed()  // Пользовательский сигнал закрытия

    // Отслеживаем изменение свойства visible:
    onVisibleChanged: {
        if (!visible) {
            windowClosed()
        }
    }

    WarningScreen {
        id: warningScreen
    }

}
