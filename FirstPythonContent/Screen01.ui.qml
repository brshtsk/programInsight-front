

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
import QtQuick.Studio.Application

Rectangle {
    id: mainWindowContent
    width: 1200
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
                // ScrollBar.vertical.policy: ScrollBar.AlwaysOff
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
                    model: opModel

                    // // Тестовая модель
                    // model: ListModel {
                    //     ListElement {
                    //         opNameText: "Программная<br>инженерия"
                    //         info1Text: "289"
                    //         info2Text: "700к ₽"
                    //         universityNameText: "НИУ ВШЭ"
                    //         opCodeText: "09.03.04"
                    //         imageSource: "resources/hselogo.svg"
                    //     }
                    //     ListElement {
                    //         opNameText: "Прикладная математика<br>и информатика"
                    //         info1Text: "300"
                    //         info2Text: "720к ₽"
                    //         universityNameText: "НИУ ВШЭ"
                    //         opCodeText: "01.03.02"
                    //         imageSource: "resources/hselogo.svg"
                    //     }
                    //     ListElement {
                    //         opNameText: "Анализ данных<br>в экономике"
                    //         info1Text: "272"
                    //         info2Text: "470к ₽"
                    //         universityNameText: "МФТИ"
                    //         opCodeText: "38.03.01"
                    //         imageSource: "resources/mfti-logo.png"
                    //     }
                    //     ListElement {
                    //         opNameText: "Физика<br>и нанотехнологии"
                    //         info1Text: "280"
                    //         info2Text: "500к ₽"
                    //         universityNameText: "МФТИ"
                    //         opCodeText: "16.03.01"
                    //         imageSource: "resources/mfti-logo.png"
                    //     }
                    //     ListElement {
                    //         opNameText: "Информационная<br>безопасность"
                    //         info1Text: "260"
                    //         info2Text: "450к ₽"
                    //         universityNameText: "МИРЭА"
                    //         opCodeText: "10.03.01"
                    //         imageSource: "resources/other-logo.svg"
                    //     }
                    // }

                    // delegate: Rectangle {
                    //     id: opRowRectangle
                    //     width: 420
                    //     height: 140
                    //     color: "#53b93f"
                    //     radius: 10
                    //     anchors.horizontalCenter: parent.horizontalCenter // Центрируем

                    //     Image {
                    //         id: universityImage
                    //         x: 15
                    //         y: 70
                    //         width: 50
                    //         height: 50
                    //         source: model.imageSource
                    //         fillMode: Image.PreserveAspectFit
                    //     }

                    //     Text {
                    //         id: opNameText
                    //         x: 15
                    //         y: 15
                    //         width: parent.width - 30
                    //         height: 55
                    //         color: "#ffffff"
                    //         text: model.opNameText
                    //         font.pixelSize: 20
                    //         textFormat: Text.RichText
                    //         font.family: Constants.font.family
                    //         font.styleName: "SemiBold"
                    //     }

                    //     Text {
                    //         id: universityNameText
                    //         x: 75
                    //         y: 70
                    //         width: 120
                    //         height: 23
                    //         color: "#ffffff"
                    //         text: model.universityNameText
                    //         font.pixelSize: 15
                    //         horizontalAlignment: Text.AlignLeft
                    //         verticalAlignment: Text.AlignBottom
                    //         textFormat: Text.RichText
                    //         font.family: Constants.font.family
                    //         font.styleName: "SemiBold"
                    //     }

                    //     Text {
                    //         id: opCodeText
                    //         x: 75
                    //         y: 97
                    //         width: 120
                    //         height: 23
                    //         color: "#ffffff"
                    //         text: model.opCodeText
                    //         font.pixelSize: 15
                    //         horizontalAlignment: Text.AlignLeft
                    //         verticalAlignment: Text.AlignTop
                    //         textFormat: Text.RichText
                    //         font.family: Constants.font.family
                    //         font.styleName: "SemiBold"
                    //     }

                    //     Rectangle {
                    //         id: info1Rectangle
                    //         x: 251
                    //         y: 70
                    //         width: 72
                    //         height: 40
                    //         color: "#ffffff"
                    //         radius: 10

                    //         Text {
                    //             id: info1Text
                    //             font.pixelSize: 20
                    //             horizontalAlignment: Text.AlignHCenter
                    //             verticalAlignment: Text.AlignVCenter
                    //             font.family: Constants.font.family
                    //             font.styleName: "SemiBold"
                    //             width: parent.width
                    //             height: parent.height
                    //             color: "#53b93f"
                    //             anchors.left: parent.left
                    //             anchors.right: parent.right
                    //             anchors.leftMargin: 10 // Отступ слева
                    //             anchors.rightMargin: 10 // Отступ справа
                    //             text: model.info1Text
                    //         }
                    //     }

                    //     Rectangle {
                    //         id: info2Rectangle
                    //         x: 333
                    //         y: 70
                    //         width: 72
                    //         height: 40
                    //         color: "#ffffff"
                    //         radius: 10

                    //         Text {
                    //             id: info2Text
                    //             font.pixelSize: 20
                    //             horizontalAlignment: Text.AlignHCenter
                    //             verticalAlignment: Text.AlignVCenter
                    //             font.family: Constants.font.family
                    //             font.styleName: "SemiBold"
                    //             width: parent.width
                    //             height: parent.height
                    //             color: "#53b93f"
                    //             anchors.left: parent.left
                    //             anchors.right: parent.right
                    //             anchors.leftMargin: 10 // Отступ слева
                    //             anchors.rightMargin: 10 // Отступ справа
                    //             text: model.info2Text
                    //         }
                    //     }

                    //     Text {
                    //         id: typeInfo1Text
                    //         x: 251
                    //         y: 112
                    //         width: 72
                    //         height: 16
                    //         color: "#ffffff"
                    //         text: qsTr("Баллов ЕГЭ")
                    //         font.pixelSize: 12
                    //         horizontalAlignment: Text.AlignHCenter
                    //         verticalAlignment: Text.AlignVCenter
                    //         font.family: Constants.font.family
                    //     }

                    //     Text {
                    //         id: typeInfo2Text
                    //         x: 333
                    //         y: 112
                    //         width: 72
                    //         height: 16
                    //         color: "#ffffff"
                    //         text: qsTr("Стоимость")
                    //         font.pixelSize: 12
                    //         horizontalAlignment: Text.AlignHCenter
                    //         verticalAlignment: Text.AlignVCenter
                    //         font.family: Constants.font.family
                    //     }

                    //     MouseArea {
                    //         id: opCardMouseArea
                    //         objectName: "opCardMouseArea"
                    //         anchors.fill: parent
                    //         cursorShape: Qt.PointingHandCursor // Изменяем курсор на "руку"
                    //         // onClicked: {
                    //         //     // Используем встроенное свойство index
                    //         //     listView.cardClicked(index, model.opNameText, model.universityNameText)
                    //         // }
                    //     }
                    // }
                    delegate: OpListViewCard {}

                    // Connections {
                    //     target: listView
                    //     onOpCardClicked: {
                    //         console.log("Клик по карточке: индекс", index,
                    //                     "ОП:", opName, "университет:",
                    //                     universityName)

                    //         // Логика обработки клика, или передача сигнала на Python
                    //         pyHandler.handleCardClicked(index, opName,
                    //                                     universityName)
                    //     }
                    // }
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
                objectName: "searchSettingsButton"
                width: 48
                height: 72
                font.pixelSize: 16
                icon.color: "#ffffff"
                anchors.right: parent.right
                anchors.verticalCenter: parent.verticalCenter

                contentItem: Image {
                    scale: searchSettingsButton.hovered ? 1.05 : 1.0
                    id: searchSettingsImage
                    source: "resources/icons8-настройки-48.png"
                    width: 35
                    height: 35
                    anchors.centerIn: parent
                    fillMode: Image.PreserveAspectFit // опционально, если нужно сохранить пропорции
                    Behavior on scale {
                        NumberAnimation {
                            duration: 100
                        }
                    }
                }

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
                id: searchInfoZoneItem
                width: 200
                height: 70
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter

                Text {
                    id: searchOpText
                    text: "Поиск ОП"
                    font.pixelSize: 36
                    textFormat: Text.RichText
                    font.family: Constants.font.family
                    font.styleName: "SemiBold"
                    anchors.left: parent.left
                    anchors.top: parent.top
                }

                Text {
                    id: resultAmountText
                    objectName: "resultAmountText"
                    color: "#373737"
                    text: "Получено 009 результатов"
                    anchors.left: parent.left
                    font.pixelSize: 18
                    textFormat: Text.RichText
                    font.family: Constants.font.family
                    font.styleName: "Condensed SemiBold"
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
        height: 750

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
                    verticalAlignment: Text.AlignVCenter
                    textFormat: Text.RichText
                    font.family: Constants.font.family
                    font.styleName: "Condensed SemiBold"
                    anchors.verticalCenter: parent.verticalCenter
                }
            }
        }

        Item {
            id: statisticsZoneItem
            x: 0
            y: 90
            width: parent.width
            height: 300

            Text {
                id: statisticHeaderText
                color: "#373737"
                text: "Статистика по результатам"
                anchors.left: parent.left
                font.pixelSize: 18
                font.styleName: "Condensed SemiBold"
                textFormat: Text.RichText
                font.family: Constants.font.family
                anchors.top: parent.top
            }
            ListView {
                id: statisticListView
                width: parent.width
                height: 270
                anchors.bottom: parent.bottom
                spacing: 10
                interactive: false

                model: statisticsModel // Используем Python-модель
                // // Ниже тестовая модель
                // model: ListModel {
                //     ListElement {
                //         statisticTypeText: "Средний балл ЕГЭ"
                //         imageSource: "resources/pencil-plain.png"
                //         statisticProgressText: "78"
                //         progress: 0.78
                //     }

                //     ListElement {
                //         statisticTypeText: "Средняя стоимоть (тыс. ₽)"
                //         imageSource: "resources/money.png"
                //         statisticProgressText: "242"
                //         progress: 1.0
                //     }

                //     ListElement {
                //         statisticTypeText: "Среднее количество мест"
                //         imageSource: "resources/people.png"
                //         statisticProgressText: "105"
                //         progress: 1.0
                //     }

                //     ListElement {
                //         statisticTypeText: "С бюджетными местами"
                //         imageSource: "resources/cap.svg"
                //         statisticProgressText: "57%"
                //         progress: 0.57
                //     }
                // }
                delegate: Item {
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
                        border.color: "#dde9db"
                        border.width: 4

                        Image {
                            id: statisticTypeImage
                            width: 30
                            height: 30
                            source: model.imageSource
                            fillMode: Image.PreserveAspectFit
                            anchors.verticalCenter: parent.verticalCenter
                            anchors.horizontalCenter: parent.horizontalCenter
                        }
                    }

                    Text {
                        id: statisticTypeText
                        x: 58
                        width: 220
                        height: 28
                        color: "#000000"
                        text: model.statisticTypeText
                        font.pixelSize: 20
                        horizontalAlignment: Text.AlignLeft
                        verticalAlignment: Text.AlignBottom
                        textFormat: Text.RichText
                        font.family: Constants.font.family
                        font.styleName: "SemiBold"
                        anchors.verticalCenter: parent.verticalCenter
                    }

                    CircularProgressBar {
                        id: statisticProgressBar
                        width: 45
                        height: 45
                        progress: model.progress
                        progressColor: "#53b93f"
                        backgroundColor: "#d0d0d0"
                        strokeWidth: 4
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.right: parent.right

                        Text {
                            id: statisticProgressText
                            font.pixelSize: 16
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            font.family: Constants.font.family
                            font.styleName: "SemiBold"
                            width: parent.width
                            height: 20
                            anchors.verticalCenter: parent.verticalCenter
                            color: "#53b93f"
                            anchors.left: parent.left
                            anchors.right: parent.right
                            anchors.leftMargin: 10 // Отступ слева
                            anchors.rightMargin: 10 // Отступ справа
                            text: model.statisticProgressText
                        }
                    }
                }
            }
        }

        Image {
            id: scorePriceImage
            objectName: "scorePriceImage"
            anchors.horizontalCenter: parent.horizontalCenter
            y: 410
            height: 290
            source: "resources/example-plot.png"
            fillMode: Image.PreserveAspectFit

            property alias headerVisible: scorePriceText.visible
            property alias headerText: scorePriceText.text
        }

        Text {
            id: scorePriceText
            y: 550
            anchors.horizontalCenter: parent.horizontalCenter
            color: "#373737"
            text: "Статистика ОП"
            font.pixelSize: 18
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            textFormat: Text.RichText
            font.family: Constants.font.family
            font.styleName: "Condensed SemiBold"

            visible: false
        }

        Button {
            id: dashboardButton
            objectName: "dashboardButton"
            x: 0
            width: parent.width
            height: 48
            text: "К дашбордам"
            anchors.bottom: parent.bottom

            font.pixelSize: 20 // Увеличенный размер шрифта
            font.family: Constants.font.family
            font.styleName: "SemiBold"

            contentItem: Text {
                scale: dashboardButton.hovered ? 1.05 : 1.0
                text: dashboardButton.text
                font: dashboardButton.font
                color: "#FFFFFF" // Белый цвет текста
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                Behavior on scale {
                    NumberAnimation {
                        duration: 100
                    }
                }
            }

            background: Rectangle {
                color: dashboardButton.pressed ? "#7dd96b" : "#53b93f"
                radius: 10
                scale: dashboardButton.hovered ? 1.05 : 1.0
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

    Item {
        id: leftMenuItem
        x: 30
        y: 40
        width: 180
        height: 750

        Item {
            id: upperLogoItem
            x: 0
            y: 0
            width: parent.width
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

        ListView {
            id: menuBarListView
            width: parent.width
            height: 200
            y: 95
            spacing: 25
            model: ListModel {

                ListElement {
                    text: "Кластеры"
                }

                ListElement {
                    text: "Экспорт"
                }

                ListElement {
                    text: "Настройки"
                }
            }
            delegate: Button {
                id: menuRowButton
                width: 120
                height: 20
                anchors.horizontalCenter: parent.horizontalCenter

                contentItem: Text {
                    font.pixelSize: 18 // Увеличенный размер шрифта
                    font.family: Constants.font.family
                    font.styleName: "SemiBold"
                    text: model.text
                    // icon.color: pressed ? "#ff8a8a" : (hovered ? "#ff0707" : "#d5d5d5") // Бледно-красный при нажатии
                    color: menuRowButton.pressed ? "#7dd96b" : (menuRowButton.hovered ? "53b93f" : "#696969")
                    horizontalAlignment: Text.AlignLeft
                    verticalAlignment: Text.AlignVCenter
                    scale: menuRowButton.hovered ? 1.05 : 1.0
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

                background: Rectangle {
                    color: "#00FFFFFF"
                }
            }
        }
    }
}
