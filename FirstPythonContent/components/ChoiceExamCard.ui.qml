

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
    id: multipleItemRecatngle
    width: 270
    height: 30 + choiceExamListView.height + 10
    color: "#53b93f"
    radius: 10
    anchors.horizontalCenter: parent.horizontalCenter

    Text {
        id: multipleHeaderText
        height: 20
        color: "#ffffff"
        // text: "Выбор из 2 предметов"
        text: model.header
        y: 5
        anchors.horizontalCenter: parent.horizontalCenter
        font.pixelSize: 18
        font.styleName: "Regular"
        font.family: Constants.font.family
    }

    ListView {
        id: choiceExamListView
        x: 0
        y: 30
        width: parent.width - 30
        height: contentHeight
        anchors.horizontalCenter: parent.horizontalCenter

        // Добавляем отступ перед первым элементом
        header: Rectangle {
            width: listView.width
            height: 0
            color: "#00ffffff"
        }

        // Добавляем отступ после последнего элемента
        footer: Rectangle {
            width: listView.width
            height: 0
            color: "#00ffffff"
        }
        spacing: 5 // Добавляем отступ между элементами
        // model: ListModel {
        //     ListElement {
        //         optionNameText: "Физика"
        //     }
        //     ListElement {
        //         optionNameText: "Информатика"
        //     }
        // }
        model: options
        delegate: Rectangle {
            id: examColumnRectangle
            anchors.horizontalCenter: parent.horizontalCenter
            y: 30
            width: 210
            height: 25
            color: "#ffffff"
            radius: 10

            Flickable {
                id: optionNameContainerFlickable
                width: parent.width - 20
                height: optionNameText.height
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
                clip: true
                contentWidth: optionNameText.width < width ? width : optionNameText.width

                Text {
                    id: optionNameText
                    height: 20
                    color: "#000000"
                    text: model.optionNameText
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    font.pixelSize: 16
                    font.styleName: "Regular"
                    font.family: Constants.font.family
                    horizontalAlignment: Text.AlignLeft
                }

                ScrollBar.horizontal: ScrollBar {
                    policy: ScrollBar.Auto // или ScrollBar.Always для постоянного отображения
                }
            }
        }
    }
}
