import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    width: 300
    height: 35

    // Список доступных городов
    property var availableCities: ["Москва", "Можайск", "Санкт-Петербург", "Владивосток", "Владикавказ", "Казань", "Монтана"]

    TextField {
        id: cityNameTextField
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right
        width: parent.width
        height: 35
        placeholderText: "любой город"
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
            // Если поле не пустое, фильтруем список городов
            if (text !== "") {
                var suggestionsCount = 0;
                for (var i = 0; i < availableCities.length; i++) {
                    if (availableCities[i].toLowerCase().indexOf(text.toLowerCase()) !== -1) {
                        completerModel.append({ "city": availableCities[i] });
                        suggestionsCount++;
                        // Ограничиваем количество вариантов до двух
                        if (suggestionsCount >= 2) break;
                    }
                }
            }
            listView.visible = completerModel.count > 0;
        }
    }

    // Модель для подсказок
    ListModel {
        id: completerModel
    }

    ListView {
        id: listView
        anchors.top: cityNameTextField.bottom
        anchors.left: cityNameTextField.left
        anchors.right: cityNameTextField.right
        // Высота зависит от количества элементов (до двух)
        height: Math.min(completerModel.count * 40, 80)
        model: completerModel
        visible: false
        clip: true
        z: 999  // Высокий уровень, чтобы быть поверх остальных элементов

        delegate: Item {
            width: parent.width
            height: 40

            Text {
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                anchors.leftMargin: 10
                text: city
                font.pixelSize: 16
            }

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    cityNameTextField.text = city;
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
