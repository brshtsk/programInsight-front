import QtQuick
import QtQuick.Controls
import FirstPython

Rectangle {
    id: root
    width: 250
    height: 85
    color: "#53b93f"

    Text {
        id: headerText
        y: 10
        x: 15
        color: "#ffffff"
        text: "Недопустимые параметры<br>у экзамена!"
        font.pixelSize: 16
        textFormat: Text.RichText
        font.family: Constants.font.family
        font.styleName: "SemiBold"
        anchors.verticalCenter: upperLogoItem.verticalCenter
    }

    Button {
        id: saveProfileExamsButton
        objectName: "saveProfileExamsButton"
        x: 10
        y: 55
        width: 50
        height: 20

        font.pixelSize: 16
        font.family: Constants.font.family
        font.styleName: "SemiBold"

        contentItem: Text {
            scale: saveProfileExamsButton.hovered ? 1.05 : 1.0
            font: saveProfileExamsButton.font
            color: "#53b93f"
            text: "Ок" // Белый цвет текста
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            Behavior on scale {
                NumberAnimation {
                    duration: 100
                }
            }
        }

        background: Rectangle {
            color: saveProfileExamsButton.pressed ? "#ededed" : "#ffffff"
            radius: 10
            scale: saveProfileExamsButton.hovered ? 1.05 : 1.0
            Behavior on scale {
                NumberAnimation {
                    duration: 100
                }
            }
            Behavior on color {
                ColorAnimation {
                    duration: 200
                }
            }
        }
    }
}
