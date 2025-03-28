import QtQuick 2.15
import FirstPython
import QtQuick.Controls

Rectangle {
    id: opCard
    width: 420
    height: 140
    color: "#53b93f"
    radius: 10
    anchors.horizontalCenter: parent.horizontalCenter

    // Элементы дизайна карточки
    Image {
        id: universityImage
        x: 15
        y: 70
        width: 50
        height: 50

        // По умолчанию значения model.imageSource начинаются на "resources"
        source: "../" + model.imageSource
        fillMode: Image.PreserveAspectFit
    }

    Flickable {
        id: opNameContainerFlickable
        x: 15
        y: 15
        width: parent.width - 30
        height: opNameText.height // либо можно задать фиксированную высоту, например, 55
        clip: true
        contentWidth: opNameText.width

    Text {
        id: opNameText
        x: 0
        y: 0
        height: 55
        color: "#ffffff"
        text: model.opNameText
        font.pixelSize: 20
        textFormat: Text.RichText
        font.family: Constants.font.family
        font.styleName: "SemiBold"
    }

    ScrollBar.horizontal: ScrollBar {
        policy: ScrollBar.Auto
    }

    }

    Text {
        id: universityNameText
        x: 75
        y: 70
        width: 120
        height: 23
        color: "#ffffff"
        text: model.universityNameText
        font.pixelSize: 15
        horizontalAlignment: Text.AlignLeft
        verticalAlignment: Text.AlignBottom
        textFormat: Text.RichText
        font.family: Constants.font.family
        font.styleName: "SemiBold"
    }

    Text {
        id: opCodeText
        x: 75
        y: 97
        width: 120
        height: 23
        color: "#ffffff"
        text: model.opCodeText
        font.pixelSize: 15
        horizontalAlignment: Text.AlignLeft
        verticalAlignment: Text.AlignTop
        textFormat: Text.RichText
        font.family: Constants.font.family
        font.styleName: "SemiBold"
    }

    // Пример информационных блоков (info1, info2)
    Rectangle {
        id: info1Rectangle
        x: 251
        y: 70
        width: 72
        height: 40
        color: "#ffffff"
        radius: 10

        Text {
            id: info1Text
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.family: Constants.font.family
            font.styleName: "SemiBold"
            anchors.fill: parent
            color: "#53b93f"
            text: model.info1Text
        }
    }

    Rectangle {
        id: info2Rectangle
        x: 333
        y: 70
        width: 72
        height: 40
        color: "#ffffff"
        radius: 10

        Text {
            id: info2Text
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.family: Constants.font.family
            font.styleName: "SemiBold"
            anchors.fill: parent
            color: "#53b93f"
            text: model.info2Text
        }
    }

    Text {
        id: typeInfo1Text
        x: 251
        y: 112
        width: 72
        height: 16
        color: "#ffffff"
        text: qsTr("Баллов ЕГЭ")
        font.pixelSize: 12
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        font.family: Constants.font.family
    }

    Text {
        id: typeInfo2Text
        x: 333
        y: 112
        width: 72
        height: 16
        color: "#ffffff"
        text: qsTr("Стоимость")
        font.pixelSize: 12
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        font.family: Constants.font.family
    }

    MouseArea {
        anchors.fill: parent
        cursorShape: Qt.PointingHandCursor
        onPressed: {
            // Если событие произошло в области opNameContainerFlickable, передаём его дальше
            if (mouse.x >= opNameContainerFlickable.x &&
                mouse.x <= opNameContainerFlickable.x + opNameContainerFlickable.width &&
                mouse.y >= opNameContainerFlickable.y &&
                mouse.y <= opNameContainerFlickable.y + opNameContainerFlickable.height &&
                opNameText.width > opNameContainerFlickable.width) {
                mouse.accepted = false
            }
        }
        onClicked: {
            // Если событие не было обработано Flickable'ом, то кликаем по карточке
            pyHandler.handleCardClicked(index, opNameText.text, universityNameText.text)
        }
    }

}
