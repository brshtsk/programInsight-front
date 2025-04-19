import QtQuick
import QtQuick.Window
import FirstPython

Window {
    width: dataSettingsScreen.width
    height: dataSettingsScreen.height

    // Фиксированные размеры
    minimumWidth: width
    maximumWidth: width
    minimumHeight: height
    maximumHeight: height

    visible: true
    title: "DataSettings"

    signal windowClosed()  // Пользовательский сигнал закрытия

    // Отслеживаем изменение свойства visible:
    onVisibleChanged: {
        if (!visible) {
            windowClosed()
        }
    }

    DataSettingsScreen {
        id: dataSettingsScreen
    }

}
