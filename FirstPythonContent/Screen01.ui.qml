

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick
import QtQuick.Controls
//2.15
import QtQuick.Window
//2.15
import QtQuick.Layouts
//1.15
import FirstPython
import QtQuick.Studio.DesignEffects

Rectangle {
    width: 1360
    height: 810
    color: "#ffffff"

    Rectangle {
        id: backSearchZoneRectangle
        x: 250

        y: 30
        width: 480
        height: 770
        color: "#dde9db"
        radius: 10
        border.width: 0

        Rectangle {
            id: scrollRectangle
            x: 0
            y: 95
            width: parent.width
            height: 675
            visible: true
            color: "#00ffffff"
            radius: 10
            border.width: 0

            ScrollView {
                id: scrollView
                //anchors.fill: parent
                width: parent.width
                height: parent.height
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.leftMargin: 10 // Отступ слева
                anchors.rightMargin: 10 // Отступ справа
                wheelEnabled: true
                ScrollBar.vertical.policy: ScrollBar.AlwaysOff
                clip: true // Ограничение содержимого прокрутки границами ScrollView

                ListView {
                    id: listView
                    anchors.fill: parent
                    // Добавляем отступ перед первым элементом
                    header: Rectangle {
                        width: listView.width
                        height: 15
                        color: "#00ffffff"
                    }

                    // Добавляем отступ после последнего элемента
                    footer: Rectangle {
                        width: listView.width
                        height: 15
                        color: "#00ffffff"
                    }
                    spacing: 15 // Добавляем отступ между элементами
                    model: customModel
                    // // Тестовая модель
                    // model: ListModel {
                    //     ListElement {
                    //         opNameText: "Программная<br>инженерия"
                    //         info1Text: "289"
                    //         info2Text: "700к ₽"
                    //         universityNameText: "НИУ ВШЭ"
                    //         opCodeText: "09.03.04"
                    //         imageSource: "resources/hselogo.svg"
                    //     }
                    //     ListElement {
                    //         opNameText: "Прикладная математика<br>и информатика"
                    //         info1Text: "300"
                    //         info2Text: "720к ₽"
                    //         universityNameText: "НИУ ВШЭ"
                    //         opCodeText: "01.03.02"
                    //         imageSource: "resources/hselogo.svg"
                    //     }
                    //     ListElement {
                    //         opNameText: "Анализ данных<br>в экономике"
                    //         info1Text: "272"
                    //         info2Text: "470к ₽"
                    //         universityNameText: "МФТИ"
                    //         opCodeText: "38.03.01"
                    //         imageSource: "resources/mfti-logo.png"
                    //     }
                    //     ListElement {
                    //         opNameText: "Физика<br>и нанотехнологии"
                    //         info1Text: "280"
                    //         info2Text: "500к ₽"
                    //         universityNameText: "МФТИ"
                    //         opCodeText: "16.03.01"
                    //         imageSource: "resources/mfti-logo.png"
                    //     }
                    //     ListElement {
                    //         opNameText: "Информационная<br>безопасность"
                    //         info1Text: "260"
                    //         info2Text: "450к ₽"
                    //         universityNameText: "МИРЭА"
                    //         opCodeText: "10.03.01"
                    //         imageSource: "resources/other-logo.svg"
                    //     }
                    // }
                    delegate: Rectangle {
                        id: opRowRectangle
                        x: 260
                        y: 165
                        width: 420
                        height: 170
                        color: "#53b93f"
                        radius: 10
                        anchors.horizontalCenter: parent.horizontalCenter // Центрируем

                        Image {
                            id: universityImage
                            x: 15
                            y: 80
                            width: 75
                            height: 75
                            source: model.imageSource
                            fillMode: Image.PreserveAspectFit
                        }

                        Text {
                            id: opNameText
                            x: 15
                            y: 15
                            width: parent.width - 30
                            height: 65
                            color: "#ffffff"
                            text: model.opNameText
                            font.pixelSize: 24
                            textFormat: Text.RichText
                            font.family: "Bahnschrift SemiBold"
                        }

                        Text {
                            id: universityNameText
                            x: 95
                            y: 80
                            width: 120
                            height: 35
                            color: "#ffffff"
                            text: model.universityNameText
                            font.pixelSize: 18
                            horizontalAlignment: Text.AlignLeft
                            verticalAlignment: Text.AlignBottom
                            textFormat: Text.RichText
                            font.family: "Bahnschrift SemiBold"
                        }

                        Text {
                            id: opCodeText
                            x: 96
                            y: 120
                            width: 120
                            height: 35
                            color: "#ffffff"
                            text: model.opCodeText
                            font.pixelSize: 18
                            horizontalAlignment: Text.AlignLeft
                            verticalAlignment: Text.AlignTop
                            textFormat: Text.RichText
                            font.family: "Bahnschrift SemiBold"
                        }

                        Rectangle {
                            id: info1Rectangle
                            x: 251
                            y: 80
                            width: 72
                            height: 48
                            color: "#ffffff"
                            radius: 10

                            Text {
                                id: info1Text
                                font.pixelSize: 20
                                horizontalAlignment: Text.AlignHCenter
                                verticalAlignment: Text.AlignVCenter
                                font.family: "Bahnschrift SemiBold"
                                width: parent.width
                                height: parent.height
                                color: "#53b93f"
                                anchors.left: parent.left
                                anchors.right: parent.right
                                anchors.leftMargin: 10 // Отступ слева
                                anchors.rightMargin: 10 // Отступ справа
                                text: model.info1Text
                            }
                        }

                        Rectangle {
                            id: info2Rectangle
                            x: 333
                            y: 80
                            width: 72
                            height: 48
                            color: "#ffffff"
                            radius: 10

                            Text {
                                id: info2Text
                                font.pixelSize: 20
                                horizontalAlignment: Text.AlignHCenter
                                verticalAlignment: Text.AlignVCenter
                                font.family: "Bahnschrift SemiBold"
                                width: parent.width
                                height: parent.height
                                color: "#53b93f"
                                anchors.left: parent.left
                                anchors.right: parent.right
                                anchors.leftMargin: 10 // Отступ слева
                                anchors.rightMargin: 10 // Отступ справа
                                text: model.info2Text
                            }
                        }

                        Text {
                            id: typeInfo1Text
                            x: 251
                            y: 130
                            width: 72
                            height: 16
                            color: "#ffffff"
                            text: qsTr("Баллов ЕГЭ")
                            font.pixelSize: 12
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                        }

                        Text {
                            id: typeInfo2Text
                            x: 333
                            y: 130
                            width: 72
                            height: 16
                            color: "#ffffff"
                            text: qsTr("Стоимость")
                            font.pixelSize: 12
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                        }
                    }
                }
            }
        }

        Item {
            id: upperZoneItem
            y: 10
            height: 80
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 20
            anchors.rightMargin: 20

            Button {
                id: searchSettingsButton
                objectName: "button"
                width: 48
                height: 72
                font.pixelSize: 16
                icon.color: "#ffffff"
                icon.source: "resources/icons8-настройки-48.png"
                anchors.right: parent.right
                anchors.verticalCenter: parent.verticalCenter

                background: Rectangle {
                    color: searchSettingsButton.pressed ? "#7dd96b" : "#53b93f" // Изменение цвета при нажатии
                    radius: 10
                    scale: searchSettingsButton.hovered ? 1.05 : 1.0 // Увеличение кнопки при наведении
                    Behavior on scale {
                        NumberAnimation {
                            duration: 100
                        }
                    }
                }
            }

            Item {
                id: _item
                width: 200
                height: 70
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter

                Text {
                    id: searchOpText
                    text: "Поиск ОП"
                    font.pixelSize: 36
                    textFormat: Text.RichText
                    font.family: "Bahnschrift SemiBold"
                    anchors.left: parent.left
                    anchors.top: parent.top
                }

                Text {
                    id: resultAmountText
                    color: "#373737"
                    text: "Получено 009 результатов"
                    anchors.left: parent.left
                    font.pixelSize: 18
                    textFormat: Text.RichText
                    font.family: "Bahnschrift Light SemiCondensed"
                    anchors.bottom: parent.bottom
                }
            }
        }
    }
}
