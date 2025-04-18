import QtQuick
import QtQuick.Controls
import FirstPython

Item {
    id: singleExamsList
    width: 300
    height: userExamListView.height

    // property var exams: [
    //     {
    //         examNameText: "Математика (профиль)",
    //         examTypeText: "ЕГЭ",
    //         scoreText: "82",
    //         parent: "settings"
    //     },
    //     {
    //         examNameText: "Русский язык",
    //         examTypeText: "ЕГЭ",
    //         scoreText: "97",
    //         parent: "settings"
    //     },
    //     {
    //         examNameText: "Иностранный",
    //         examTypeText: "ЕГЭ",
    //         scoreText: "88",
    //         parent: "settings"
    //     },
    // ]

    property var exams

    ListView {
        id: userExamListView
        objectName: "userExamListView"
        anchors.horizontalCenter: parent.horizontalCenter
        y: 0
        width: 300
        height: contentHeight
        spacing: 5
        clip: true

        // Добавляем отступ перед первым элементом
        header: Rectangle {
            width: listView.width
            height: 10
            color: "#00ffffff"
        }

        // Добавляем отступ после последнего элемента
        footer: Rectangle {
            width: listView.width
            height: 15
            color: "#00ffffff"
        }

        model: singleExamsList.exams
        delegate: UserExamsListViewCard {

        }
    }
}
