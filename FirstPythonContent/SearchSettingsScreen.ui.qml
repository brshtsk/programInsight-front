// SettingsDialog.ui.qml
import QtQuick
import QtQuick.Controls
import QtQuick.Studio.Application
import FirstPython
import "components"

Rectangle {
    id: settingsContent
    width: 710
    height: 600
    color: "#ffffff"

    Item {
        id: upperLogoItem
        x: 210
        y: 0
        width: 180
        height: 80

        Text {
            id: projectNameText
            x: 0
            y: 0
            color: "#53b93f"
            text: "ProgramInsight"
            anchors.right: parent.right
            anchors.verticalCenter: parent.verticalCenter
            font.pixelSize: 18
            textFormat: Text.RichText
            font.family: Constants.font.family
            font.styleName: "SemiBold"
        }

        Image {
            id: image
            width: 40
            height: 40
            anchors.left: parent.left
            anchors.verticalCenter: parent.verticalCenter
            source: "resources/near-logo.svg"
            fillMode: Image.PreserveAspectFit
        }
    }

    Rectangle {
        id: typeAndScoreSettingsRectangle
        y: 80
        x: 20
        height: 160
        width: 390
        color: "#dde9db"
        radius: 10
        border.width: 0

        Item {
            id: qualificationSettingsItem
            y: 10
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            height: 40
            width: 200

            Text {
                id: qualificationTypeSettingsText
                x: 0
                height: 30
                anchors.verticalCenter: parent.verticalCenter
                text: "Квалификация"
                color: "#373737"
                font.pixelSize: 21
                verticalAlignment: Text.AlignVCenter
                textFormat: Text.RichText
                font.family: Constants.font.family
                font.styleName: "SemiBold"
                anchors.left: parent.left
            }

            ComboBox {
                id: qualificationTypeComboBox
                objectName: "qualificationTypeComboBox"
                anchors.verticalCenter: parent.verticalCenter
                height: 30
                anchors.right: parent.right
                anchors.rightMargin: 5
                width: 180

                model: ["Бакалавариат", "Специалитет", "Бакалавариат/Специалитет", "Магистратура"]

                // Кастомизация фон и текстового содержимого
                contentItem: Rectangle {
                    id: scoreComboBoxBackground
                    anchors.fill: parent
                    anchors.leftMargin: -5
                    anchors.rightMargin: -5
                    color: "#53b93f"
                    radius: 10

                    Text {
                        width: parent.width - 20
                        text: qualificationTypeComboBox.currentText
                              === "Бакалавариат/Специалитет" ? "Бак/Спец" : qualificationTypeComboBox.currentText
                        color: "#ffffff"
                        anchors.centerIn: parent
                        font.pixelSize: 18
                        font.family: Constants.font.family
                        font.styleName: "SemiBold"
                    }
                }
                // Кастомизация индикатора (стрелочки)
                indicator: Item {
                    width: 20
                    height: 20
                    anchors.right: parent.right
                    anchors.verticalCenter: parent.verticalCenter

                    Text {
                        text: "\u25BE" // Символ стрелочки вниз
                        color: "#ffffff"
                        anchors.centerIn: parent
                        font.pixelSize: 24
                    }
                }
            }
        }

        Item {
            id: applyFilterByScoreItem
            y: 60
            width: 200
            height: 40
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            Text {
                id: applyFilterByScoreText
                x: 0
                width: 330
                height: 30
                color: "#373737"
                text: "Фильтровать ОП по баллам"
                anchors.verticalCenter: parent.verticalCenter
                anchors.right: parent.right
                font.pixelSize: 21
                verticalAlignment: Text.AlignBottom
                textFormat: Text.RichText
                font.family: Constants.font.family
                font.styleName: "SemiBold"
            }

            CheckBox {
                id: applyFilterByScoreCheckBox
                objectName: "applyFilterByScoreCheckBox"
                width: 30
                height: 30
                text: ""
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left

                indicator: Rectangle {
                    id: scoreCheckBoxIndicator
                    color: "#ffffff"
                    radius: 5
                    border.color: "#53b93f"
                    border.width: 2
                    anchors.fill: parent
                    Image {
                        id: scoreCheckMark
                        width: 20
                        height: 20
                        visible: applyFilterByScoreCheckBox.checked
                        source: "resources/tick.svg"
                        anchors.centerIn: parent
                    }
                }
            }

            Rectangle {
                id: filterScoreHelpRectangle
                anchors.right: parent.right
                anchors.rightMargin: 10
                anchors.verticalCenter: parent.verticalCenter
                width: 24
                height: 36
                color: "#53b93f"
                radius: 10

                Text {
                    anchors.fill: parent
                    text: "?"
                    color: "#ffffff"
                    font.pixelSize: 21
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    textFormat: Text.RichText
                    font.family: Constants.font.family
                    font.styleName: "Bold"
                }

                MouseArea {
                    id: scoreHelpMouseArea
                    anchors.fill: parent
                    hoverEnabled: true
                }

                ToolTip {
                    text: "Подсказка:<br><br>Ниже укажите средний проходной балл по <b>одному</b> предмету."
                    visible: scoreHelpMouseArea.containsMouse
                }
            }
        }

        Item {
            id: scoreIntervalItem
            y: 110
            width: 200
            height: 40
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            Text {
                id: scoreFromText
                width: 130
                height: 30
                color: "#373737"
                text: "Проходной балл от"
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                font.pixelSize: 21
                verticalAlignment: Text.AlignBottom
                textFormat: Text.RichText
                font.family: Constants.font.family
                font.styleName: "SemiBold"
            }

            TextField {
                id: minScoreTextField
                x: 192
                objectName: "minScoreTextField"
                width: 65
                height: 35 // Увеличьте высоту
                placeholderText: "min"
                font.pixelSize: 16
                selectionColor: "#53b93f"
                anchors.verticalCenter: parent.verticalCenter

                topPadding: 5 // Поднимает текст, чтобы не обрезался
                verticalAlignment: Text.AlignVCenter

                background: Rectangle {
                    anchors.fill: parent
                    color: "#ffffff"
                    radius: 5
                    border.color: "#53b93f"
                    border.width: 2
                }
            }

            Text {
                id: scoreToText
                x: 260
                y: 5
                width: 20
                height: 30
                color: "#373737"
                text: "до"
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 21
                verticalAlignment: Text.AlignBottom
                textFormat: Text.RichText
                font.family: Constants.font.family
                font.styleName: "SemiBold"
            }

            TextField {
                id: maxScoreTextField
                x: 287
                objectName: "maxScoreTextField"
                width: 65
                height: 35 // Увеличьте высоту
                placeholderText: "max"
                font.pixelSize: 16
                selectionColor: "#53b93f"
                anchors.verticalCenter: parent.verticalCenter

                topPadding: 5 // Поднимает текст, чтобы не обрезался
                verticalAlignment: Text.AlignVCenter

                background: Rectangle {
                    anchors.fill: parent
                    color: "#ffffff"
                    radius: 5
                    border.color: "#53b93f"
                    border.width: 2
                }
            }
        }
    }

    Rectangle {
        id: paymentSettingsRectangle
        x: 20
        y: 250
        width: 390
        height: 160
        color: "#dde9db"
        radius: 10
        border.width: 0

        Item {
            id: applyFilterByPriceItem
            y: 60
            width: 200
            height: 40
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            Text {
                id: applyFilterByPriceText
                x: 0
                width: 330
                height: 30
                color: "#373737"
                text: "Фильтровать ОП по цене"
                anchors.verticalCenter: parent.verticalCenter
                anchors.right: parent.right
                font.pixelSize: 21
                verticalAlignment: Text.AlignBottom
                textFormat: Text.RichText
                font.family: Constants.font.family
                font.styleName: "SemiBold"
            }

            CheckBox {
                id: applyFilterByPriceCheckBox
                objectName: "applyFilterByPriceCheckBox"
                width: 30
                height: 30
                text: ""
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left

                // Делаем CheckBox неактивным, если выбран "Бюджет"
                enabled: paymentTypeComboBox.currentText !== "Бюджет"

                indicator: Rectangle {
                    id: checkBoxIndicator1
                    color: paymentTypeComboBox.currentText === "Бюджет" ? "#dde9db" : "#ffffff"
                    radius: 5
                    border.color: "#53b93f"
                    border.width: 2
                    anchors.fill: parent
                    Image {
                        id: checkMark1
                        width: 20
                        height: 20
                        visible: paymentTypeComboBox.currentText
                                 === "Бюджет" ? 0 : applyFilterByPriceCheckBox.checked
                        source: "resources/tick.svg"
                        anchors.centerIn: parent
                    }
                }
            }
        }

        Item {
            id: priceIntervalItem
            y: 110
            width: 200
            height: 40
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            Text {
                id: fromText
                width: 130
                height: 30
                color: "#373737"
                text: "Стоимость от"
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                font.pixelSize: 21
                verticalAlignment: Text.AlignBottom
                textFormat: Text.RichText
                font.family: Constants.font.family
                font.styleName: "SemiBold"
            }

            TextField {
                id: minPriceTextField
                x: 140
                objectName: "minPriceTextField"
                width: 65
                height: 35 // Увеличьте высоту
                placeholderText: "min"
                font.pixelSize: 16
                selectionColor: "#53b93f"
                anchors.verticalCenter: parent.verticalCenter

                topPadding: 5 // Поднимает текст, чтобы не обрезался
                verticalAlignment: Text.AlignVCenter

                background: Rectangle {
                    anchors.fill: parent
                    color: "#ffffff"
                    radius: 5
                    border.color: "#53b93f"
                    border.width: 2
                }
            }

            Text {
                id: toText
                x: 208
                y: 5
                width: 20
                height: 30
                color: "#373737"
                text: "до"
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 21
                verticalAlignment: Text.AlignBottom
                textFormat: Text.RichText
                font.family: Constants.font.family
                font.styleName: "SemiBold"
            }

            TextField {
                id: maxPriceTextField
                x: 235
                objectName: "maxPriceTextField"
                width: 65
                height: 35 // Увеличьте высоту
                placeholderText: "max"
                font.pixelSize: 16
                selectionColor: "#53b93f"
                anchors.verticalCenter: parent.verticalCenter

                topPadding: 5 // Поднимает текст, чтобы не обрезался
                verticalAlignment: Text.AlignVCenter

                background: Rectangle {
                    anchors.fill: parent
                    color: "#ffffff"
                    radius: 5
                    border.color: "#53b93f"
                    border.width: 2
                }
            }

            Text {
                id: trText
                x: 305
                y: 5
                width: 65
                height: 30
                color: "#373737"
                text: "тыс. ₽"
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 21
                verticalAlignment: Text.AlignBottom
                textFormat: Text.RichText
                font.family: Constants.font.family
                font.styleName: "SemiBold"
            }
        }

        Item {
            id: onlyWithBudgetSettingsItem
            x: 10
            y: 10
            width: 200
            height: 40
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 10
            anchors.rightMargin: 10

            Text {
                id: paymentTypeSettingsText
                x: 0
                height: 30
                anchors.verticalCenter: parent.verticalCenter
                text: "Оплата"
                color: "#373737"
                font.pixelSize: 21
                verticalAlignment: Text.AlignVCenter
                textFormat: Text.RichText
                font.family: Constants.font.family
                font.styleName: "SemiBold"
                anchors.left: parent.left
            }

            ComboBox {
                id: paymentTypeComboBox
                objectName: "paymentTypeComboBox"
                anchors.verticalCenter: parent.verticalCenter
                height: 30
                anchors.right: parent.right
                anchors.rightMargin: 5
                width: 180

                model: ["Бюджет", "Платное"]

                // Кастомизация фон и текстового содержимого
                contentItem: Rectangle {
                    id: paymentComboBoxBackground
                    anchors.fill: parent
                    anchors.leftMargin: -5
                    anchors.rightMargin: -5
                    color: "#53b93f"
                    radius: 10

                    Text {
                        width: parent.width - 20
                        text: paymentTypeComboBox.currentText
                        color: "#ffffff"
                        anchors.centerIn: parent
                        font.pixelSize: 18
                        font.family: Constants.font.family
                        font.styleName: "SemiBold"
                    }
                }
                // Кастомизация индикатора (стрелочки)
                indicator: Item {
                    width: 20
                    height: 20
                    anchors.right: parent.right
                    anchors.verticalCenter: parent.verticalCenter

                    Text {
                        text: "\u25BE" // Символ стрелочки вниз
                        color: "#ffffff"
                        anchors.centerIn: parent
                        font.pixelSize: 24
                    }
                }
            }
        }
    }

    Text {
        id: headerText
        x: 55
        y: 19
        text: "Настройки<br>поиска"
        font.pixelSize: 24
        textFormat: Text.RichText
        font.family: Constants.font.family
        font.styleName: "SemiBold"
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.leftMargin: 29
        anchors.topMargin: 11
    }

    Rectangle {
        id: rectangle
        x: 420
        y: 80
        width: 270
        height: 390
        color: "#dde9db"
        radius: 10

        Item {
            id: userExamsSettingsItem
            y: 10
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            height: 40

            Button {
                id: loadProfileExamsButton
                objectName: "loadProfileExamsButton"
                x: 0
                anchors.verticalCenter: parent.verticalCenter
                width: 150
                height: 30

                font.pixelSize: 18
                font.family: Constants.font.family
                font.styleName: "SemiBold"

                contentItem: Text {
                    scale: loadProfileExamsButton.hovered ? 1.05 : 1.0
                    font: loadProfileExamsButton.font
                    color: "#FFFFFF"
                    text: "Из профиля" // Белый цвет текста
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    Behavior on scale {
                        NumberAnimation {
                            duration: 100
                        }
                    }
                }

                background: Rectangle {
                    color: loadProfileExamsButton.pressed ? "#7dd96b" : "#53b93f"
                    radius: 10
                    scale: loadProfileExamsButton.hovered ? 1.05 : 1.0
                    Behavior on scale {
                        NumberAnimation {
                            duration: 100
                        }
                    }
                    Behavior on color {
                        ColorAnimation {
                            duration: 200
                        }
                    }
                }
            }

            Button {
                id: addExamButton
                objectName: "addExamButton"
                anchors.right: parent.right
                anchors.verticalCenter: parent.verticalCenter
                width: 45
                height: 30

                font.pixelSize: 21
                font.family: Constants.font.family
                font.styleName: "SemiBold"

                contentItem: Text {
                    scale: addExamButton.hovered ? 1.05 : 1.0
                    font: addExamButton.font
                    color: "#FFFFFF"
                    text: "+"
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    Behavior on scale {
                        NumberAnimation {
                            duration: 100
                        }
                    }
                }

                background: Rectangle {
                    color: addExamButton.pressed ? "#7dd96b" : "#53b93f"
                    radius: 10
                    scale: addExamButton.hovered ? 1.05 : 1.0
                    Behavior on scale {
                        NumberAnimation {
                            duration: 100
                        }
                    }
                    Behavior on color {
                        ColorAnimation {
                            duration: 200
                        }
                    }
                }
            }
        }
    }

    Rectangle {
        id: userExamsRectangle
        x: 420
        y: 20
        width: 270
        height: 50
        color: "#53b93f"
        radius: 10

        Text {
            id: userExamsHeader
            x: 20
            anchors.verticalCenter: parent.verticalCenter
            text: "Мои предметы"
            color: "#ffffff"
            font.pixelSize: 21
            verticalAlignment: Text.AlignVCenter
            textFormat: Text.RichText
            font.family: Constants.font.family
            font.styleName: "SemiBold"
        }

        Rectangle {
            id: userExamsHelpRectangle
            anchors.right: parent.right
            anchors.rightMargin: 10
            anchors.verticalCenter: parent.verticalCenter
            width: 24
            height: 36
            color: "#ffffff"
            radius: 10

            Text {
                anchors.fill: parent
                text: "?"
                color: "#53b93f"
                font.pixelSize: 21
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                textFormat: Text.RichText
                font.family: Constants.font.family
                font.styleName: "Bold"
            }

            MouseArea {
                id: helpMouseArea
                anchors.fill: parent
                hoverEnabled: true
            }

            ToolTip {
                text: "Подсказка:<br><br>Укажите в этом разделе предметы, которые вы собираетесь сдавать для поступления.<br>Далее вам будут показаны только подходящие ОП!<br><br>Также вы можете указать свои баллы по предметам, чтобы найти ОП, на которые у вас достаточно баллов.<br>Поля с баллами можно оставить пустыми, тогда фильтрация по баллам не применится.<br><br>Кнопка \"Из профиля\" позволяет загрузить список экзаменов, сохраненный в профиле."
                visible: helpMouseArea.containsMouse
            }
        }
    }

    Rectangle {
        id: searchByNameRectangle
        x: 20
        y: 420
        width: 390
        height: 160
        color: "#0053b93f"
        radius: 10

        Item {
            id: cityNameSettingsItem
            x: 10
            y: 10
            width: 200
            height: 40
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            Text {
                id: cityNameSettingsText
                x: 0
                height: 30
                color: "#373737"
                text: "Город обучения"
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                font.pixelSize: 21
                verticalAlignment: Text.AlignVCenter
                textFormat: Text.RichText
                font.styleName: "SemiBold"
                font.family: Constants.font.family
            }

            TextFieldWithCompleter {
                id: cityNameTextField
                anchors.verticalCenter: parent.verticalCenter
                anchors.right: parent.right
                objectName: "cityNameTextField"
                width: 200
                height: 35
                placeholder: "любой город"
                availableValues: ["Москва", "Можайск", "Санкт-Петербург", "Владивосток", "Владикавказ", "Казань"]
            }
        }

        Item {
            id: opNameSettingsItem
            x: 10
            y: 60
            width: 200
            height: 40
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            Text {
                id: opNameSettingsText
                x: 0
                height: 30
                color: "#373737"
                text: "Название ОП"
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                font.pixelSize: 21
                verticalAlignment: Text.AlignVCenter
                textFormat: Text.RichText
                font.styleName: "SemiBold"
                font.family: Constants.font.family
            }

            TextFieldWithCompleter {
                id: opNameTextField
                anchors.verticalCenter: parent.verticalCenter
                anchors.right: parent.right
                objectName: "opNameTextField"
                width: 200
                height: 35
                placeholder: "любое ОП"
                availableValues: ["Программная инженерия", "Прикладная математика", "Прикладной анализ данных", "Прикладная математика и информатика"]
            }
        }

        Item {
            id: universityNameSettingsItem
            x: 10
            y: 110
            width: 200
            height: 40
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            Text {
                id: universityNameSettingsText
                x: 0
                height: 30
                color: "#373737"
                text: "Название ВУЗа"
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                font.pixelSize: 21
                verticalAlignment: Text.AlignVCenter
                textFormat: Text.RichText
                font.styleName: "SemiBold"
                font.family: Constants.font.family
            }

            TextFieldWithCompleter {
                id: universityNameTextField
                anchors.verticalCenter: parent.verticalCenter
                anchors.right: parent.right
                objectName: "universityNameTextField"
                width: 200
                height: 35
                placeholder: "любой ВУЗ"
                availableValues: ["ВШЭ", "ИТМО", "МИФИ", "МФТИ"]
            }
        }
    }

    Rectangle {
        id: sortOpRectangle
        x: 420
        y: 480
        width: 270
        height: 100
        color: "#dde9db"
        radius: 10

        Item {
            id: upperSortOpSettingsItem
            x: 10
            y: 10
            width: 200
            height: 40
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            Text {
                id: sortOpVarSettingsText
                x: 0
                height: 30
                color: "#373737"
                text: "Сортировка ОП"
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                font.pixelSize: 21
                verticalAlignment: Text.AlignVCenter
                textFormat: Text.RichText
                font.styleName: "SemiBold"
                font.family: Constants.font.family
            }
        }

        Item {
            id: lowerSortOpSettingsItem
            x: 10
            y: 50
            width: 200
            height: 40
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 10
            anchors.rightMargin: 10

            ComboBox {
                id: sortOpVarComboBox
                width: 180
                height: 30
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                anchors.leftMargin: 5
                objectName: "sortOpVarComboBox"
                model: ["По рейтингу RAEX", "По стоимости", "По проходным"]
                indicator: Item {
                    width: 20
                    height: 20
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.right: parent.right
                    Text {
                        color: "#ffffff"
                        text: "\u25be"
                        font.pixelSize: 24
                        anchors.centerIn: parent
                    }
                }
                contentItem: Rectangle {
                    id: sortOpVarComboBoxBackground
                    color: "#53b93f"
                    radius: 10
                    anchors.fill: parent
                    anchors.leftMargin: -5
                    anchors.rightMargin: -5
                    Text {
                        width: parent.width - 20
                        color: "#ffffff"
                        text: sortOpVarComboBox.currentText
                        font.pixelSize: 18
                        font.styleName: "SemiBold"
                        font.family: Constants.font.family
                        anchors.centerIn: parent
                    }
                }
            }

            Button {
                id: sortUpDownButton
                objectName: "sortUpDownButton"
                anchors.right: parent.right
                anchors.verticalCenter: parent.verticalCenter
                width: 45
                height: 30

                font.pixelSize: 21
                font.family: Constants.font.family
                font.styleName: "SemiBold"

                contentItem: Image {
                    // Немного костыльно, так как трабл с размером png
                    scale: sortUpDownButton.hovered ? 1.47 : 1.4
                    id: sortUpDownImage
                    source: "resources/sort-from-bottom.png"
                    width: 30
                    height: 30

                    anchors.centerIn: parent
                    fillMode: Image.PreserveAspectFit
                    Behavior on scale {
                        NumberAnimation {
                            duration: 100
                        }
                    }
                }

                background: Rectangle {
                    color: sortUpDownButton.pressed ? "#7dd96b" : "#53b93f" // Изменение цвета при нажатии
                    radius: 10
                    scale: sortUpDownButton.hovered ? 1.05 : 1.0 // Увеличение кнопки при наведении
                    Behavior on scale {
                        NumberAnimation {
                            duration: 100
                        }
                    }
                    Behavior on color {
                        ColorAnimation {
                            duration: 200
                        }
                    }
                }
            }
        }
    }
}
