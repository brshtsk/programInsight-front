import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    id: examsWithOptionsList
    width: 300
    height: optionsListView.height

    // // Тестовые данные, чтобы сразу проверить отображение
    // property var examOptions: [
    //     {
    //         header: "Выбор из 2 предметов",
    //         options: [
    //             { optionNameText: "Физика" },
    //             { optionNameText: "Информатика" }
    //         ]
    //     },
    //     {
    //         header: "Выбор из 3 предметов",
    //         options: [
    //             { optionNameText: "География" },
    //             { optionNameText: "История" },
    //             { optionNameText: "Химия" }
    //         ]
    //     }
    // ]

    property var examOptions

    ListView {
        id: optionsListView
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

        footer: Rectangle {
            width: listView.width
            height: 10
            color: "#00ffffff"
        }

        // Модель – массив групп экзаменов
        model: examsWithOptionsList.examOptions

        // В делегате создаём экземпляр ChoiceExamCard и явно передаём данные
        delegate: ChoiceExamCard {
            examData: modelData
            // Если нужно, можно передавать и отдельные поля, например:
            // examHeader: model.header
            // examOptions: model.options
        }
    }
}
