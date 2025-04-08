import QtQuick
import QtQuick.Controls
import FirstPython
import "components"

Rectangle {
    width: 340
    height: 200
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
        height: 58
        text: "Настройки"
        font.pixelSize: 24
        verticalAlignment: Text.AlignVCenter
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
        height: 60
        color: "#dde9db"
        radius: 10

        Text {
            id: qualificationTypeSettingsText
            x: 10
            y: 10
            width: 280
            height: 40
            text: "Обновите данные до<br>последней версии"
            color: "#373737"
            font.pixelSize: 18
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            textFormat: Text.RichText
            font.family: Constants.font.family
            font.styleName: "SemiBold"
        }
    }

    Button {
        id: dashboardButton
        x: 20
        y: 150
        width: 300
        height: 30
        text: "Запустить анализ!"
        font.pixelSize: 18
        objectName: "dashboardButton"
        font.styleName: "SemiBold"
        font.family: Constants.font.family
        contentItem: Text {
            color: "#ffffff"
            text: "Обновить"
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            scale: dashboardButton.hovered ? 1.05 : 1.0
            font: dashboardButton.font
            Behavior {
                NumberAnimation {
                    duration: 100
                }
            }
        }
        background: Rectangle {
            color: dashboardButton.pressed ? "#7dd96b" : "#53b93f"
            radius: 10
            scale: dashboardButton.hovered ? 1.05 : 1.0
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
