import QtQuick
import QtQuick.Controls
import FirstPython
import "components"

Rectangle {
    width: 340
    height: 250
    color: "#ffffff"

    Item {
        id: upperLogoItem
        anchors.right: parent.right
        anchors.rightMargin: 20
        anchors.verticalCenter: headerText.verticalCenter
        width: 160
        height: 60

        Text {
            id: projectNameText
            x: 0
            y: 0
            color: "#53b93f"
            text: "ProgramInsight"
            anchors.right: parent.right
            anchors.verticalCenter: parent.verticalCenter
            font.pixelSize: 16
            textFormat: Text.RichText
            font.family: Constants.font.family
            font.styleName: "SemiBold"
        }

        Image {
            id: image
            width: 35
            height: 35
            anchors.left: parent.left
            anchors.verticalCenter: parent.verticalCenter
            source: "resources/near-logo.svg"
            fillMode: Image.PreserveAspectFit
        }
    }

    Text {
        id: headerText
        y: 15
        text: "Экспорт<br>данных"
        font.pixelSize: 24
        textFormat: Text.RichText
        font.family: Constants.font.family
        font.styleName: "SemiBold"
        anchors.left: parent.left
        anchors.leftMargin: 30
    }

    Rectangle {
        id: rectangle
        x: 20
        y: 80
        width: 300
        height: 110
        color: "#dde9db"
        radius: 10

        Text {
            id: infoText
            objectName: "infoText"
            x: 10
            y: 8
            width: 280
            height: 40
            text: "Экспортируйте ОП<br>по вашим настройкам поиска"
            color: "#373737"
            font.pixelSize: 18
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            textFormat: Text.RichText
            font.family: Constants.font.family
            font.styleName: "SemiBold"
        }

        Flickable {
            id: pathTextFlickable
            objectName: "pathTextFlickable"
            x: 10
            y: 30
            width: parent.width - 20
            height: 20
            clip: true

            // если текст уже помещается — ширина контейнера, иначе — реальная ширина текста
            contentWidth: pathText.implicitWidth > width ? pathText.implicitWidth : width
            contentHeight: height
            flickableDirection: Flickable.HorizontalFlick
            visible: false

            Text {
                id: pathText
                objectName: "pathText"
                height: 20
                text: "C/////"
                color: "#373737"
                font.pixelSize: 18
                font.family: Constants.font.family
                font.styleName: "SemiBold"
                textFormat: Text.RichText
                verticalAlignment: Text.AlignTop
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
            }

            // появится лишь если текст не влазит
            ScrollBar.horizontal: ScrollBar {
                policy: ScrollBar.Auto // можно заменить на Always, чтобы всегда была полоса
            }
        }

        Item {
            id: formatSettingsItem
            x: 10
            y: 60
            width: 200
            height: 40
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 10
            anchors.rightMargin: 10

            Text {
                id: formatSettingsText
                x: 0
                height: 30
                anchors.verticalCenter: parent.verticalCenter
                text: "Формат"
                color: "#373737"
                font.pixelSize: 21
                verticalAlignment: Text.AlignVCenter
                textFormat: Text.RichText
                font.family: Constants.font.family
                font.styleName: "SemiBold"
                anchors.left: parent.left
            }

            ComboBox {
                id: formatTypeComboBox
                objectName: "formatTypeComboBox"
                anchors.verticalCenter: parent.verticalCenter
                height: 30
                anchors.right: parent.right
                anchors.rightMargin: 5
                width: 120

                model: ["XLSX", "CSV", "JSON"]

                // Кастомизация фон и текстового содержимого
                contentItem: Rectangle {
                    id: formatComboBoxBackground
                    anchors.fill: parent
                    anchors.leftMargin: -5
                    anchors.rightMargin: -5
                    color: "#53b93f"
                    radius: 10

                    Text {
                        width: parent.width - 20
                        color: "#ffffff"
                        text: formatTypeComboBox.currentText
                        anchors.centerIn: parent
                        font.pixelSize: 18
                        font.family: Constants.font.family
                        font.styleName: "SemiBold"
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

    Button {
        id: exportButton
        x: 20
        y: 200
        width: 300
        height: 30
        font.pixelSize: 18
        objectName: "exportButton"
        font.styleName: "SemiBold"
        font.family: Constants.font.family
        contentItem: Text {
            color: "#ffffff"
            text: "Экспортировать"
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            scale: exportButton.hovered ? 1.05 : 1.0
            font: exportButton.font
            Behavior {
                NumberAnimation {
                    duration: 100
                }
            }
        }
        background: Rectangle {
            color: exportButton.pressed ? "#7dd96b" : "#53b93f"
            radius: 10
            scale: exportButton.hovered ? 1.05 : 1.0
            Behavior {
                NumberAnimation {
                    duration: 100
                }
            }

            Behavior {
                ColorAnimation {
                    duration: 200
                }
            }
        }
    }
}
