import QtQuick
import QtQuick.Window
import FirstPython

Window {
    width: dataSettingsScreen.width
    height: dataSettingsScreen.height

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
