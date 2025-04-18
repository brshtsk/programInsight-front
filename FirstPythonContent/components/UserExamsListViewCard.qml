import QtQuick 2.15
import FirstPython
import QtQuick.Controls

Rectangle {
    id: examCard
    width: 270
    height: 65
    color: "#ffffff"
    radius: 10
    anchors.horizontalCenter: parent.horizontalCenter
    border.color: "#53b93f"
    border.width: 2

    Flickable {
        id: examNameContainerFlickable
        x: 15
        y: 10
        width: parent.width - 50
        height: examNameText.height // либо можно задать фиксированную высоту, например, 55
        clip: true
        contentWidth: examNameText.width

    Text {
        id: examNameText
        x: 0
        y: 0
        height: 20
        color: "#373737"
        text: modelData.examNameText
        font.pixelSize: 18
        textFormat: Text.RichText
        font.family: Constants.font.family
        font.styleName: "SemiBold"
    }

    ScrollBar.horizontal: ScrollBar {
        policy: ScrollBar.Auto
    }

    }

    // Пример информационных блоков (info1, info2)
    Rectangle {
        id: scoreRectangle
        y: 33
        anchors.left: examTypeRectangle.right
        anchors.leftMargin: 5
        width: scoreText.width + 20
        height: 25
        color: "#dde9db"
        radius: 10

        Text {
            id: scoreText
            font.pixelSize: 18
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.family: Constants.font.family
            font.styleName: "SemiBold"
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            color: "#373737"
            text: "Балл: " + modelData.scoreText
        }
    }

    Rectangle {
        id: examTypeRectangle
        x: 15
        y: 33
        width: examTypeText.width + 20
        height: 25
        color: "#dde9db"
        radius: 10
        Text {
            id: examTypeText
            color: "#373737"
            text: modelData.examTypeText
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: 18
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.styleName: "SemiBold"
            font.family: Constants.font.family
        }
    }

    Item {
        id: deleteItem
        anchors.verticalCenter: examNameContainerFlickable.verticalCenter
        anchors.right: parent.right
        anchors.rightMargin: 15
        width: 20
        height: 20
        Button {
            id: deleteButton
            width: 20
            height: 20
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter

            // Прозрачный фон
            background: Rectangle {
                color: "transparent"
            }

            // Элемент, отображающий символ "×"
            contentItem: Text {
                anchors.fill: parent
                text: "×"
                color: deleteButton.pressed ? "#ffc885" : "#ed9528"
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                font.pointSize: 22
                font.family: Constants.font.family
                font.styleName: "Regular"

                scale: deleteButton.hovered ? 1.1 : 1.0
                Behavior on scale {
                    NumberAnimation { duration: 100 }
                }
                Behavior on color {
                    ColorAnimation {
                        duration: 200
                    }
                }
            }

            // Сигнал для удаления объекта
            onClicked: {
                examHandler.handleExamDeleted(modelData.examNameText, modelData.examTypeText, modelData.parent)
                // parent - "settings"/"cabinet"
            }
        }

    }
}
