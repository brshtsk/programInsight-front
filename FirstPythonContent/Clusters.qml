import QtQuick
import QtQuick.Window
import FirstPython

Window {
    width: clustersScreen.width
    height: clustersScreen.height

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
