

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
        width: 565
        height: 770
        color: "#dde9db"
        radius: 10
        border.width: 0

        Rectangle {
            id: scrollRectangle
            x: 0
            y: 95
            width: 565
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
                    model: customModel
                    // // Тестовая модель
                    // model: ListModel {
                    //     ListElement {
                    //         opText: "Программная инженерия<br/>НИУ ВШЭ"
                    //         info1Text: "289<br/>баллов ЕГЭ"
                    //         info2Text: "700к ₽<br/>стоимость"
                    //     }
                    //     ListElement {
                    //         opText: "Операция 2"
                    //         info1Text: "Инфо 2.1"
                    //         info2Text: "Инфо 2.2"
                    //     }
                    //     ListElement {
                    //         opText: "Операция 3"
                    //         info1Text: "Инфо 3.1"
                    //         info2Text: "Инфо 3.2"
                    //     }
                    // }
                    delegate: Item {
                        width: listView.width
                        height: 80

                        RowLayout {
                            id: opRow
                            width: parent.width
                            height: parent.height

                            Item {
                                Layout.fillWidth: true
                            }

                            Rectangle {
                                id: opNameRectangle
                                width: 290
                                height: 70
                                color: "#ffffff"
                                radius: 10
                                Layout.alignment: Qt.AlignLeft

                                Text {
                                    anchors.fill: parent
                                    anchors.leftMargin: 8
                                    anchors.rightMargin: 8
                                    horizontalAlignment: Text.AlignHCenter
                                    verticalAlignment: Text.AlignVCenter
                                    font.pointSize: 12
                                    id: opText
                                    color: "#000000"
                                    text: model.opText
                                    textFormat: Text.RichText
                                }
                            }

                            Item {
                                Layout.fillWidth: true
                            }

                            Rectangle {
                                id: opInfoRectangle
                                width: 220
                                height: 70
                                color: "#ffffff"
                                radius: 10
                                Layout.alignment: Qt.AlignRight

                                RowLayout {
                                    id: opInfoLayout
                                    width: parent.width
                                    height: parent.height

                                    Text {
                                        id: info1Text
                                        color: "#26b33a"
                                        text: model.info1Text
                                        font.styleName: "Полужирный"
                                        font.pointSize: 12
                                        horizontalAlignment: Text.AlignHCenter
                                        verticalAlignment: Text.AlignVCenter
                                        anchors.leftMargin: 8
                                        anchors.rightMargin: 8
                                        Layout.fillWidth: true
                                        textFormat: Text.RichText
                                    }

                                    Rectangle {
                                        id: separator
                                        width: 2
                                        height: 50
                                        color: "#000000"
                                        Layout.preferredWidth: 2
                                    }

                                    Text {
                                        id: info2Text
                                        color: "#26b33a"
                                        text: model.info2Text
                                        font.styleName: "Полужирный"
                                        font.pointSize: 12
                                        horizontalAlignment: Text.AlignHCenter
                                        verticalAlignment: Text.AlignVCenter
                                        anchors.leftMargin: 8
                                        anchors.rightMargin: 8
                                        Layout.fillWidth: true
                                        textFormat: Text.RichText
                                    }
                                }
                            }

                            Item {
                                Layout.fillWidth: true
                            }
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
                    text: "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\nhr { height: 1px; border-width: 0; }\nli.unchecked::marker { content: \"\\2610\"; }\nli.checked::marker { content: \"\\2612\"; }\n</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift SemiBold'; font-size:28pt;\">Поиск ОП</span></p></body></html>"
                    font.pixelSize: 24
                    textFormat: Text.RichText
                    font.family: "Tahoma"
                    anchors.left: parent.left
                    anchors.top: parent.top
                }

                Text {
                    id: searchOpText1
                    text: "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\nhr { height: 1px; border-width: 0; }\nli.unchecked::marker { content: \"\\2610\"; }\nli.checked::marker { content: \"\\2612\"; }\n</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Bahnschrift Light SemiCondensed'; font-size:14pt; color:#343434;\">Получено 009 результатов</span></p></body></html>"
                    anchors.left: parent.left
                    font.pixelSize: 24
                    textFormat: Text.RichText
                    font.family: "Tahoma"
                    anchors.bottom: parent.bottom
                }
            }
        }
    }
}
