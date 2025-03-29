import QtQuick
import QtQuick.Controls
import FirstPython

Item {
    id: singleExamsList
    width: 300
    height: singleExamListView.height

    // property var exams: [
    //     { examNameText: "Математика (профиль)" },
    //     { examNameText: "Русский язык" },
    //     { examNameText: "Иностранный" },
    // ]

    property var exams

    ListView {
        id: singleExamListView
        objectName: "singleExamListView"
        anchors.horizontalCenter: parent.horizontalCenter
        y: 0
        width: 300
        height: contentHeight
        spacing: 10

        interactive: false

        // Добавляем отступ перед первым элементом
        header: Rectangle {
            width: listView.width
            height: 10
            color: "#00ffffff"
        }

        model: singleExamsList.exams
        delegate: Rectangle {
            id: examItemRecatngle
            anchors.horizontalCenter: parent.horizontalCenter
            y: 40
            width: 270
            height: 35
            color: "#53b93f"
            radius: 10

            Flickable {
                id: examNameContainerFlickable
                width: parent.width - 20
                height: examNameText.height
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
                clip: true
                contentWidth: examNameText.width
                              < width ? width : examNameText.width

                Text {
                    id: examNameText
                    height: 20
                    color: "#ffffff"
                    text: modelData.examNameText
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    font.pixelSize: 18
                    horizontalAlignment: Text.AlignLeft
                    font.styleName: "Regular"
                    font.family: Constants.font.family
                }

                ScrollBar.horizontal: ScrollBar {
                    policy: ScrollBar.Auto // или ScrollBar.Always для постоянного отображения
                }
            }
        }
    }
}
