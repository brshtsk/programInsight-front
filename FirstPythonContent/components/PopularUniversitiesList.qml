import QtQuick
import QtQuick.Controls
import FirstPython

Item {
    id: root
    width: 330
    height: 125

    // property var universityValues: [
    //     {
    //         universityNameText: "НИУ ВШЭ",
    //         thisOpAmountStr: "12",
    //         thisOpAmountInt: 12,
    //         maxOpAmountInt: 12,
    //     },

    //     {
    //         universityNameText: "НИЯУ МИФИ",
    //         thisOpAmountStr: "10",
    //         thisOpAmountInt: 10,
    //         maxOpAmountInt: 12,
    //     },

    //     {
    //         universityNameText: "МГУ",
    //         thisOpAmountStr: "6",
    //         thisOpAmountInt: 6,
    //         maxOpAmountInt: 12,
    //     }
    // ]

    property var universityValues

    ListView {
        id: diagramStatsListView

        height: contentHeight
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top

        spacing: 10 // Добавляем отступ между элементами

        model: universityValues

        delegate: Item {
            id: universityColumnItem
            y: 0
            anchors.left: parent.left
            anchors.right: parent.right
            height: 35

            Flickable {
                id: universityNameContainerFlickable
                width: 130
                height: universityNameText.height
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                clip: true
                contentWidth: universityNameText.width < width ? width : universityNameText.width

                Text {
                    id: universityNameText
                    height: 20
                    color: "#ffffff"
                    text: modelData.universityNameText
                    anchors.right: parent.right
                    anchors.verticalCenter: parent.verticalCenter
                    font.pixelSize: 16
                    horizontalAlignment: Text.AlignRight
                    verticalAlignment: Text.AlignVCenter
                    font.styleName: "SemiBold"
                    font.family: Constants.font.family
                }

                ScrollBar.horizontal: ScrollBar {
                    policy: ScrollBar.Auto // или ScrollBar.Always для постоянного отображения
                }
            }

            Item {
                id: barZoneItem
                anchors.right: parent.right
                anchors.top: parent.top
                width: 190
                height: parent.height

                Rectangle {
                    id: frequencyBarRectangle
                    anchors.left: parent.left
                    anchors.verticalCenter: parent.verticalCenter
                    width: 150 * modelData.thisOpAmountInt / modelData.maxOpAmountInt
                    height: 10
                    color: "#ffffff"
                    radius: 5
                }

                Text {
                    id: frequencyAmountText
                    width: 30
                    height: 20
                    color: "#ffffff"
                    text: modelData.thisOpAmountStr
                    anchors.left: frequencyBarRectangle.right
                    anchors.leftMargin: 5
                    anchors.verticalCenter: parent.verticalCenter
                    font.pixelSize: 16
                    horizontalAlignment: Text.AlignLeft
                    verticalAlignment: Text.AlignVCenter
                    font.styleName: "SemiBold"
                    font.family: Constants.font.family
                }
            }
        }
    }
}
