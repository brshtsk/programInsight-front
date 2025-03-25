// SettingsDialog.ui.qml
import QtQuick
import QtQuick.Controls
import QtQuick.Studio.Application
import FirstPython

Rectangle {
    id: dashboardsContent
    width: 1010
    height: 680
    color: "#ffffff"

    Rectangle {
        id: roundBarRectangle
        x: 20
        y: 120

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
            id: circleStatsZoneItem
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
                        text: model.propertyNameText
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

    Rectangle {
        id: mainStatsRectangle
        x: 20
        y: 20
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
        y: 395
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
        y: 120
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

    Item {
        id: upperLogoItem
        x: 740
        y: 25
        width: 180
        height: 80
        Text {
            id: projectNameText
            x: 0
            y: 0
            color: "#53b93f"
            text: "ProgramInsight"
            anchors.verticalCenter: parent.verticalCenter
            anchors.right: parent.right
            font.pixelSize: 18
            textFormat: Text.RichText
            font.styleName: "SemiBold"
            font.family: Constants.font.family
        }

        Image {
            id: image
            width: 40
            height: 40
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            source: "resources/near-logo.svg"
            fillMode: Image.PreserveAspectFit
        }
    }

    Rectangle {
        id: universityDiagramRectangle
        x: 290
        y: 480
        width: 370
        height: 180
        color: "#53b93f"
        radius: 10

        Text {
            id: universityDistributionText
            anchors.left: parent.left
            anchors.top: parent.top
            anchors.leftMargin: 20
            anchors.topMargin: 10
            width: 270
            height: 30
            color: "#ffffff"
            text: "Самые частые ВУЗы"
            font.pixelSize: 21
            horizontalAlignment: Text.AlignLeft
            verticalAlignment: Text.AlignTop
            font.styleName: "SemiBold"
            font.family: Constants.font.family
        }

        Item {
            id: universityStatsZoneItem
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.bottom: parent.bottom
            anchors.leftMargin: 20
            anchors.rightMargin: 20
            anchors.bottomMargin: 10
            height: 130

            // Item {
            //     id: universityColumnItem
            //     y: 0
            //     anchors.left: parent.left
            //     anchors.right: parent.right
            //     height: 35

            //     Text {
            //         id: universityNameText
            //         width: 130
            //         height: 20
            //         color: "#ffffff"
            //         text: "НИУ ВШЭ"
            //         anchors.left: parent.left
            //         anchors.verticalCenter: parent.verticalCenter
            //         font.pixelSize: 16
            //         horizontalAlignment: Text.AlignRight
            //         verticalAlignment: Text.AlignVCenter
            //         font.styleName: "SemiBold"
            //         font.family: Constants.font.family
            //     }

            //     Item {
            //         id: barZoneItem
            //         anchors.right: parent.right
            //         anchors.top: parent.top
            //         width: 190
            //         height: parent.height

            //         Rectangle {
            //             id: frequencyBarRectangle
            //             anchors.left: parent.left
            //             anchors.verticalCenter: parent.verticalCenter
            //             width: 150
            //             height: 10
            //             color: "#ffffff"
            //             radius: 5
            //         }

            //         Text {
            //             id: frequencyAmountText
            //             width: 30
            //             height: 20
            //             color: "#ffffff"
            //             text: "14"
            //             anchors.left: frequencyBarRectangle.right
            //             anchors.leftMargin: 5
            //             anchors.verticalCenter: parent.verticalCenter
            //             font.pixelSize: 16
            //             horizontalAlignment: Text.AlignLeft
            //             verticalAlignment: Text.AlignVCenter
            //             font.styleName: "SemiBold"
            //             font.family: Constants.font.family
            //         }
            //     }
            // }
            ListView {
                id: diagramStatsListView
                anchors.left: parent.left
                anchors.right: parent.right
                height: parent.height
                anchors.verticalCenter: parent.verticalCenter

                spacing: 10 // Добавляем отступ между элементами

                model: ListModel {
                    ListElement {
                        universityNameText: "НИУ ВШЭ"
                        thisOpAmountStr: "12"
                        thisOpAmountInt: 12
                        maxOpAmountInt: 12
                    }

                    ListElement {
                        universityNameText: "НИЯУ МИФИ"
                        thisOpAmountStr: "10"
                        thisOpAmountInt: 10
                        maxOpAmountInt: 12
                    }

                    ListElement {
                        universityNameText: "МГУ"
                        thisOpAmountStr: "6"
                        thisOpAmountInt: 6
                        maxOpAmountInt: 12
                    }
                }

                delegate: Item {
                    id: universityColumnItem
                    y: 0
                    anchors.left: parent.left
                    anchors.right: parent.right
                    height: 35

                    Text {
                        id: universityNameText
                        width: 130
                        height: 20
                        color: "#ffffff"
                        text: model.universityNameText
                        anchors.left: parent.left
                        anchors.verticalCenter: parent.verticalCenter
                        font.pixelSize: 16
                        horizontalAlignment: Text.AlignRight
                        verticalAlignment: Text.AlignVCenter
                        font.styleName: "SemiBold"
                        font.family: Constants.font.family
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
                            width: 150 * thisOpAmountInt / maxOpAmountInt
                            height: 10
                            color: "#ffffff"
                            radius: 5
                        }

                        Text {
                            id: frequencyAmountText
                            width: 30
                            height: 20
                            color: "#ffffff"
                            text: model.thisOpAmountStr
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
    }

    Rectangle {
        id: percentageInfoRectangle
        x: 20
        y: 480
        width: 260
        height: 180
        color: "#dde9db"
        radius: 10

        Text {
            id: percentageInfoText
            anchors.left: parent.left
            anchors.top: parent.top
            anchors.leftMargin: 20
            anchors.topMargin: 10
            width: 220
            height: 50
            color: "#000000"
            text: "По вашим настройкам<br>подходит"
            font.pixelSize: 21
            horizontalAlignment: Text.AlignLeft
            verticalAlignment: Text.AlignTop
            font.styleName: "SemiBold"
            font.family: Constants.font.family
        }

        Text {
            id: percentageValueText
            anchors.left: parent.left
            anchors.top: percentageInfoText.bottom
            anchors.leftMargin: 20
            width: 220
            height: 75
            color: "#000000"
            text: "4,2%"
            font.pixelSize: 42
            horizontalAlignment: Text.AlignLeft
            verticalAlignment: Text.AlignVCenter
            font.styleName: "SemiBold"
            font.family: Constants.font.family
        }

        Text {
            id: percentageInfoLowerText
            anchors.left: parent.left
            anchors.top: percentageValueText.bottom
            anchors.leftMargin: 20
            anchors.bottomMargin: 10
            width: 220
            height: 30
            color: "#000000"
            text: "из общего числа ОП"
            font.pixelSize: 21
            horizontalAlignment: Text.AlignLeft
            verticalAlignment: Text.AlignTop
            font.styleName: "SemiBold"
            font.family: Constants.font.family
        }
    }
}
