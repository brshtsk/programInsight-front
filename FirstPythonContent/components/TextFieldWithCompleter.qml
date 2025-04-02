// C:/Users/kitki/QtProjects/FirstPython/FirstPythonContent/components/TextFieldWithCompleter.qml
import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    id: rootItem
    width: 300
    height: 35

    property var availableValues: []
    property string placeholder: "введите текст"
    property int maxCompitionsAmount: 2
    property bool disableCompleterNow: false

    // Экспорт свойства текста
    property alias text: inputTextField.text

    // Переименованный сигнал для удобного подключения в Python
    signal userTextChanged(string newText)

    TextField {
        id: inputTextField
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right
        width: parent.width
        height: 35
        placeholderText: placeholder
        font.pixelSize: 16
        selectionColor: "#53b93f"
        topPadding: 5
        verticalAlignment: Text.AlignVCenter

        background: Rectangle {
            anchors.fill: parent
            color: "#ffffff"
            radius: 5
            border.color: "#53b93f"
            border.width: 2
        }

        onTextChanged: {
            // Вызываем пользовательский сигнал вместо стандартного textChanged
            rootItem.userTextChanged(text)
            completerModel.clear();
            if (text !== "") {
                var suggestionsCount = 0;
                for (var i = 0; i < availableValues.length; i++) {
                    if (availableValues[i].toLowerCase().indexOf(text.toLowerCase()) !== -1) {
                        completerModel.append({ "value": availableValues[i] });
                        suggestionsCount++;
                        if (suggestionsCount >= maxCompitionsAmount)
                            break;
                    }
                }
            }
            listView.visible = completerModel.count > 0;

            if (disableCompleterNow) {
                listView.visible = false
                disableCompleterNow = false
            }
        }

        onFocusChanged: {
            if (!focus)
                listView.visible = false;
        }
    }

    ListModel {
        id: completerModel
    }

    ListView {
        id: listView
        anchors.top: inputTextField.bottom
        anchors.left: inputTextField.left
        anchors.right: inputTextField.right
        height: Math.min(completerModel.count * 30, maxCompitionsAmount * 30)
        model: completerModel
        visible: false
        clip: true
        z: 999

        delegate: Item {
            width: parent.width
            height: 30

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    inputTextField.text = value;
                    listView.visible = false;
                }
                hoverEnabled: true
                Rectangle {
                    anchors.fill: parent
                    color: mouseArea.containsMouse ? "#ffffff" : "#ffffff"
                    z: -1
                    id: mouseArea
                }
            }

            Text {
                color: inputTextField.color
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                anchors.leftMargin: 10
                text: value
                font.pixelSize: 16
            }
        }

        Rectangle {
            anchors.fill: parent
            color: "transparent"
            border.color: "#53b93f"
            border.width: 1
        }
    }
}
