import QtQuick
import QtQuick.Window
import FirstPython

Window {
    width: dashboardsScreen.width
    height: dashboardsScreen.height

    // Фиксированные размеры
    minimumWidth: width
    maximumWidth: width
    minimumHeight: height
    maximumHeight: height

    visible: true
    title: "Dashboards"

    signal windowClosed()  // Пользовательский сигнал закрытия

    // Отслеживаем изменение свойства visible:
    onVisibleChanged: {
        if (!visible) {
            windowClosed()
        }
    }

    DashboardsScreen {
        id: dashboardsScreen
    }

}
