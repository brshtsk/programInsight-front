// SettingsDialog.ui.qml
import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material

Rectangle {
    id: settingsContent
    width: 420
    height: 330
    color: "#ffffff"

    Item {
        id: keySettingsItem
        // anchors.fill: parent
        // anchors.margins: 20
        anchors.left: parent.left
        anchors.leftMargin: 20
        anchors.top: parent.top
        anchors.topMargin: 20
        height: 160
        width: 380

        Text {
            id: headerText
            text: "Настройки поиска"
            font.pixelSize: 24
            width: parent.width
            height: 30
            textFormat: Text.RichText
            font.family: "Bahnschrift SemiBold"
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.top: parent.top
        }

        Rectangle {
            id: keySettingsRectangle
            anchors.bottom: parent.bottom
            anchors.horizontalCenter: parent.horizontalCenter
            width: parent.width
            height: 110
            color: "#dde9db"
            radius: 10
            border.width: 0

            Item {
                id: scoreSettingsItem
                y: 10
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.leftMargin: 10
                anchors.rightMargin: 10
                height: 40
                width: 200

                Text {
                    id: scoreTypeSettingsText
                    x: 0
                    height: 30
                    anchors.verticalCenter: parent.verticalCenter
                    text: "Отображение баллов"
                    color: "#373737"
                    font.pixelSize: 20
                    verticalAlignment: Text.AlignBottom
                    textFormat: Text.RichText
                    font.family: "Bahnschrift Light"
                    anchors.left: parent.left
                }

                ComboBox {
                    id: scoreTypeComboBox
                    objectName: "scoreTypeComboBox"
                    anchors.verticalCenter: parent.verticalCenter
                    height: 30
                    anchors.right: parent.right
                    anchors.rightMargin: 5
                    width: 130

                    model: ["На бюджет", "На платное"]

                    // Кастомизация фон и текстового содержимого
                    contentItem: Rectangle {
                        id: comboBoxBackground
                        anchors.fill: parent
                        anchors.leftMargin: -5
                        anchors.rightMargin: -5
                        color: "#53b93f"
                        radius: 10

                        Text {
                            width: parent.width - 20
                            text: scoreTypeComboBox.currentText
                            color: "#ffffff"
                            anchors.centerIn: parent
                            font.pixelSize: 18
                            font.family: "Bahnschrift SemiBold"
                        }
                    }
                    // Кастомизация индикатора (стрелочки)
                    indicator: Item {
                        width: 20
                        height: 20
                        anchors.right: parent.right
                        anchors.verticalCenter: parent.verticalCenter

                        Text {
                            text: "\u25BE" // Символ стрелочки вниз
                            color: "#ffffff"
                            anchors.centerIn: parent
                            font.pixelSize: 24
                        }
                    }
                }
            }

            Item {
                id: onlyWithBudgetSettingsItem
                y: 60
                width: 200
                height: 40
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.leftMargin: 10
                anchors.rightMargin: 10
                Text {
                    id: onlyWithBudgetSettingsText
                    x: 0
                    width: 320
                    height: 30
                    color: "#373737"
                    text: "Только ОП с бюджетными местами"
                    anchors.verticalCenter: parent.verticalCenter
                    font.pixelSize: 20
                    verticalAlignment: Text.AlignBottom
                    textFormat: Text.RichText
                    font.family: "Bahnschrift Light"
                    anchors.right: parent.right
                }

                CheckBox {
                    id: onlyWithBudgetCheckBox
                    objectName: "onlyWithBudgetCheckBox"
                    width: 30
                    height: 30
                    text: ""
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.left: parent.left

                    indicator: Rectangle {
                        id: checkBoxIndicator
                        anchors.fill: parent
                        color: "white" // Белый фон
                        border.color: "#53b93f" // Зелёная рамка
                        border.width: 2
                        radius: 5

                        // Иконка галочки, отображается только если CheckBox установлен
                        Image {
                            id: checkMark
                            anchors.centerIn: parent
                            source: "resources/tick.svg" // Укажите путь к вашему файлу
                            width: 20
                            height: 20
                            visible: onlyWithBudgetCheckBox.checked
                        }
                    }
                }
            }
        }
    }

    Item {
        id: paidSettingsItem
        width: 380
        height: 110
        anchors.left: parent.left
        y: 200
        anchors.leftMargin: 20

        Rectangle {
            id: paidSettingsRectangle
            anchors.fill: parent
            color: "#dde9db"
            radius: 10
            border.width: 0

            Item {
                id: applyFilterByPriceItem
                y: 10
                width: 200
                height: 40
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.leftMargin: 10
                anchors.rightMargin: 10
                Text {
                    id: applyFilterByPriceText
                    x: 0
                    width: 320
                    height: 30
                    color: "#373737"
                    text: "Фильтровать ОП по цене"
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.right: parent.right
                    font.pixelSize: 20
                    verticalAlignment: Text.AlignBottom
                    textFormat: Text.RichText
                    font.family: "Bahnschrift Light"
                }

                CheckBox {
                    id: applyFilterByPriceCheckBox
                    objectName: "applyFilterByPriceCheckBox"
                    width: 30
                    height: 30
                    text: ""
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.left: parent.left
                    indicator: Rectangle {
                        id: checkBoxIndicator1
                        color: "#ffffff"
                        radius: 5
                        border.color: "#53b93f"
                        border.width: 2
                        anchors.fill: parent
                        Image {
                            id: checkMark1
                            width: 20
                            height: 20
                            visible: applyFilterByPriceCheckBox.checked
                            source: "resources/tick.svg"
                            anchors.centerIn: parent
                        }
                    }
                }
            }

            Item {
                id: priceIntervalItem
                y: 60
                width: 200
                height: 40
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.leftMargin: 10
                anchors.rightMargin: 10
                Text {
                    id: fromText
                    width: 130
                    height: 30
                    color: "#373737"
                    text: "Стоимость от"
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.left: parent.left
                    font.pixelSize: 20
                    verticalAlignment: Text.AlignBottom
                    textFormat: Text.RichText
                    font.family: "Bahnschrift Light"
                }

                TextField {
                    id: minPriceTextField
                    x: 130
                    objectName: "minPriceTextField"
                    width: 65
                    height: 35 // Увеличьте высоту
                    placeholderText: "min"
                    font.pixelSize: 16
                    selectionColor: "#53b93f"
                    anchors.verticalCenter: parent.verticalCenter

                    topPadding: 5 // Поднимает текст, чтобы не обрезался
                    verticalAlignment: Text.AlignVCenter

                    background: Rectangle {
                        anchors.fill: parent
                        color: "#ffffff"
                        radius: 5
                        border.color: "#53b93f"
                        border.width: 2
                    }
                }

                Text {
                    id: toText
                    x: 200
                    y: 5
                    width: 20
                    height: 30
                    color: "#373737"
                    text: "до"
                    anchors.verticalCenter: parent.verticalCenter
                    font.pixelSize: 20
                    verticalAlignment: Text.AlignBottom
                    textFormat: Text.RichText
                    font.family: "Bahnschrift Light"
                }

                TextField {
                    id: maxPriceTextField
                    x: 230
                    objectName: "maxPriceTextField"
                    width: 65
                    height: 35 // Увеличьте высоту
                    placeholderText: "min"
                    font.pixelSize: 16
                    selectionColor: "#53b93f"
                    anchors.verticalCenter: parent.verticalCenter

                    topPadding: 5 // Поднимает текст, чтобы не обрезался
                    verticalAlignment: Text.AlignVCenter

                    background: Rectangle {
                        anchors.fill: parent
                        color: "#ffffff"
                        radius: 5
                        border.color: "#53b93f"
                        border.width: 2
                    }
                }

                Text {
                    id: trText
                    x: 300
                    y: 5
                    width: 60
                    height: 30
                    color: "#373737"
                    text: "тыс. ₽"
                    anchors.verticalCenter: parent.verticalCenter
                    font.pixelSize: 20
                    verticalAlignment: Text.AlignBottom
                    textFormat: Text.RichText
                    font.family: "Bahnschrift Light"
                }
            }
        }
    }
}
