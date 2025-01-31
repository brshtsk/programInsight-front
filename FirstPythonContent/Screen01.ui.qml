

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick
import QtQuick.Controls
//2.15
import QtQuick.Window
//2.15
import QtQuick.Layouts
//1.15
import QtQuick.Shapes
import FirstPython
import QtQuick.Studio.DesignEffects
import "components"

// Убедитесь, что путь правильный
Rectangle {
    width: 1190
    height: 810
    color: "#ffffff"

    Rectangle {
        id: backSearchZoneRectangle
        x: 250

        y: 30
        width: 480
        height: 770
        color: "#dde9db"
        radius: 10
        border.width: 0

        Rectangle {
            id: scrollRectangle
            x: 0
            y: 95
            width: parent.width
            height: 675
            visible: true
            color: "#00ffffff"
            radius: 10
            border.width: 0

            ScrollView {
                id: scrollView
                //anchors.fill: parent
                width: parent.width
                height: parent.height
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.leftMargin: 10 // Отступ слева
                anchors.rightMargin: 10 // Отступ справа
                wheelEnabled: true
                ScrollBar.vertical.policy: ScrollBar.AlwaysOff
                clip: true // Ограничение содержимого прокрутки границами ScrollView

                ListView {
                    id: listView
                    anchors.fill: parent
                    // Добавляем отступ перед первым элементом
                    header: Rectangle {
                        width: listView.width
                        height: 15
                        color: "#00ffffff"
                    }

                    // Добавляем отступ после последнего элемента
                    footer: Rectangle {
                        width: listView.width
                        height: 15
                        color: "#00ffffff"
                    }
                    spacing: 15 // Добавляем отступ между элементами
                    // model: customModel
                    // Тестовая модель
                    model: ListModel {
                        ListElement {
                            opNameText: "Программная<br>инженерия"
                            info1Text: "289"
                            info2Text: "700к ₽"
                            universityNameText: "НИУ ВШЭ"
                            opCodeText: "09.03.04"
                            imageSource: "resources/hselogo.svg"
                        }
                        ListElement {
                            opNameText: "Прикладная математика<br>и информатика"
                            info1Text: "300"
                            info2Text: "720к ₽"
                            universityNameText: "НИУ ВШЭ"
                            opCodeText: "01.03.02"
                            imageSource: "resources/hselogo.svg"
                        }
                        ListElement {
                            opNameText: "Анализ данных<br>в экономике"
                            info1Text: "272"
                            info2Text: "470к ₽"
                            universityNameText: "МФТИ"
                            opCodeText: "38.03.01"
                            imageSource: "resources/mfti-logo.png"
                        }
                        ListElement {
                            opNameText: "Физика<br>и нанотехнологии"
                            info1Text: "280"
                            info2Text: "500к ₽"
                            universityNameText: "МФТИ"
                            opCodeText: "16.03.01"
                            imageSource: "resources/mfti-logo.png"
                        }
                        ListElement {
                            opNameText: "Информационная<br>безопасность"
                            info1Text: "260"
                            info2Text: "450к ₽"
                            universityNameText: "МИРЭА"
                            opCodeText: "10.03.01"
                            imageSource: "resources/other-logo.svg"
                        }
                    }
                    delegate: Rectangle {
                        id: opRowRectangle
                        width: 420
                        height: 150
                        color: "#53b93f"
                        radius: 10
                        anchors.horizontalCenter: parent.horizontalCenter // Центрируем

                        Image {
                            id: universityImage
                            x: 15
                            y: 80
                            width: 50
                            height: 50
                            source: model.imageSource
                            fillMode: Image.PreserveAspectFit
                        }

                        Text {
                            id: opNameText
                            x: 15
                            y: 15
                            width: parent.width - 30
                            height: 65
                            color: "#ffffff"
                            text: model.opNameText
                            font.pixelSize: 24
                            textFormat: Text.RichText
                            font.family: "Bahnschrift SemiBold"
                        }

                        Text {
                            id: universityNameText
                            x: 75
                            y: 80
                            width: 120
                            height: 23
                            color: "#ffffff"
                            text: model.universityNameText
                            font.pixelSize: 15
                            horizontalAlignment: Text.AlignLeft
                            verticalAlignment: Text.AlignBottom
                            textFormat: Text.RichText
                            font.family: "Bahnschrift SemiBold"
                        }

                        Text {
                            id: opCodeText
                            x: 75
                            y: 107
                            width: 120
                            height: 23
                            color: "#ffffff"
                            text: model.opCodeText
                            font.pixelSize: 15
                            horizontalAlignment: Text.AlignLeft
                            verticalAlignment: Text.AlignTop
                            textFormat: Text.RichText
                            font.family: "Bahnschrift SemiBold"
                        }

                        Rectangle {
                            id: info1Rectangle
                            x: 251
                            y: 80
                            width: 72
                            height: 40
                            color: "#ffffff"
                            radius: 10

                            Text {
                                id: info1Text
                                font.pixelSize: 20
                                horizontalAlignment: Text.AlignHCenter
                                verticalAlignment: Text.AlignVCenter
                                font.family: "Bahnschrift SemiBold"
                                width: parent.width
                                height: parent.height
                                color: "#53b93f"
                                anchors.left: parent.left
                                anchors.right: parent.right
                                anchors.leftMargin: 10 // Отступ слева
                                anchors.rightMargin: 10 // Отступ справа
                                text: model.info1Text
                            }
                        }

                        Rectangle {
                            id: info2Rectangle
                            x: 333
                            y: 80
                            width: 72
                            height: 40
                            color: "#ffffff"
                            radius: 10

                            Text {
                                id: info2Text
                                font.pixelSize: 20
                                horizontalAlignment: Text.AlignHCenter
                                verticalAlignment: Text.AlignVCenter
                                font.family: "Bahnschrift SemiBold"
                                width: parent.width
                                height: parent.height
                                color: "#53b93f"
                                anchors.left: parent.left
                                anchors.right: parent.right
                                anchors.leftMargin: 10 // Отступ слева
                                anchors.rightMargin: 10 // Отступ справа
                                text: model.info2Text
                            }
                        }

                        Text {
                            id: typeInfo1Text
                            x: 251
                            y: 122
                            width: 72
                            height: 16
                            color: "#ffffff"
                            text: qsTr("Баллов ЕГЭ")
                            font.pixelSize: 12
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                        }

                        Text {
                            id: typeInfo2Text
                            x: 333
                            y: 122
                            width: 72
                            height: 16
                            color: "#ffffff"
                            text: qsTr("Стоимость")
                            font.pixelSize: 12
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                        }
                    }
                }
            }
        }

        Item {
            id: upperZoneItem
            y: 10
            height: 80
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 20
            anchors.rightMargin: 20

            Button {
                id: searchSettingsButton
                objectName: "button"
                width: 48
                height: 72
                font.pixelSize: 16
                icon.color: "#ffffff"
                icon.source: "resources/icons8-настройки-48.png"
                anchors.right: parent.right
                anchors.verticalCenter: parent.verticalCenter

                background: Rectangle {
                    color: searchSettingsButton.pressed ? "#7dd96b" : "#53b93f" // Изменение цвета при нажатии
                    radius: 10
                    scale: searchSettingsButton.hovered ? 1.05 : 1.0 // Увеличение кнопки при наведении
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

            Item {
                id: _item
                width: 200
                height: 70
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter

                Text {
                    id: searchOpText
                    text: "Поиск ОП"
                    font.pixelSize: 36
                    textFormat: Text.RichText
                    font.family: "Bahnschrift SemiBold"
                    anchors.left: parent.left
                    anchors.top: parent.top
                }

                Text {
                    id: resultAmountText
                    color: "#373737"
                    text: "Получено 009 результатов"
                    anchors.left: parent.left
                    font.pixelSize: 18
                    textFormat: Text.RichText
                    font.family: "Bahnschrift Light SemiCondensed"
                    anchors.bottom: parent.bottom
                }
            }
        }
    }

    Item {
        id: rezultZoneItem
        x: 770
        y: 40
        width: 400
        height: 770

        Item {
            id: userZoneItem
            x: 0
            y: 0
            width: parent.width
            height: 80

            Button {
                id: favouriteButton
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter
                width: 40
                height: 40
                icon.height: 32
                icon.width: 32
                wheelEnabled: true
                icon.color: pressed ? "#ff8a8a" : (hovered ? "#ff0707" : "#d5d5d5") // Бледно-красный при нажатии
                icon.source: "resources/heart-gray.svg"
                background: Rectangle {
                    color: "#00FFFFFF"
                }

                // Увеличение размера иконки при наведении
                scale: hovered ? 1.05 : 1.0

                // Плавная анимация увеличения
                Behavior on scale {
                    NumberAnimation {
                        duration: 150
                        easing.type: Easing.InOutQuad
                    }
                }

                Behavior on icon.color {
                    ColorAnimation {
                        duration: 200
                    }
                }
            }

            Item {
                id: userAccountItem
                width: 165
                height: parent.height
                anchors.right: parent.right
                anchors.verticalCenter: parent.verticalCenter

                Button {
                    id: userCabinetButton
                    x: 152
                    y: 349
                    width: 40
                    height: 40
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.right: parent.right
                    font.pixelSize: 16
                    objectName: "button"
                    icon.source: "resources/user-icon.svg"
                    icon.color: "#ffffff"
                    background: Rectangle {
                        color: userCabinetButton.pressed ? "#e5e5e5" : "#d5d5d5"
                        radius: 10
                        scale: userCabinetButton.hovered ? 1.05 : 1.0
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
                Text {
                    id: userNameText
                    width: 120
                    height: 48
                    color: "#696969"
                    text: "Митя<br>Бершицкий"
                    anchors.left: parent.left
                    font.pixelSize: 18
                    horizontalAlignment: Text.AlignLeft
                    verticalAlignment: Text.AlignBottom
                    textFormat: Text.RichText
                    font.family: "Bahnschrift Light"
                    anchors.verticalCenter: parent.verticalCenter
                }
            }
        }

        Item {
            id: statisticsZoneItem
            x: 0
            y: 90
            width: parent.width
            height: 200

            Text {
                id: statisticHeaderText
                color: "#373737"
                text: "Статистика по результатам"
                anchors.left: parent.left
                font.pixelSize: 18
                textFormat: Text.RichText
                font.family: "Bahnschrift Light SemiCondensed"
                anchors.top: parent.top
            }
            ListView {
                id: statisticListView
                width: parent.width
                height: 80
                anchors.bottom: parent.bottom
                model: ListModel {
                    ListElement {
                        name: "Red"
                        colorCode: "red"
                    }

                    ListElement {
                        name: "Green"
                        colorCode: "green"
                    }

                    ListElement {
                        name: "Blue"
                        colorCode: "blue"
                    }

                    ListElement {
                        name: "White"
                        colorCode: "white"
                    }
                }
                delegate: Row {
                    spacing: 5
                    Rectangle {
                        width: 100
                        height: 20
                        color: colorCode
                    }

                    Text {
                        width: 100
                        text: name
                    }
                }
            }

            Item {
                id: statisticRowItem
                x: 0
                y: 40
                width: parent.width
                height: 60

                Rectangle {
                    id: statisticTypeRectangle
                    color: "#00d5d5d5"
                    width: 48
                    height: 48
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.left: parent.left
                    radius: 10
                    border.color: "#d5d5d5"
                    border.width: 2

                    Image {
                        id: statisticTypeImage
                        width: 36
                        height: 36
                        source: "resources/exam.svg"
                        fillMode: Image.PreserveAspectFit
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.horizontalCenter: parent.horizontalCenter
                    }
                }

                Text {
                    id: statisticTypeText
                    x: 58
                    width: 220
                    height: 35
                    color: "#000000"
                    text: "Средний балл ЕГЭ"
                    font.pixelSize: 24
                    horizontalAlignment: Text.AlignLeft
                    verticalAlignment: Text.AlignBottom
                    textFormat: Text.RichText
                    font.family: "Bahnschrift SemiBold"
                    anchors.verticalCenter: parent.verticalCenter
                }

                CircularProgressBar {
                    id: progressBar
                    width: 40
                    height: 40
                    progress: 0.75 // Установите значение прогресса
                    progressColor: "#53b93f"
                    backgroundColor: "#d0d0d0"
                    strokeWidth: 4
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.right: parent.right
                }
            }
        }
    }
}
