import QtQuick 2.15
import FirstPython

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

    Text {
        id: opNameText
        x: 15
        y: 15
        width: parent.width - 30
        height: 55
        color: "#ffffff"
        text: model.opNameText
        font.pixelSize: 20
        textFormat: Text.RichText
        font.family: Constants.font.family
        font.styleName: "SemiBold"
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

    // MouseArea для обработки клика и изменения курсора
    MouseArea {
        anchors.fill: parent
        cursorShape: Qt.PointingHandCursor
        onClicked: {
            // Передаем информацию в питон-обработчик

            pyHandler.handleCardClicked(index, opNameText.text, universityNameText.text)
        }
    }
}
