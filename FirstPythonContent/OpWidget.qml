import QtQuick
import QtQuick.Window
import FirstPython

Window {
    width: opWidgetScreen.width
    height: opWidgetScreen.height

    // Фиксированные размеры
    minimumWidth: width
    maximumWidth: width
    minimumHeight: height
    maximumHeight: height

    visible: true
    title: "OpWidget"

    signal windowClosed()  // Пользовательский сигнал закрытия

    // Отслеживаем изменение свойства visible:
    onVisibleChanged: {
        if (!visible) {
            windowClosed()
        }
    }

    OpWidgetScreen {
        id: opWidgetScreen
    }

}
