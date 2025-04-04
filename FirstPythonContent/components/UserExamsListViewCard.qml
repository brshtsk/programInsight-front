import QtQuick 2.15
import FirstPython
import QtQuick.Controls

Rectangle {
    id: examCard
    width: 270
    height: 65
    color: "#53b93f"
    radius: 10
    anchors.horizontalCenter: parent.horizontalCenter

    Flickable {
        id: examNameContainerFlickable
        x: 15
        y: 10
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
        anchors.right: parent.right
        anchors.rightMargin: 15
        width: 54
        height: 25
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
            text: modelData.scoreText
        }
    }

    Text {
        id: scoreInfoText
        anchors.top: scoreRectangle.bottom
        anchors.right: scoreRectangle.left
        anchors.rightMargin: 5
        anchors.verticalCenter: scoreRectangle.verticalCenter
        height: 14
        color: "#ffffff"
        text: "Балл:"
        font.pixelSize: 18
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        font.family: Constants.font.family
        font.styleName: "SemiBold"

    }

    Rectangle {
        id: examTypeRectangle
        x: 55
        y: 33
        width: 54
        height: 25
        color: "#ffffff"
        radius: 10
        Text {
            id: examTypeText
            color: "#53b93f"
            text: modelData.examTypeText
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
        anchors.right: examTypeRectangle.left
        anchors.rightMargin: 5
        anchors.verticalCenter: examTypeRectangle.verticalCenter
        height: 20
        color: "#ffffff"
        text: "Тип:"
        font.pixelSize: 18
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        font.family: Constants.font.family
        font.styleName: "SemiBold"
    }

}
