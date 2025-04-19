import QtQuick
import QtQuick.Window
import FirstPython

Window {
    width: clustersScreen.width
    height: clustersScreen.height

    // Фиксированные размеры
    minimumWidth: width
    maximumWidth: width
    minimumHeight: height
    maximumHeight: height

    visible: true
    title: "Clusters"

    signal windowClosed()  // Пользовательский сигнал закрытия

    // Отслеживаем изменение свойства visible:
    onVisibleChanged: {
        if (!visible) {
            windowClosed()
        }
    }

    ClustersScreen {
        id: clustersScreen
    }

}
