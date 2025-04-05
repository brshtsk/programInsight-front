import QtQuick
import QtQuick.Controls
import FirstPython

Item {
    id: root
    width: 280
    height: roundStatsListView.height

    // property var donutStatsList: [
    //     {
    //         propertyNameText: "В топ-30<br>RAEX",
    //         propertyValueText: "34",
    //         propertyPercentText: "82,1%",
    //         floatPercent: 0.821,
    //         percentColor: "#53b93f",
    //         barBackground: "#ffffff",
    //     },
    //     {
    //         propertyNameText: "Ниже топ-30<br>RAEX",
    //         propertyValueText: "8",
    //         propertyPercentText: "17,9%",
    //         floatPercent: 0.179,
    //         percentColor: "#ed9528",
    //         barBackground: "#ffffff",
    //     },
    //     {
    //         propertyNameText: "Бакалавриат",
    //         propertyValueText: "29",
    //         propertyPercentText: "71%",
    //         floatPercent: 0.71,
    //         percentColor: "#696969",
    //         barBackground: "#ffffff",
    //     },
    //     {
    //         propertyNameText: "Специалитет",
    //         propertyValueText: "29",
    //         propertyPercentText: "29%",
    //         floatPercent: 0.29,
    //         percentColor: "#000000",
    //         barBackground: "#ffffff",
    //     }
    // ]

    property var donutStatsList

    ListView {
        id: roundStatsListView
        anchors.left: parent.left
        anchors.right: parent.right
        height: contentHeight
        anchors.verticalCenter: parent.verticalCenter

        spacing: 5 // Добавляем отступ между элементами

        model: root.donutStatsList

        delegate: Item {
            id: circleStatisticColumnItem
            x: 0
            y: 0
            width: parent.width
            height: 50

            Text {
                id: propertyNameText
                width: 130
                height: 40
                color: "#000000"
                text: modelData.propertyNameText
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 18
                horizontalAlignment: Text.AlignLeft
                verticalAlignment: Text.AlignVCenter
                font.styleName: "SemiBold"
                font.family: Constants.font.family
            }

            Text {
                id: propertyValueText
                x: 135
                width: 60
                height: 40
                color: "#000000"
                text: modelData.propertyValueText
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 24
                horizontalAlignment: Text.AlignRight
                verticalAlignment: Text.AlignVCenter
                font.styleName: "SemiBold"
                font.family: Constants.font.family
            }

            Text {
                id: propertyPercentText
                width: 70
                height: 40
                text: modelData.propertyPercentText
                anchors.verticalCenter: parent.verticalCenter
                anchors.right: parent.right
                font.pixelSize: 24
                horizontalAlignment: Text.AlignLeft
                verticalAlignment: Text.AlignVCenter
                color: modelData.percentColor
                font.family: Constants.font.family
                font.styleName: "SemiBold"
            }

            ProgressBar {
                id: propertyPercentProgressBar
                anchors.right: parent.right
                anchors.bottom: parent.bottom
                width: 70
                height: 5
                value: modelData.floatPercent

                background: Rectangle {
                    color: modelData.barBackground // Цвет фона
                    radius: height / 2 // Закругление краев
                }

                contentItem: Item {
                    Rectangle {
                        width: propertyPercentProgressBar.width
                               * propertyPercentProgressBar.value
                        height: propertyPercentProgressBar.height
                        radius: height / 2 // Закругленные края шкалы прогресса
                        color: modelData.percentColor // Цвет шкалы прогресса
                    }
                }
            }
        }
    }
}
