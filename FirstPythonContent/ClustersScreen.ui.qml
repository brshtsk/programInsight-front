import QtQuick
import QtQuick.Controls
import FirstPython

Rectangle {
    id: clustersContent

    width: 950
    height: 640
    color: "#ffffff"

    Text {
        id: headerText
        text: "Кластерный<br>анализ"
        font.pixelSize: 24
        textFormat: Text.RichText
        font.family: Constants.font.family
        font.styleName: "SemiBold"
        anchors.left: parent.left
        anchors.verticalCenter: mainStatsRectangle.verticalCenter
        anchors.leftMargin: 30
    }

    Item {
        id: upperLogoItem
        x: 200
        anchors.verticalCenter: mainStatsRectangle.verticalCenter
        width: 130
        height: 80

        Image {
            id: image
            width: 50
            height: 50
            anchors.right: parent.right
            anchors.verticalCenter: parent.verticalCenter
            source: "resources/near-logo.svg"
            fillMode: Image.PreserveAspectFit
        }
    }

    Rectangle {
        id: mainStatsRectangle
        x: 350
        y: 20
        width: 410
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
            anchors.verticalCenter: parent.verticalCenter

            Item {
                id: sentralUpperItem
                anchors.verticalCenter: parent.verticalCenter
                anchors.right: parent.right
                anchors.rightMargin: 20
                height: parent.height
                width: 170

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
                    id: opTypeText
                    objectName: "opTypeText"
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
                    objectName: "opNumText"
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
        }
    }

    Rectangle {
        id: clusterSettingsRectangle
        x: 20
        y: 120
        width: 320
        height: 60
        color: "#dde9db"
        radius: 10

        Item {
            id: algorithmSettingsItem
            x: 10
            y: 10
            width: 200
            height: 40
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            Text {
                id: algorithmTypeSettingsText
                x: 0
                height: 30
                color: "#373737"
                text: "Алгоритм"
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                font.pixelSize: 21
                verticalAlignment: Text.AlignVCenter
                textFormat: Text.RichText
                font.styleName: "SemiBold"
                font.family: Constants.font.family
            }

            ComboBox {
                id: algorithmTypeComboBox
                width: 180
                height: 30
                anchors.verticalCenter: parent.verticalCenter
                anchors.right: parent.right
                anchors.rightMargin: 5
                objectName: "algorithmTypeComboBox"
                model: ["Автоматически", "K-Means", "Mean Shift", "DBSCAN"]
                indicator: Item {
                    width: 20
                    height: 20
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.right: parent.right
                    Text {
                        color: "#ffffff"
                        text: "\u25be"
                        font.pixelSize: 24
                        anchors.centerIn: parent
                    }
                }
                contentItem: Rectangle {
                    id: algorithmComboBoxBackground
                    color: "#53b93f"
                    radius: 10
                    anchors.fill: parent
                    anchors.leftMargin: -5
                    anchors.rightMargin: -5
                    Text {
                        width: parent.width - 20
                        color: "#ffffff"
                        text: algorithmTypeComboBox.currentText
                        font.pixelSize: 18
                        font.styleName: "SemiBold"
                        font.family: Constants.font.family
                        anchors.centerIn: parent
                    }
                }
            }
        }
    }

    Rectangle {
        id: filterByExamsRectangle
        x: 20
        y: 190
        width: 320
        height: 100
        color: "#dde9db"
        radius: 10
        Item {
            id: upperFilterByExamsItem
            x: 10
            y: 10
            width: 200
            height: 40
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            Text {
                id: filterByExamsText
                height: 30
                color: "#373737"
                text: "Пара переменных"
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                font.pixelSize: 21
                verticalAlignment: Text.AlignVCenter
                textFormat: Text.RichText
                font.styleName: "SemiBold"
                font.family: Constants.font.family
            }
        }

        Item {
            id: lowerFilterByExamsItem
            x: 10
            y: 50
            width: 200
            height: 40
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            ComboBox {
                id: filterByExamsComboBox
                width: 290
                height: 30
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                anchors.leftMargin: 5
                objectName: "filterByExamsComboBox"
                model: ["Стоимость / Проходной бюджет", "Стоимость / Проходной платное"]
                indicator: Item {
                    width: 20
                    height: 20
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.right: parent.right
                    Text {
                        color: "#ffffff"
                        text: "\u25be"
                        font.pixelSize: 24
                        anchors.centerIn: parent
                    }
                }
                contentItem: Rectangle {
                    id: filterByExamsComboBoxBackground
                    color: "#53b93f"
                    radius: 10
                    anchors.fill: parent
                    anchors.leftMargin: -5
                    anchors.rightMargin: -5
                    Text {
                        width: parent.width - 20
                        color: "#ffffff"
                        text: filterByExamsComboBox.currentText
                        font.pixelSize: 18
                        font.styleName: "SemiBold"
                        font.family: Constants.font.family
                        anchors.centerIn: parent
                    }
                }
            }
        }
    }

    Rectangle {
        id: rectangle
        x: 20
        y: 300
        width: 320
        height: 50
        color: "#dde9db"
        radius: 10

        Button {
            id: dashboardButton
            x: 10
            y: 10
            width: 300
            height: 30
            text: "Запустить анализ!"
            font.pixelSize: 18
            objectName: "dashboardButton"
            font.styleName: "SemiBold"
            font.family: Constants.font.family
            contentItem: Text {
                color: "#ffffff"
                text: dashboardButton.text
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                scale: dashboardButton.hovered ? 1.05 : 1.0
                font: dashboardButton.font
                Behavior {
                    NumberAnimation {
                        duration: 100
                    }
                }
            }
            background: Rectangle {
                color: dashboardButton.pressed ? "#7dd96b" : "#53b93f"
                radius: 10
                scale: dashboardButton.hovered ? 1.05 : 1.0
                Behavior {
                    NumberAnimation {
                        duration: 100
                    }
                }

                Behavior {
                    ColorAnimation {
                        duration: 200
                    }
                }
            }
        }
    }

    Image {
        id: clustrersImage
        x: 350
        y: 120
        width: 580
        height: 500
        source: "resources/clusters.png"
        fillMode: Image.PreserveAspectFit
    }

    Rectangle {
        id: rectangle1
        x: 20
        y: 400
        width: 320
        height: 220
        color: "#ffffff"

        radius: 10
        border.color: "#53b93f"
        border.width: 2
    }

    Rectangle {
        id: helpRectangle
        x: 770
        y: 20
        width: 160
        height: 90
        color: "#dde9db"
        radius: 10

        Text {
            id: helpText
            color: "#373737"
            x: 10
            text: "Справка"
            anchors.verticalCenter: parent.verticalCenter
            font.pixelSize: 21
            horizontalAlignment: Text.AlignLeft
            verticalAlignment: Text.AlignTop
            font.styleName: "SemiBold"
            font.family: Constants.font.family
        }

        Rectangle {
            id: filterScoreHelpRectangle
            anchors.right: parent.right
            anchors.rightMargin: 10
            anchors.verticalCenter: parent.verticalCenter
            width: 24
            height: 36
            color: "#53b93f"
            radius: 10

            Text {
                anchors.fill: parent
                text: "?"
                color: "#ffffff"
                font.pixelSize: 21
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                textFormat: Text.RichText
                font.family: Constants.font.family
                font.styleName: "Bold"
            }

            MouseArea {
                id: scoreHelpMouseArea
                anchors.fill: parent
                hoverEnabled: true
            }

            ToolTip {
                text: "Подсказка:<br><br>В данном разделе можно провести кластерый анализ<br>по выборке, заданной вашими настройками поиска."
                visible: scoreHelpMouseArea.containsMouse
            }
        }
    }

    Item {
        id: choiceItem
        x: 20
        y: 360
        width: 320
        height: 30

        Text {
            id: choiceText
            text: "Выбор кластера"
            font.pixelSize: 21
            textFormat: Text.RichText
            font.family: Constants.font.family
            font.styleName: "SemiBold"
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }
}
