

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick
import QtQuick.Controls
import FirstPython

Rectangle {
    id: opInfoContent

    width: 700
    height: 460

    Rectangle {
        id: opNameRectangle
        x: 20
        y: 20
        width: 500
        height: 80
        color: "#53b93f"
        radius: 10

        Text {
            id: text1
            anchors.left: parent.left
            anchors.verticalCenter: parent.verticalCenter
            anchors.leftMargin: 10
            font.styleName: "SemiBold"
            width: 450
            height: 60
            color: "#ffffff"
            text: "Прикладная математика<br>и информатика"
            font.family: Constants.font.family
            font.pointSize: 18
        }
    }
}
