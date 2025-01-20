

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
    width: 1440
    height: 810
    color: "#ffffff"

    Text {
        width: 375
        height: 100
        color: "#000000"
        text: "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\nhr { height: 1px; border-width: 0; }\nli.unchecked::marker { content: \"\\2610\"; }\nli.checked::marker { content: \"\\2612\"; }\n</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Tw Cen MT'; font-size:24pt; color:#000000;\">Program Insight</span></p></body></html>"
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        textFormat: Text.RichText
        font.family: "Tahoma"
        anchors.verticalCenterOffset: -347
        anchors.horizontalCenterOffset: 1
        font.pointSize: 22
        anchors.centerIn: parent
    }

    Rectangle {
        id: scrollRectangle
        x: 50
        y: 230
        width: 565
        height: 530
        color: "#ffffff"
        radius: 10
        gradient: Gradient {
            GradientStop {
                position: 0
                color: "#196a83"
            }

            GradientStop {
                position: 1
                color: "#50a7c2"
            }
            orientation: Gradient.Vertical
        }

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

    Rectangle {
        id: seaechRectangle
        x: 50
        y: 135
        width: 340
        height: 85
        color: "#ffffff"
        radius: 10
        gradient: Gradient {
            GradientStop {
                position: 0
                color: "#196a83"
            }

            GradientStop {
                position: 1
                color: "#50a7c2"
            }
            orientation: Gradient.Vertical
        }

        Rectangle {
            id: rectangle11
            x: 10
            y: 45
            width: 320
            height: 35
            color: "#b7ffffff"
            radius: 10

            TextInput {
                id: textInput
                x: 8
                y: 0
                width: 304
                height: 35
                text: ""
                font.pixelSize: 16
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                overwriteMode: false
                cursorVisible: false
                passwordCharacter: ""
                inputMask: ""
            }
        }

        Button {
            id: button
            objectName: "button"
            x: 230
            y: 6
            width: 100
            height: 35
            text: qsTr("Фильтры")
            font.pixelSize: 16

            background: Rectangle {
                color: button.pressed ? "#90caf9" : "#b7ffffff" // Изменение цвета при нажатии
                radius: 10
                border.color: "#ffffff"
                border.width: 2
                scale: button.hovered ? 1.05 : 1.0 // Увеличение кнопки при наведении
                Behavior on scale {
                    NumberAnimation {
                        duration: 100
                    }
                }
            }

            contentItem: Text {
                color: "#000000"
                text: "Фильтры"
                font.pixelSize: 16
                anchors.centerIn: parent
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
            }

            //cursorShape: Qt.PointingHandCursor // Изменение курсора
        }

        Text {
            id: _text
            x: 20
            y: 13
            width: 214
            height: 22
            color: "#ffffff"
            text: qsTr("Поиск ОП")
            font.pixelSize: 16
        }
    }

    Rectangle {
        id: countRectangle
        x: 395
        y: 135
        width: 220
        height: 85
        color: "#ffffff"
        radius: 10
        gradient: Gradient {
            GradientStop {
                position: 0
                color: "#196a83"
            }

            GradientStop {
                position: 1
                color: "#50a7c2"
            }
            orientation: Gradient.Vertical
        }

        Text {
            id: _text1
            x: 8
            y: 8
            width: 82
            height: 69
            color: "#ffffff"
            text: qsTr("009")
            font.pixelSize: 36
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }

        Text {
            id: _text2
            x: 96
            y: 32
            width: 98
            height: 22
            color: "#ffffff"
            text: qsTr("ОП найдено")
            font.pixelSize: 16
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }
    }

    Rectangle {
        id: rectangle31
        x: 654
        y: 135
        width: 477
        height: 625
        color: "#ffffff"
        radius: 10
        border.width: 5

        TextEdit {
            id: textEdit
            x: 48
            y: 257
            width: 386
            height: 112
            text: qsTr("ToDo:\nтут можно бахнуть обзор\nключевых показателей по найденным ОП\nи кнопку перехода к дашбордам по\nрезультатам поиска")
            font.pixelSize: 12
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }
    }

    Rectangle {
        id: rectangle32
        x: 1165
        y: 135
        width: 245
        height: 349
        color: "#ffffff"
        radius: 10
        border.width: 5
        TextEdit {
            id: textEdit1
            x: 26
            y: 119
            width: 193
            height: 112
            text: qsTr("ToDo:\nтут можно поставить\nсписок лучших вузов\nпо Data Science\n(и кнопки, чтобы\nпосмотреть подробнее)")
            font.pixelSize: 12
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }
    }

    Rectangle {
        id: rectangle33
        x: 1165
        y: 490
        width: 245
        height: 270
        color: "#ffffff"
        radius: 10
        border.width: 5
        TextEdit {
            id: textEdit2
            x: 26
            y: 79
            width: 193
            height: 112
            text: qsTr("ToDo:\nтут можно перейти к\nразделу с просмотром\nкластеров (они будут\nготовы заранее)")
            font.pixelSize: 12
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }
    }
}
