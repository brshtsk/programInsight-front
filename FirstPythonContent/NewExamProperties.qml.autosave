import QtQuick
import QtQuick.Window
import FirstPython

Window {
    width: examPropertiesScreen.width
    height: examPropertiesScreen.height

    visible: true
    title: "NewExam"

    signal windowClosed()  // Пользовательский сигнал закрытия

    // Отслеживаем изменение свойства visible:
    onVisibleChanged: {
        if (!visible) {
            windowClosed()
        }
    }

    NewExamPropertiesScreen {
        id: examPropertiesScreen
    }

}
