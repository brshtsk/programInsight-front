import QtQuick
import QtQuick.Window
import FirstPython

Window {
    width: userCabinetScreen.width
    height: userCabinetScreen.height

    // Фиксированные размеры
    minimumWidth: width
    maximumWidth: width
    minimumHeight: height
    maximumHeight: height

    visible: true
    title: "UserCabinet"

    signal windowClosed()  // Пользовательский сигнал закрытия

    // Отслеживаем изменение свойства visible:
    onVisibleChanged: {
        if (!visible) {
            windowClosed()
        }
    }

    UserCabinetScreen {
        id: userCabinetScreen
    }

}
