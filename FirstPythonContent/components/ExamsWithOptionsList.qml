import QtQuick 2.15
import QtQuick.Controls 2.15

// Если ChoiceExamCard.ui.qml лежит в той же директории,
// QML автоматически распознает его как компонент с именем ChoiceExamCard.
Item {
    id: examsWithOptionsList
    width: 300
    height: 400

    // Свойство для вариантов экзаменов; сюда будет передаваться model.options из Python.
    property var examOptions: model.options

    ListView {
        id: optionsListView
        anchors.fill: parent
        // Используем свойство examOptions как модель
        model: examsWithOptionsList.examOptions
        delegate: ChoiceExamCard { }
    }
}
