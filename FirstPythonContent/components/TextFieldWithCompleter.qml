import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    width: 300
    height: 35

    property var availableValues: []
    property string placeholder: "введите текст"

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
            completerModel.clear();
            if (text !== "") {
                var suggestionsCount = 0;
                for (var i = 0; i < availableValues.length; i++) {
                    if (availableValues[i].toLowerCase().indexOf(text.toLowerCase()) !== -1) {
                        completerModel.append({ "value": availableValues[i] });
                        suggestionsCount++;
                        if (suggestionsCount >= 2) break;
                    }
                }
            }
            listView.visible = completerModel.count > 0;
        }

        // Скрываем completer при потере фокуса
        onFocusChanged: {
            if (!focus) {
                listView.visible = false;
            }
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
        height: Math.min(completerModel.count * 40, 80)
        model: completerModel
        visible: false
        clip: true
        z: 999

        delegate: Item {
            width: parent.width
            height: 40

            Text {
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                anchors.leftMargin: 10
                text: value
                font.pixelSize: 16
            }

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    inputTextField.text = value;
                    listView.visible = false;
                }
                hoverEnabled: true
                Rectangle {
                    anchors.fill: parent
                    color: mouseArea.containsMouse ? "#e0e0e0" : "transparent"
                    z: -1
                    id: mouseArea
                }
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
