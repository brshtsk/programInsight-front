import QtQuick
import QtQuick.Controls
import FirstPython
import "components"

Rectangle {
    id: root
    width: 340
    height: 350

    Button {
        id: saveExamButton
        objectName: "saveExamButton"
        x: 20
        y: 300
        width: 300
        height: 30

        font.pixelSize: 18
        font.family: Constants.font.family
        font.styleName: "SemiBold"

        contentItem: Text {
            scale: saveExamButton.hovered ? 1.05 : 1.0
            font: saveExamButton.font
            color: "#FFFFFF"
            text: "Сохранить предмет" // Белый цвет текста
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            Behavior on scale {
                NumberAnimation {
                    duration: 100
                }
            }
        }

        background: Rectangle {
            color: saveExamButton.pressed ? "#7dd96b" : "#53b93f"
            radius: 10
            scale: saveExamButton.hovered ? 1.05 : 1.0
            Behavior on scale {
                NumberAnimation {
                    duration: 100
                }
            }
            Behavior on color {
                ColorAnimation {
                    duration: 200
                }
            }
        }
    }

    Item {
        id: upperZoneItem
        x: 20
        y: 20
        width: 300
        height: 50

        Text {
            id: headerText
            x: 10
            anchors.verticalCenter: parent.verticalCenter
            height: 25
            text: "Новый предмет"
            font.pixelSize: 24
            font.styleName: "SemiBold"
            font.family: Constants.font.family
        }

        Rectangle {
            id: newExamHelpRectangle
            x: 193
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
                id: helpMouseArea
                anchors.fill: parent
                hoverEnabled: true
            }

            ToolTip {
                text: "Подсказка:<br><br>Введите информацию о сдаваеомом экзамене.<br>Если вам известен балл за экзамен, укажите его."
                visible: helpMouseArea.containsMouse
            }
        }
    }

    Rectangle {
        id: propertiesRectangle
        x: 20
        y: 190
        width: 300
        height: 100
        color: "#dde9db"
        radius: 10

        Item {
            id: examTypeItem
            x: 10
            y: 10
            width: 280
            height: 40

            Text {
                id: examTypeText
                color: "#373737"
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter
                text: "Тип экзамена"
                font.pixelSize: 21
                font.styleName: "SemiBold"
                font.family: Constants.font.family
            }

            ComboBox {
                id: examTypeComboBox
                objectName: "examTypeComboBox"
                anchors.verticalCenter: parent.verticalCenter
                height: 30
                anchors.right: parent.right
                anchors.rightMargin: 5
                width: 120

                model: ["ЕГЭ/ДВИ", "Доп баллы ЕГЭ", "Магистратура"]

                // Кастомизация фон и текстового содержимого
                contentItem: Rectangle {
                    id: examComboBoxBackground
                    anchors.fill: parent
                    anchors.leftMargin: -5
                    anchors.rightMargin: -5
                    color: "#53b93f"
                    radius: 10

                    Text {
                        width: parent.width - 20
                        text: examTypeComboBox.currentText === "Магистратура" ? "Магстр..." : examTypeComboBox.currentText === "Доп баллы ЕГЭ" ? "Доп ЕГЭ" : examTypeComboBox.currentText
                        color: "#ffffff"
                        anchors.centerIn: parent
                        font.pixelSize: 18
                        font.family: Constants.font.family
                        font.styleName: "SemiBold"
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
            id: scoreItem
            x: 10
            y: 50
            width: 280
            height: 40
            Text {
                id: scoreText
                color: "#373737"
                text: "Балл за экзамен"
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                font.pixelSize: 21
                font.styleName: "SemiBold"
                font.family: Constants.font.family
            }

            TextField {
                id: examScoreTextField
                anchors.right: parent.right
                objectName: "examScoreTextField"
                width: 65
                height: 35 // Увеличьте высоту
                placeholderText: ""
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
        }
    }

    Rectangle {
        id: examNameRectangle
        x: 20
        y: 80
        width: 300
        height: 100
        color: "#dde9db"
        radius: 10

        Item {
            id: examNameItem
            x: 10
            y: 10
            width: 220
            height: 40

            Text {
                id: examNameText
                color: "#373737"
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter
                text: "Название"
                font.pixelSize: 21
                font.styleName: "SemiBold"
                font.family: Constants.font.family
            }
        }

        Item {
            id: examNameInputItem
            x: 10
            y: 50
            width: 280
            height: 40

            TextFieldWithCompleter {
                id: examNameTextField
                anchors.verticalCenter: parent.verticalCenter
                anchors.right: parent.right
                objectName: "examNameTextField"
                width: parent.width
                height: 35
                placeholder: "введите название предмета"
                availableValues: ["Программная инженерия", "Прикладная математика", "Прикладной анализ данных", "Прикладная математика и информатика", "Компьютерные науки и анализ данных"]
                maxCompitionsAmount: 5
            }
        }
    }
}
