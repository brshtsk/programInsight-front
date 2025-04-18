import QtQuick 2.15
import FirstPython
import QtQuick.Controls

Rectangle {
    id: clusterCard
    width: 270
    height: 65
    color: modelData.clusterCardColor
    radius: 10
    anchors.horizontalCenter: parent.horizontalCenter
    border.color: "#53b93f"
    border.width: 0

    Flickable {
        id: clusterNameContainerFlickable
        x: 15
        y: 10
        width: parent.width - 30
        height: clusterNameText.height // либо можно задать фиксированную высоту, например, 55
        clip: true
        contentWidth: clusterNameText.width

    Text {
        id: clusterNameText
        x: 0
        y: 0
        height: 20
        color: modelData.clusterNameColor
        text: modelData.clusterNameText
        font.pixelSize: 18
        textFormat: Text.RichText
        font.family: Constants.font.family
        font.styleName: "SemiBold"
    }

    ScrollBar.horizontal: ScrollBar {
        policy: ScrollBar.Auto
    }

    }

    Rectangle {
        id: clusterSizeRectangle
        x: 15
        y: 33
        width: clusterSizeText.width + 20
        height: 25
        color: "#ffffff"
        radius: 10
        Text {
            id: clusterSizeText
            color: "#000000"
            text: "Кол-во ОП: " + modelData.clusterSizeText
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: 18
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.styleName: "SemiBold"
            font.family: Constants.font.family
        }
    }

    MouseArea {
        anchors.fill: parent
        cursorShape: Qt.PointingHandCursor

        onClicked: {
            // Если событие не было обработано Flickable'ом, то кликаем по карточке
            clusterHandler.handleCardClicked(
                modelData.clusterNameText
            )
        }
    }
}
