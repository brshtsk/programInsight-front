import QtQuick
import QtQuick.Window
import FirstPython

Window {
    width: settingsScreen.width
    height: settingsScreen.height

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
