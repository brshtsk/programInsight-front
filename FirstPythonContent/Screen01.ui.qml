

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
            anchors.fill: parent
            wheelEnabled: true
            ScrollBar.vertical.policy: ScrollBar.AlwaysOff
            clip: true // Ограничение содержимого прокрутки границами ScrollView

            Column {
                id: column
                visible: true
                width: scrollView.width
                anchors.left: parent.left
                spacing: 10 // Можно добавить для красивого расстояния между элементами

                Rectangle {
                    id: rectangle1
                    width: 290
                    height: 70
                    color: "#ffffff"
                    radius: 10
                    layer.wrapMode: ShaderEffectSource.ClampToEdge
                    anchors.horizontalCenter: parent.horizontalCenter

                    TextArea {
                        anchors.fill: parent
                        anchors.leftMargin: 8
                        anchors.rightMargin: 8
                        anchors.topMargin: 0
                        anchors.bottomMargin: 0
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        font.pointSize: 12
                        readOnly: true
                        id: textArea
                        color: "#000000"
                        text: "Программная инженерия\nНИУ ВШЭ"
                    }

                    MouseArea {
                        id: mouseArea1
                        x: 0
                        y: 320
                        anchors.fill: parent
                        hoverEnabled: true
                        cursorShape: Qt.PointingHandCursor
                    }

                    Rectangle {
                        id: rectangle12
                        x: 0
                        y: 0
                        width: 220
                        height: 70
                        color: "#ffffff"
                        radius: 10
                        anchors.horizontalCenterOffset: 260
                        layer.wrapMode: ShaderEffectSource.ClampToEdge
                        TextArea {
                            id: textArea9
                            color: "#26b33a"
                            text: "289\nбаллов ЕГЭ"
                            anchors.fill: parent
                            anchors.leftMargin: 8
                            anchors.rightMargin: 110
                            anchors.topMargin: 0
                            anchors.bottomMargin: 0
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            font.styleName: "Полужирный"
                            readOnly: true
                            font.pointSize: 12
                        }

                        Rectangle {
                            id: rectangle15
                            x: 109
                            y: 10
                            width: 2
                            height: 50
                            color: "#000000"
                        }

                        TextArea {
                            id: textArea10
                            color: "#26b33a"
                            text: "700к ₽\nстоимость"
                            anchors.fill: parent
                            anchors.leftMargin: 110
                            anchors.rightMargin: 8
                            anchors.topMargin: 0
                            anchors.bottomMargin: 0
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            font.styleName: "Полужирный"
                            readOnly: true
                            font.pointSize: 12
                        }

                        MouseArea {
                            id: mouseArea10
                            x: 0
                            y: 320
                            anchors.fill: parent
                            hoverEnabled: true
                            cursorShape: Qt.PointingHandCursor
                        }

                        anchors.horizontalCenter: parent.horizontalCenter
                    }
                }

                RowLayout {
                    id: opRow
                    width: parent.width
                    height: 70

                    Item {
                        Layout.fillWidth: true // Заполнитель между прямоугольниками
                        //Layout.weight: 2 // Левый заполнитель пошире
                    }

                    Rectangle {
                        id: opNameRectangle
                        width: 290
                        height: 70
                        color: "#ffffff"
                        radius: 10
                        Layout.alignment: Qt.AlignLeft

                        TextArea {
                            anchors.fill: parent
                            anchors.leftMargin: 8
                            anchors.rightMargin: 8
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            font.pointSize: 12
                            readOnly: true
                            id: opTextArea
                            color: "#000000"
                            text: "Программная инженерия\nНИУ ВШЭ"
                        }
                    }

                    Item {
                        Layout.fillWidth: true // Заполнитель между прямоугольниками
                        //Layout.weight: 1 // Средний заполнитель поуже
                    }

                    Rectangle {
                        id: opInfoRectangle
                        width: 220
                        height: 70
                        color: "#ffffff"
                        radius: 10
                        Layout.alignment: Qt.AlignRight
                    }

                    Item {
                        Layout.fillWidth: true // Заполнитель между прямоугольниками
                        //Layout.weight: 2 // Правый заполнитель пошире
                    }
                }

                Rectangle {
                    id: rectangle2
                    width: 290
                    height: 70
                    color: "#ffffff"
                    radius: 10
                    layer.wrapMode: ShaderEffectSource.ClampToEdge
                    TextArea {
                        id: textArea1
                        color: "#000000"
                        text: "Прикладная математика и\nинформатика\nНИУ ВШЭ"
                        anchors.fill: parent
                        anchors.leftMargin: 8
                        anchors.rightMargin: 8
                        anchors.topMargin: 0
                        anchors.bottomMargin: 0
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        readOnly: true
                        font.pointSize: 12
                    }

                    MouseArea {
                        id: mouseArea2
                        x: 0
                        y: -80
                        anchors.fill: parent
                        hoverEnabled: true
                        cursorShape: Qt.PointingHandCursor
                    }

                    Rectangle {
                        id: rectangle13
                        x: 0
                        y: 0
                        width: 220
                        height: 70
                        color: "#ffffff"
                        radius: 10
                        layer.wrapMode: ShaderEffectSource.ClampToEdge
                        TextArea {
                            id: textArea11
                            color: "#26b33a"
                            text: "298\nбаллов ЕГЭ"
                            anchors.fill: parent
                            anchors.leftMargin: 8
                            anchors.rightMargin: 110
                            anchors.topMargin: 0
                            anchors.bottomMargin: 0
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            readOnly: true
                            font.styleName: "Полужирный"
                            font.pointSize: 12
                        }

                        Rectangle {
                            id: rectangle16
                            x: 109
                            y: 10
                            width: 2
                            height: 50
                            color: "#000000"
                        }

                        TextArea {
                            id: textArea12
                            color: "#26b33a"
                            text: "3млрд $\nстоимость"
                            anchors.fill: parent
                            anchors.leftMargin: 110
                            anchors.rightMargin: 8
                            anchors.topMargin: 0
                            anchors.bottomMargin: 0
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            readOnly: true
                            font.styleName: "Полужирный"
                            font.pointSize: 12
                        }

                        MouseArea {
                            id: mouseArea11
                            x: 0
                            y: 320
                            anchors.fill: parent
                            hoverEnabled: true
                            cursorShape: Qt.PointingHandCursor
                        }
                        anchors.horizontalCenterOffset: 260
                        anchors.horizontalCenter: parent.horizontalCenter
                    }
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                Rectangle {
                    id: rectangle3
                    width: 290
                    height: 70
                    color: "#ffffff"
                    radius: 10
                    layer.wrapMode: ShaderEffectSource.ClampToEdge
                    TextArea {
                        id: textArea2
                        color: "#000000"
                        text: "Прикладная математика и\nинформатика\nМФТИ"
                        anchors.fill: parent
                        anchors.leftMargin: 8
                        anchors.rightMargin: 8
                        anchors.topMargin: 0
                        anchors.bottomMargin: 0
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        readOnly: true
                        font.pointSize: 12
                    }

                    MouseArea {
                        id: mouseArea3
                        x: 0
                        y: -80
                        anchors.fill: parent
                        hoverEnabled: true
                        cursorShape: Qt.PointingHandCursor
                    }

                    Rectangle {
                        id: rectangle14
                        x: 0
                        y: 0
                        width: 220
                        height: 70
                        color: "#ffffff"
                        radius: 10
                        layer.wrapMode: ShaderEffectSource.ClampToEdge
                        TextArea {
                            id: textArea13
                            color: "#26b33a"
                            text: "52\nбаллов ЕГЭ"
                            anchors.fill: parent
                            anchors.leftMargin: 8
                            anchors.rightMargin: 110
                            anchors.topMargin: 0
                            anchors.bottomMargin: 0
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            readOnly: true
                            font.styleName: "Полужирный"
                            font.pointSize: 12
                        }

                        Rectangle {
                            id: rectangle17
                            x: 109
                            y: 10
                            width: 2
                            height: 50
                            color: "#000000"
                        }

                        TextArea {
                            id: textArea14
                            color: "#26b33a"
                            text: "560к ₽\nстоимость"
                            anchors.fill: parent
                            anchors.leftMargin: 110
                            anchors.rightMargin: 8
                            anchors.topMargin: 0
                            anchors.bottomMargin: 0
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            readOnly: true
                            font.styleName: "Полужирный"
                            font.pointSize: 12
                        }

                        MouseArea {
                            id: mouseArea12
                            x: 0
                            y: 320
                            anchors.fill: parent
                            hoverEnabled: true
                            cursorShape: Qt.PointingHandCursor
                        }
                        anchors.horizontalCenterOffset: 260
                        anchors.horizontalCenter: parent.horizontalCenter
                    }
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                Rectangle {
                    id: rectangle4
                    width: 290
                    height: 70
                    color: "#ffffff"
                    radius: 10
                    layer.wrapMode: ShaderEffectSource.ClampToEdge
                    TextArea {
                        id: textArea3
                        color: "#000000"
                        text: "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧"
                        anchors.fill: parent
                        anchors.leftMargin: 8
                        anchors.rightMargin: 8
                        anchors.topMargin: 0
                        anchors.bottomMargin: 0
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        readOnly: true
                        font.pointSize: 12
                    }

                    MouseArea {
                        id: mouseArea4
                        x: 0
                        y: -80
                        anchors.fill: parent
                        hoverEnabled: true
                        cursorShape: Qt.PointingHandCursor
                    }

                    Rectangle {
                        id: rectangle18
                        x: 0
                        y: 0
                        width: 220
                        height: 70
                        color: "#ffffff"
                        radius: 10
                        layer.wrapMode: ShaderEffectSource.ClampToEdge
                        TextArea {
                            id: textArea15
                            color: "#26b33a"
                            text: "999\nбаллов ЕГЭ"
                            anchors.fill: parent
                            anchors.leftMargin: 8
                            anchors.rightMargin: 110
                            anchors.topMargin: 0
                            anchors.bottomMargin: 0
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            readOnly: true
                            font.styleName: "Полужирный"
                            font.pointSize: 12
                        }

                        Rectangle {
                            id: rectangle19
                            x: 109
                            y: 10
                            width: 2
                            height: 50
                            color: "#000000"
                        }

                        TextArea {
                            id: textArea16
                            color: "#26b33a"
                            text: "70 ₽\nстоимость"
                            anchors.fill: parent
                            anchors.leftMargin: 110
                            anchors.rightMargin: 8
                            anchors.topMargin: 0
                            anchors.bottomMargin: 0
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            readOnly: true
                            font.styleName: "Полужирный"
                            font.pointSize: 12
                        }

                        MouseArea {
                            id: mouseArea13
                            x: 0
                            y: 320
                            anchors.fill: parent
                            hoverEnabled: true
                            cursorShape: Qt.PointingHandCursor
                        }
                        anchors.horizontalCenterOffset: 260
                        anchors.horizontalCenter: parent.horizontalCenter
                    }
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                Rectangle {
                    id: rectangle5
                    width: 290
                    height: 70
                    color: "#ffffff"
                    radius: 10
                    layer.wrapMode: ShaderEffectSource.ClampToEdge
                    TextArea {
                        id: textArea4
                        color: "#000000"
                        text: "🫡🫡🫡"
                        anchors.fill: parent
                        anchors.leftMargin: 8
                        anchors.rightMargin: 8
                        anchors.topMargin: 0
                        anchors.bottomMargin: 0
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        readOnly: true
                        font.pointSize: 12
                    }

                    MouseArea {
                        id: mouseArea5
                        x: 0
                        y: -80
                        anchors.fill: parent
                        hoverEnabled: true
                        cursorShape: Qt.PointingHandCursor
                    }

                    Rectangle {
                        id: rectangle20
                        x: 0
                        y: 0
                        width: 220
                        height: 70
                        color: "#ffffff"
                        radius: 10
                        layer.wrapMode: ShaderEffectSource.ClampToEdge
                        TextArea {
                            id: textArea17
                            color: "#26b33a"
                            text: "-4\nбаллов ЕГЭ"
                            anchors.fill: parent
                            anchors.leftMargin: 8
                            anchors.rightMargin: 110
                            anchors.topMargin: 0
                            anchors.bottomMargin: 0
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            readOnly: true
                            font.styleName: "Полужирный"
                            font.pointSize: 12
                        }

                        Rectangle {
                            id: rectangle21
                            x: 109
                            y: 10
                            width: 2
                            height: 50
                            color: "#000000"
                        }

                        TextArea {
                            id: textArea18
                            color: "#26b33a"
                            text: "80к ₽\nстоимость"
                            anchors.fill: parent
                            anchors.leftMargin: 110
                            anchors.rightMargin: 8
                            anchors.topMargin: 0
                            anchors.bottomMargin: 0
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            readOnly: true
                            font.styleName: "Полужирный"
                            font.pointSize: 12
                        }

                        MouseArea {
                            id: mouseArea14
                            x: 0
                            y: 320
                            anchors.fill: parent
                            hoverEnabled: true
                            cursorShape: Qt.PointingHandCursor
                        }
                        anchors.horizontalCenterOffset: 260
                        anchors.horizontalCenter: parent.horizontalCenter
                    }
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                Rectangle {
                    id: rectangle6
                    width: 290
                    height: 70
                    color: "#ffffff"
                    radius: 10
                    layer.wrapMode: ShaderEffectSource.ClampToEdge
                    TextArea {
                        id: textArea5
                        color: "#000000"
                        text: "o((>ω< ))o"
                        anchors.fill: parent
                        anchors.leftMargin: 8
                        anchors.rightMargin: 8
                        anchors.topMargin: 0
                        anchors.bottomMargin: 0
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        readOnly: true
                        font.pointSize: 12
                    }

                    MouseArea {
                        id: mouseArea6
                        x: 0
                        y: -80
                        anchors.fill: parent
                        hoverEnabled: true
                        cursorShape: Qt.PointingHandCursor
                    }

                    Rectangle {
                        id: rectangle22
                        x: 0
                        y: 0
                        width: 220
                        height: 70
                        color: "#ffffff"
                        radius: 10
                        layer.wrapMode: ShaderEffectSource.ClampToEdge
                        TextArea {
                            id: textArea19
                            color: "#26b33a"
                            text: "25\nбаллов ЕГЭ"
                            anchors.fill: parent
                            anchors.leftMargin: 8
                            anchors.rightMargin: 110
                            anchors.topMargin: 0
                            anchors.bottomMargin: 0
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            readOnly: true
                            font.styleName: "Полужирный"
                            font.pointSize: 12
                        }

                        Rectangle {
                            id: rectangle23
                            x: 109
                            y: 10
                            width: 2
                            height: 50
                            color: "#000000"
                        }

                        TextArea {
                            id: textArea20
                            color: "#26b33a"
                            text: "700к ₽\nстоимость"
                            anchors.fill: parent
                            anchors.leftMargin: 110
                            anchors.rightMargin: 8
                            anchors.topMargin: 0
                            anchors.bottomMargin: 0
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            readOnly: true
                            font.styleName: "Полужирный"
                            font.pointSize: 12
                        }

                        MouseArea {
                            id: mouseArea15
                            x: 0
                            y: 320
                            anchors.fill: parent
                            hoverEnabled: true
                            cursorShape: Qt.PointingHandCursor
                        }
                        anchors.horizontalCenterOffset: 260
                        anchors.horizontalCenter: parent.horizontalCenter
                    }
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                Rectangle {
                    id: rectangle7
                    width: 290
                    height: 70
                    color: "#ffffff"
                    radius: 10
                    layer.wrapMode: ShaderEffectSource.ClampToEdge
                    TextArea {
                        id: textArea6
                        color: "#000000"
                        text: "🐘"
                        anchors.fill: parent
                        anchors.leftMargin: 8
                        anchors.rightMargin: 8
                        anchors.topMargin: 0
                        anchors.bottomMargin: 0
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        readOnly: true
                        font.pointSize: 12
                    }

                    MouseArea {
                        id: mouseArea7
                        x: 0
                        y: -80
                        anchors.fill: parent
                        hoverEnabled: true
                        cursorShape: Qt.PointingHandCursor
                    }

                    Rectangle {
                        id: rectangle24
                        x: 0
                        y: 0
                        width: 220
                        height: 70
                        color: "#ffffff"
                        radius: 10
                        layer.wrapMode: ShaderEffectSource.ClampToEdge
                        TextArea {
                            id: textArea21
                            color: "#26b33a"
                            text: "42\nбаллов ЕГЭ"
                            anchors.fill: parent
                            anchors.leftMargin: 8
                            anchors.rightMargin: 110
                            anchors.topMargin: 0
                            anchors.bottomMargin: 0
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            readOnly: true
                            font.styleName: "Полужирный"
                            font.pointSize: 12
                        }

                        Rectangle {
                            id: rectangle25
                            x: 109
                            y: 10
                            width: 2
                            height: 50
                            color: "#000000"
                        }

                        TextArea {
                            id: textArea22
                            color: "#26b33a"
                            text: "700к ₽\nстоимость"
                            anchors.fill: parent
                            anchors.leftMargin: 110
                            anchors.rightMargin: 8
                            anchors.topMargin: 0
                            anchors.bottomMargin: 0
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            readOnly: true
                            font.styleName: "Полужирный"
                            font.pointSize: 12
                        }

                        MouseArea {
                            id: mouseArea16
                            x: 0
                            y: 320
                            anchors.fill: parent
                            hoverEnabled: true
                            cursorShape: Qt.PointingHandCursor
                        }
                        anchors.horizontalCenterOffset: 260
                        anchors.horizontalCenter: parent.horizontalCenter
                    }
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                Rectangle {
                    id: rectangle8
                    width: 290
                    height: 70
                    color: "#ffffff"
                    radius: 10
                    layer.wrapMode: ShaderEffectSource.ClampToEdge
                    TextArea {
                        id: textArea7
                        color: "#000000"
                        text: "OwO"
                        anchors.fill: parent
                        anchors.leftMargin: 8
                        anchors.rightMargin: 8
                        anchors.topMargin: 0
                        anchors.bottomMargin: 0
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        readOnly: true
                        font.pointSize: 12
                    }

                    MouseArea {
                        id: mouseArea8
                        x: 0
                        y: -80
                        anchors.fill: parent
                        hoverEnabled: true
                        cursorShape: Qt.PointingHandCursor
                    }

                    Rectangle {
                        id: rectangle26
                        x: 0
                        y: 0
                        width: 220
                        height: 70
                        color: "#ffffff"
                        radius: 10
                        layer.wrapMode: ShaderEffectSource.ClampToEdge
                        TextArea {
                            id: textArea23
                            color: "#26b33a"
                            text: "0\nбаллов ЕГЭ"
                            anchors.fill: parent
                            anchors.leftMargin: 8
                            anchors.rightMargin: 110
                            anchors.topMargin: 0
                            anchors.bottomMargin: 0
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            readOnly: true
                            font.styleName: "Полужирный"
                            font.pointSize: 12
                        }

                        Rectangle {
                            id: rectangle27
                            x: 109
                            y: 10
                            width: 2
                            height: 50
                            color: "#000000"
                        }

                        TextArea {
                            id: textArea24
                            color: "#26b33a"
                            text: "0 ₽\nстоимость"
                            anchors.fill: parent
                            anchors.leftMargin: 110
                            anchors.rightMargin: 8
                            anchors.topMargin: 0
                            anchors.bottomMargin: 0
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            readOnly: true
                            font.styleName: "Полужирный"
                            font.pointSize: 12
                        }

                        MouseArea {
                            id: mouseArea17
                            x: 0
                            y: 320
                            anchors.fill: parent
                            hoverEnabled: true
                            cursorShape: Qt.PointingHandCursor
                        }
                        anchors.horizontalCenterOffset: 260
                        anchors.horizontalCenter: parent.horizontalCenter
                    }
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                Rectangle {
                    id: rectangle9
                    width: 290
                    height: 70
                    color: "#ffffff"
                    radius: 10
                    layer.wrapMode: ShaderEffectSource.ClampToEdge
                    TextArea {
                        id: textArea8
                        color: "#000000"
                        text: "Текст..."
                        anchors.fill: parent
                        anchors.leftMargin: 8
                        anchors.rightMargin: 8
                        anchors.topMargin: 0
                        anchors.bottomMargin: 0
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        readOnly: true
                        font.pointSize: 12
                    }

                    MouseArea {
                        id: mouseArea9
                        x: 130
                        y: -640
                        anchors.fill: parent
                        hoverEnabled: true
                        cursorShape: Qt.PointingHandCursor
                    }

                    Rectangle {
                        id: rectangle28
                        x: 0
                        y: 0
                        width: 220
                        height: 70
                        color: "#ffffff"
                        radius: 10
                        layer.wrapMode: ShaderEffectSource.ClampToEdge
                        TextArea {
                            id: textArea25
                            color: "#26b33a"
                            text: "389\nбаллов ЕГЭ"
                            anchors.fill: parent
                            anchors.leftMargin: 8
                            anchors.rightMargin: 110
                            anchors.topMargin: 0
                            anchors.bottomMargin: 0
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            readOnly: true
                            font.styleName: "Полужирный"
                            font.pointSize: 12
                        }

                        Rectangle {
                            id: rectangle29
                            x: 109
                            y: 10
                            width: 2
                            height: 50
                            color: "#000000"
                        }

                        TextArea {
                            id: textArea26
                            color: "#26b33a"
                            text: "55к ₽\nстоимость"
                            anchors.fill: parent
                            anchors.leftMargin: 110
                            anchors.rightMargin: 8
                            anchors.topMargin: 0
                            anchors.bottomMargin: 0
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            readOnly: true
                            font.styleName: "Полужирный"
                            font.pointSize: 12
                        }

                        MouseArea {
                            id: mouseArea18
                            x: 0
                            y: 320
                            anchors.fill: parent
                            hoverEnabled: true
                            cursorShape: Qt.PointingHandCursor
                        }
                        anchors.horizontalCenterOffset: 260
                        anchors.horizontalCenter: parent.horizontalCenter
                    }
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                Rectangle {
                    id: end_empty_rectangle
                    width: 200
                    height: 30
                    color: "#00ffffff"
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
