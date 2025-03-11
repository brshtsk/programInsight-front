// SettingsDialog.ui.qml
import QtQuick
import QtQuick.Controls
import QtQuick.Studio.Application
import FirstPython

Rectangle {
    id: dashboardsContent
    width: 1200
    height: 690
    color: "#ffffff"

    Rectangle {
        id: roundBarRectangle
        x: 20
        y: 320
        width: 640
        height: 350
        color: "#dde9db"
        radius: 10
        border.width: 0

        Image {
            id: statisticsSircleImage
            anchors.right: parent.right
            anchors.bottom: parent.bottom
            anchors.rightMargin: 20
            anchors.bottomMargin: 20
            width: 310
            height: 310
            source: "resources/circle_diagram.png"
            fillMode: Image.PreserveAspectFit

            Text {
                id: statisticSircleText
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
                color: "#373737"
                text: "Статистика ОП"
                font.pixelSize: 18
                textFormat: Text.RichText
                font.family: Constants.font.family
                font.styleName: "Condensed SemiBold"
            }
        }

        Item {
            id: circleStatsItem
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.left: parent.left
            anchors.leftMargin: 20
            anchors.topMargin: 20
            anchors.bottomMargin: 20
            width: 280

            ListView {
                id: roundStatsListView
                anchors.left: parent.left
                anchors.right: parent.right
                height: 245
                anchors.verticalCenter: parent.verticalCenter

                spacing: 15 // Добавляем отступ между элементами

                model: ListModel {
                    ListElement {
                        propertyNameText: "В топ-30<br>RAEX"
                        propertyValueText: "34"
                        propertyPercentText: "82,1%"
                        floatPercent: 0.821
                        percentColor: "#53b93f"
                        barBackground: "#ffffff"
                    }

                    ListElement {
                        propertyNameText: "Ниже топ-30<br>RAEX"
                        propertyValueText: "8"
                        propertyPercentText: "17,9%"
                        floatPercent: 0.179
                        percentColor: "#ed9528"
                        barBackground: "#ffffff"
                    }

                    ListElement {
                        propertyNameText: "Бакалавриат"
                        propertyValueText: "29"
                        propertyPercentText: "71%"
                        floatPercent: 0.71
                        percentColor: "#696969"
                        barBackground: "#ffffff"
                    }

                    ListElement {
                        propertyNameText: "Специалитет"
                        propertyValueText: "29"
                        propertyPercentText: "29%"
                        floatPercent: 0.29
                        percentColor: "#000000"
                        barBackground: "#ffffff"
                    }
                }

                delegate: Item {
                    id: circleStatisticItem
                    x: 0
                    y: 0
                    width: parent.width
                    height: 50

                    Text {
                        id: propertyNameText
                        width: 130
                        height: 40
                        color: "#000000"
                        text: model.propertyNameText
                        anchors.left: parent.left
                        anchors.verticalCenter: parent.verticalCenter
                        font.pixelSize: 16
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
                        text: model.propertyValueText
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
                        text: model.propertyPercentText
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.right: parent.right
                        font.pixelSize: 24
                        horizontalAlignment: Text.AlignLeft
                        verticalAlignment: Text.AlignVCenter
                        color: model.percentColor
                        font.family: Constants.font.family
                        font.styleName: "SemiBold"
                    }

                    ProgressBar {
                        id: propertyPercentProgressBar
                        anchors.right: parent.right
                        anchors.bottom: parent.bottom
                        width: 70
                        height: 5
                        value: model.floatPercent

                        background: Rectangle {
                            color: model.barBackground // Цвет фона
                            radius: height / 2 // Закругление краев
                        }

                        contentItem: Item {
                            Rectangle {
                                width: propertyPercentProgressBar.width
                                       * propertyPercentProgressBar.value
                                height: propertyPercentProgressBar.height
                                radius: height / 2 // Закругленные края шкалы прогресса
                                color: model.percentColor // Цвет шкалы прогресса
                            }
                        }
                    }
                }
            }

            // Item {
            //     id: circleStatisticItem
            //     x: 0
            //     y: 0
            //     width: parent.width
            //     height: 50

            //     Text {
            //         id: propertyNameText
            //         width: 130
            //         height: 40
            //         color: "#000000"
            //         text: "ОП в топ-30<br>RAEX"
            //         anchors.left: parent.left
            //         anchors.verticalCenter: parent.verticalCenter
            //         font.pixelSize: 16
            //         horizontalAlignment: Text.AlignLeft
            //         verticalAlignment: Text.AlignVCenter
            //         font.styleName: "SemiBold"
            //         font.family: Constants.font.family
            //     }

            //     Text {
            //         id: propertyValueText
            //         x: 135
            //         width: 60
            //         height: 40
            //         color: "#000000"
            //         text: "34"
            //         anchors.verticalCenter: parent.verticalCenter
            //         font.pixelSize: 24
            //         horizontalAlignment: Text.AlignRight
            //         verticalAlignment: Text.AlignVCenter
            //         font.styleName: "SemiBold"
            //         font.family: Constants.font.family
            //     }

            //     Text {
            //         id: propertyPercentText
            //         width: 70
            //         height: 40
            //         text: "82,2%"
            //         anchors.verticalCenter: parent.verticalCenter
            //         anchors.right: parent.right
            //         font.pixelSize: 24
            //         horizontalAlignment: Text.AlignLeft
            //         verticalAlignment: Text.AlignVCenter
            //         color: "#53b93f"
            //         font.family: Constants.font.family
            //         font.styleName: "SemiBold"
            //     }

            //     ProgressBar {
            //         id: propertyPercentProgressBar
            //         anchors.right: parent.right
            //         anchors.bottom: parent.bottom
            //         width: 70
            //         height: 5
            //         value: 0.822

            //         background: Rectangle {
            //             color: "#FFFFFF" // Цвет фона
            //             radius: height / 2 // Закругление краев
            //         }

            //         contentItem: Item {
            //             Rectangle {
            //                 width: propertyPercentProgressBar.width
            //                        * propertyPercentProgressBar.value
            //                 height: propertyPercentProgressBar.height
            //                 radius: height / 2 // Закругленные края шкалы прогресса
            //                 color: "#53b93f" // Цвет шкалы прогресса
            //             }
            //         }
            //     }
            // }
        }
    }

    Text {
        id: headerText
        x: 20
        y: 20
        text: "Дашборды"
        font.pixelSize: 36
        font.family: Constants.font.family
        font.styleName: "SemiBold"
        width: 200
        height: 50
        textFormat: Text.RichText
    }

    Rectangle {
        id: mainStatsRectangle
        x: 20
        y: 220
        width: 640
        height: 90
        color: "#53b93f"
        radius: 10

        Item {
            id: upperZoneItem
            x: 0
            height: 70
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 20
            anchors.rightMargin: 20
            anchors.verticalCenter: parent.verticalCenter

            Item {
                id: sentralUpperItem
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
                height: parent.height
                width: 200

                Text {
                    id: typeInfoText
                    x: 355
                    y: 0
                    width: 130
                    height: 20
                    color: "#dde9db"
                    text: qsTr("Выбран тип")
                    anchors.left: parent.left
                    anchors.top: parent.top
                    font.pixelSize: 16
                    horizontalAlignment: Text.AlignLeft
                    font.styleName: "Condensed SemiBold"
                    font.family: Constants.font.family
                }

                Text {
                    id: typeOpText
                    x: 185
                    y: 20
                    width: 170
                    height: 50
                    color: "#ffffff"
                    text: "Бакалавриат<br>и специалитет"
                    anchors.left: parent.left
                    anchors.bottom: parent.bottom
                    font.pixelSize: 21
                    horizontalAlignment: Text.AlignLeft
                    verticalAlignment: Text.AlignTop
                    font.styleName: "SemiBold"
                    font.family: Constants.font.family
                }
            }

            Item {
                id: leftUpperItem
                anchors.left: parent.left
                anchors.top: parent.top
                height: parent.height
                width: 200

                Text {
                    id: opNumText
                    x: 0
                    y: 20
                    width: 130
                    height: 50
                    color: "#ffffff"
                    text: "42"
                    anchors.left: parent.left
                    anchors.bottom: parent.bottom
                    font.pixelSize: 42
                    verticalAlignment: Text.AlignTop
                    font.family: Constants.font.family
                    font.styleName: "SemiBold"
                }

                Text {
                    id: amountInfoText
                    x: 0
                    y: 0
                    width: 130
                    height: 20
                    anchors.left: parent.left
                    anchors.top: parent.top
                    color: "#dde9db"
                    text: qsTr("Всего ОП найдено")
                    font.pixelSize: 16
                    font.family: Constants.font.family
                    font.styleName: "Condensed SemiBold"
                }
            }

            Item {
                id: rightUpperItem
                width: 140
                height: parent.height
                anchors.right: parent.right
                anchors.top: parent.top

                Text {
                    id: settingInfoText
                    x: 70
                    y: 0
                    width: 130
                    height: 20
                    anchors.left: parent.left
                    anchors.top: parent.top
                    color: "#dde9db"
                    text: qsTr("Выбрана оплата")
                    font.pixelSize: 16
                    horizontalAlignment: Text.AlignLeft
                    font.family: Constants.font.family
                    font.styleName: "Condensed SemiBold"
                }

                Text {
                    id: settingsTypeText
                    width: 140
                    height: 50
                    color: "#ffffff"
                    text: "Бюджет"
                    anchors.left: parent.left
                    anchors.bottom: parent.bottom
                    font.pixelSize: 21
                    horizontalAlignment: Text.AlignLeft
                    verticalAlignment: Text.AlignTop
                    font.styleName: "SemiBold"
                    font.family: Constants.font.family
                }
            }
        }
    }

    Rectangle {
        id: scoreDistributionRectangle
        x: 670
        y: 405
        width: 320
        height: 265
        color: "#53b93f"
        radius: 10

        Image {
            id: scoreDistributionImage
            anchors.bottom: parent.bottom
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.bottomMargin: 10
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            source: "resources/scores_distribution.png"
            fillMode: Image.PreserveAspectFit
        }

        Text {
            id: scoreDistributionText
            anchors.left: parent.left
            anchors.top: parent.top
            anchors.leftMargin: 20
            anchors.topMargin: 10
            width: 210
            height: 40
            color: "#ffffff"
            text: "Распределение проходных<br>баллов за предмет"
            font.pixelSize: 21
            horizontalAlignment: Text.AlignLeft
            verticalAlignment: Text.AlignTop
            font.styleName: "SemiBold"
            font.family: Constants.font.family
        }
    }

    Rectangle {
        id: priceDistributionRectangle
        x: 670
        y: 130
        width: 320
        height: 265
        color: "#dde9db"
        radius: 10
        Image {
            id: priceDistributionImage
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.bottom: parent.bottom
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            anchors.bottomMargin: 10
            source: "resources/price_distribution.png"
            fillMode: Image.PreserveAspectFit
        }

        Text {
            id: priceDistributionText
            width: 210
            height: 40
            color: "#000000"
            text: "Распределение<br>годовой стоимости"
            anchors.left: parent.left
            anchors.top: parent.top
            anchors.leftMargin: 20
            anchors.topMargin: 10
            font.pixelSize: 21
            horizontalAlignment: Text.AlignLeft
            verticalAlignment: Text.AlignTop
            font.styleName: "SemiBold"
            font.family: Constants.font.family
        }
    }
}
