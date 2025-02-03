import QtQuick
import FirstPython

Window {
    width: settingsScreen.width
    height: settingsScreen.height

    visible: true
    title: "Settings"

    SearchSettingsScreen {
        id: settingsScreen
    }

}