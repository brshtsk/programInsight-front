// SettingsDialog.ui.qml
import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material

Rectangle {
    id: settingsContent
    width: 450
    height: 270
    color: "#ffffff"

    Item {
        id: settingsItem
        anchors.fill: parent
        anchors.margins: 20

        Text {
            id: headerText
            text: "Настройки поиска"
            font.pixelSize: 24
            width: parent.width
            height: 30
            textFormat: Text.RichText
            font.family: "Bahnschrift SemiBold"
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.top: parent.top
        }

        Rectangle {
            id: settingsRectangle
            anchors.bottom: parent.bottom
            anchors.horizontalCenter: parent.horizontalCenter
            width: parent.width
            height: 190
            color: "#dde9db"
            radius: 10
            border.width: 0

            Item {
                id: scoreSettingsItem
                y: 10
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.leftMargin: 10
                anchors.rightMargin: 10
                height: 40
                width: 200

                Text {
                    id: scoreTypeSettingsText
                    x: 0
                    anchors.verticalCenter: parent.verticalCenter
                    text: "Отображение баллов"
                    color: "#373737"
                    font.pixelSize: 20
                    verticalAlignment: Text.AlignTop
                    textFormat: Text.RichText
                    font.family: "Bahnschrift Light"
                }

                ComboBox {
                    id: scoreTypeComboBox
                    objectName: "scoreTypeComboBox"
                    anchors.verticalCenter: parent.verticalCenter
                    height: 30
                    anchors.right: parent.right
                    anchors.rightMargin: 10
                    width: 130

                    model: ["На бюджет", "На платное"]

                    // Кастомизация фон и текстового содержимого
                    contentItem: Rectangle {
                        id: comboBoxBackground
                        anchors.fill: parent
                        anchors.leftMargin: -5
                        anchors.rightMargin: -5
                        color: "#53b93f"
                        radius: 10

                        Text {
                            width: parent.width - 20
                            text: scoreTypeComboBox.currentText
                            color: "#ffffff"
                            anchors.centerIn: parent
                            font.pixelSize: 18
                            font.family: "Bahnschrift SemiBold"
                        }
                    }
                    // Кастомизация индикатора (стрелочки)
                    indicator: Item {
                        width: 20
                        height: 20
                        anchors.right: parent.right
                        anchors.verticalCenter: parent.verticalCenter

                        Text {
                            text: "\u25BE" // Символ стрелочки вниз
                            color: "#ffffff"
                            anchors.centerIn: parent
                            font.pixelSize: 24
                        }
                    }
                }
            }
        }
    }
}
