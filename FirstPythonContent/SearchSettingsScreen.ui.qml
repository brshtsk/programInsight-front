// SettingsDialog.ui.qml
import QtQuick
import QtQuick.Controls

Rectangle {
    id: settingsContent
    width: 400
    height: 300
    color: "#ffffff"
    radius: 10
    border.color: "#cccccc"

    Column {
        anchors.fill: parent
        anchors.margins: 20
        spacing: 10

        Text {
            text: "Настройки"
            font.pixelSize: 20
        }
        TextField {
            placeholderText: "Введите значение..."
        }
        // Добавь другие элементы настроек по необходимости
    }
}
