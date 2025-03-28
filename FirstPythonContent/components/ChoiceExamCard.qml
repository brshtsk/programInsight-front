import QtQuick
import QtQuick.Controls
import FirstPython

Rectangle {
    id: multipleItemRectangle
    property var examData: model // сохраняем внешние данные в отдельное свойство

    width: 270
    height: 30 + choiceExamListView.height + 10
    color: "#53b93f"
    radius: 10
    anchors.horizontalCenter: parent.horizontalCenter

    Text {
        id: multipleHeaderText
        height: 20
        color: "#ffffff"
        text: examData.header // теперь берём заголовок из внешней модели
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
        spacing: 5

        interactive: false

        // Заголовок и футер можно оставить, если они нужны
        header: Rectangle {
            width: listView.width
            height: 0
            color: "#00ffffff"
        }
        footer: Rectangle {
            width: listView.width
            height: 0
            color: "#00ffffff"
        }

        // Используем данные из внешней модели, сохранённые в examData.options
        model: examData.options

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
                    text: modelData.optionNameText
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    font.pixelSize: 16
                    font.styleName: "Regular"
                    font.family: Constants.font.family
                    horizontalAlignment: Text.AlignLeft
                }

                ScrollBar.horizontal: ScrollBar {
                    policy: ScrollBar.Auto
                }
            }
        }
    }
}
