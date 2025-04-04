import QtQuick 2.15
import FirstPython
import QtQuick.Controls

Rectangle {
    id: examCard
    width: 270
    height: 100
    color: "#53b93f"
    radius: 10
    anchors.horizontalCenter: parent.horizontalCenter

    Flickable {
        id: examNameContainerFlickable
        x: 15
        y: 15
        width: parent.width - 30
        height: examNameText.height // либо можно задать фиксированную высоту, например, 55
        clip: true
        contentWidth: examNameText.width

    Text {
        id: examNameText
        x: 0
        y: 0
        height: 20
        color: "#ffffff"
        text: examNameText
        // text: "Привет"
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
        x: 74
        y: 45
        width: 54
        height: 30
        color: "#ffffff"
        radius: 10

        Text {
            id: scoreText
            font.pixelSize: 18
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.family: Constants.font.family
            font.styleName: "SemiBold"
            anchors.fill: parent
            color: "#53b93f"
            text: scoreText
        }
    }

    Text {
        id: scoreInfoText
        anchors.top: scoreRectangle.bottom
        anchors.topMargin: 2
        anchors.horizontalCenter: scoreRectangle.horizontalCenter

        width: 54
        height: 14
        color: "#ffffff"
        text: "Балл"
        font.pixelSize: 10
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        font.family: Constants.font.family
    }

    Rectangle {
        id: examTypeRectangle
        x: 15
        y: 45
        width: 54
        height: 30
        color: "#ffffff"
        radius: 10
        Text {
            id: examTypeText
            color: "#53b93f"
            text: examTypeText
            anchors.fill: parent
            font.pixelSize: 18
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.styleName: "SemiBold"
            font.family: Constants.font.family
        }
    }

    Text {
        id: examTypeInfoText
        width: 54
        height: 14
        color: "#ffffff"
        text: "Тип"
        anchors.top: examTypeRectangle.bottom
        anchors.topMargin: 2
        font.pixelSize: 10
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        font.family: Constants.font.family
        anchors.horizontalCenter: examTypeRectangle.horizontalCenter
    }

}
