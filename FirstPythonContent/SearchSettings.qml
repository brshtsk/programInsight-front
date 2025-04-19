import QtQuick
import QtQuick.Window
import FirstPython

Window {
    width: settingsScreen.width
    height: settingsScreen.height

    // Фиксированные размеры
    minimumWidth: width
    maximumWidth: width
    minimumHeight: height
    maximumHeight: height

    visible: true
    title: "Settings"

    signal windowClosed()  // Пользовательский сигнал закрытия

    // Отслеживаем изменение свойства visible:
    onVisibleChanged: {
        if (!visible) {
            windowClosed()
        }
    }

    SearchSettingsScreen {
        id: settingsScreen
    }

}
