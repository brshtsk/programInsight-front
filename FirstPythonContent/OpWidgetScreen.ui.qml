

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick
import QtQuick.Controls
import FirstPython
import "components"

Rectangle {
    id: opInfoContent

    width: 890
    height: 500

    Rectangle {
        id: opNameRectangle
        x: 20
        y: 20
        width: 850
        height: 80
        color: "#53b93f"
        radius: 10

        Text {
            id: opNameText
            anchors.left: parent.left
            anchors.verticalCenter: parent.verticalCenter
            anchors.leftMargin: 10
            font.styleName: "SemiBold"
            width: 500
            height: 60
            color: "#ffffff"
            text: "Прикладная математика<br>и информатика"
            font.family: Constants.font.family
            font.pixelSize: 24
        }

        Image {
            id: universityImage
            anchors.right: parent.right
            anchors.verticalCenter: parent.verticalCenter
            anchors.rightMargin: 10
            width: 60
            height: 60
            source: "resources/hselogo.svg"
            fillMode: Image.PreserveAspectFit
        }
    }

    Rectangle {
        id: opInfoRectangle
        x: 20
        y: 160
        width: 350
        height: 320
        color: "#ffffff"
        radius: 10

        Item {
            id: opTimeItem
            anchors.horizontalCenter: parent.horizontalCenter
            y: 10
            width: 330
            height: 50

            Image {
                id: timeImage
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter
                width: 30
                height: 30
                source: "resources/watch.png"
                fillMode: Image.PreserveAspectFit
            }

            Text {
                id: opTimeText
                x: 40
                anchors.verticalCenter: parent.verticalCenter
                font.family: Constants.font.family
                text: "4 года обучения"
                font.pixelSize: 18
            }
        }

        Item {
            id: universityItem
            y: 60
            width: 330
            height: 50
            anchors.horizontalCenterOffset: 0
            Image {
                id: capImage
                width: 30
                height: 30
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                source: "resources/black-cap.svg"
                fillMode: Image.PreserveAspectFit
            }

            Flickable {
                id: universityNameContainerFlickable
                x: 40
                width: 290
                height: universityNameText.height // либо задайте фиксированную высоту
                clip: true
                contentWidth: universityNameText.width

                // MouseArea, который меняет курсор при наведении
                MouseArea {
                    anchors.fill: parent
                    hoverEnabled: true
                    cursorShape: Qt.SizeHorCursor
                }

                Text {
                    id: universityNameText
                    x: 0
                    text: "Национальный исследовательский университет<br>Высшая школа экономики"
                    font.pixelSize: 18
                    font.family: Constants.font.family
                    wrapMode: Text.NoWrap // отключаем перенос строк, чтобы текст не делался многострочным
                }

                ScrollBar.horizontal: ScrollBar {
                    policy: ScrollBar.Auto // или ScrollBar.Auto для отображения по необходимости
                }
            }

            anchors.horizontalCenter: parent.horizontalCenter
        }

        Item {
            id: opLocationItem

            y: 110
            width: 330
            height: 50
            anchors.horizontalCenterOffset: 0
            Image {
                id: locationImage
                width: 30
                height: 30
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                source: "resources/location.svg"
                fillMode: Image.PreserveAspectFit
            }

            Text {
                id: opLocationText
                x: 40
                text: "Москва"
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 18
                font.family: Constants.font.family
            }
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Item {
            id: opRatingItem
            y: 210
            width: 330
            height: 50
            Image {
                id: ratingImage
                width: 30
                height: 30
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                source: "resources/leaderboard.svg"
                fillMode: Image.PreserveAspectFit
            }

            Text {
                id: opRatingText
                x: 40
                text: "ВУЗ 3-ий в RAEX"
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 18
                font.family: Constants.font.family
            }
            anchors.horizontalCenterOffset: 0
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Item {
            id: opAttendanceItem
            y: 160
            width: 330
            height: 50
            Image {
                id: attendanceImage
                width: 30
                height: 30
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                source: "resources/black-people.png"
                fillMode: Image.PreserveAspectFit
            }

            Text {
                id: opAttendanceText
                x: 40
                text: "Очное"
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 18
                font.family: Constants.font.family
            }
            anchors.horizontalCenterOffset: 0
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Item {
            id: opPriceItem
            y: 260
            width: 330
            height: 50
            Image {
                id: priceImage
                width: 30
                height: 30
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                source: "resources/black-money.png"
                fillMode: Image.PreserveAspectFit
            }

            Text {
                id: opPriceText
                x: 40
                text: "710к ₽ за год обучения"
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 18
                font.family: Constants.font.family
            }
            anchors.horizontalCenterOffset: 0
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }

    Rectangle {
        id: opScoreRectangle
        x: 380
        y: 110
        width: 240
        height: 90

        color: "#dde9db"
        radius: 10

        Item {
            id: budgetScoreItem
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 10
            anchors.rightMargin: 10

            y: 10
            height: 30

            Rectangle {
                id: budgetScoreRectangle
                x: 0
                y: 0
                width: 60
                height: 30
                color: "#ffffff"
                radius: 10

                Text {
                    id: budgetScoreText
                    x: 20
                    y: 8
                    color: "#000000"
                    text: "302"
                    anchors.verticalCenter: parent.verticalCenter
                    font.pixelSize: 21
                    font.styleName: "SemiBold"
                    font.family: Constants.font.family
                    anchors.horizontalCenter: parent.horizontalCenter
                }
            }

            Text {
                id: budgetInfoText
                x: 65
                color: "#000000"
                text: "балл на бюджет"
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 18
                font.styleName: "Regular"
                font.family: Constants.font.family
            }
        }

        Item {
            id: paidScoreItem
            y: 50
            height: 30
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            Rectangle {
                id: paidScoreRectangle
                x: 0
                y: 0
                width: 60
                height: 30
                color: "#ffffff"
                radius: 10
                Text {
                    id: paidScoreText
                    x: 20
                    y: 8
                    color: "#000000"
                    text: "281"
                    anchors.verticalCenter: parent.verticalCenter
                    font.pixelSize: 21
                    font.styleName: "SemiBold"
                    font.family: Constants.font.family
                    anchors.horizontalCenter: parent.horizontalCenter
                }
            }

            Text {
                id: paidInfoText
                x: 65
                color: "#000000"
                text: "балл на платное"
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 18
                font.styleName: "Regular"
                font.family: Constants.font.family
            }
        }
    }

    Rectangle {
        id: opTypeRectangle
        x: 20
        y: 110
        width: 350
        height: 40
        color: "#53b93f"
        radius: 10
        Text {
            id: opTypeText
            height: 20
            color: "#ffffff"
            text: "Бакалавриат"
            anchors.verticalCenter: parent.verticalCenter
            font.pixelSize: 18
            font.styleName: "SemiBold"
            font.family: Constants.font.family
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }

    Rectangle {
        id: opPlacesRectangle
        x: 630
        y: 110
        width: 240
        height: 90
        color: "#dde9db"
        radius: 10
        Item {
            id: budgetPlacesItem
            y: 10
            height: 30
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            Rectangle {
                id: budgetPlacesRectangle
                x: 0
                y: 0
                width: 60
                height: 30
                color: "#ffffff"
                radius: 10
                Text {
                    id: budgetPlacesText
                    x: 20
                    y: 8
                    color: "#000000"
                    text: "180"
                    anchors.verticalCenter: parent.verticalCenter
                    font.pixelSize: 21
                    font.styleName: "SemiBold"
                    font.family: Constants.font.family
                    anchors.horizontalCenter: parent.horizontalCenter
                }
            }

            Text {
                id: budgetPlacesInfoText
                x: 65
                color: "#000000"
                text: "бюджетных мест"
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 18
                font.styleName: "Regular"
                font.family: Constants.font.family
            }
        }

        Item {
            id: paidPlacesItem
            y: 50
            height: 30
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            Rectangle {
                id: paidPlacesRectangle
                x: 0
                y: 0
                width: 60
                height: 30
                color: "#ffffff"
                radius: 10
                Text {
                    id: paidPlacesText
                    x: 20
                    y: 8
                    color: "#000000"
                    text: "105"
                    anchors.verticalCenter: parent.verticalCenter
                    font.pixelSize: 21
                    font.styleName: "SemiBold"
                    font.family: Constants.font.family
                    anchors.horizontalCenter: parent.horizontalCenter
                }
            }

            Text {
                id: paidPlacesInfoText
                x: 65
                color: "#000000"
                text: "платных мест"
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 18
                font.styleName: "Regular"
                font.family: Constants.font.family
            }
        }
    }

    Rectangle {
        id: subjectsRectangle
        x: 380
        y: 210
        width: 490
        height: 270
        color: "#dde9db"
        radius: 10

        Text {
            id: examsText
            y: 10
            height: 20
            text: "Экзамены"
            font.pixelSize: 18
            font.styleName: "SemiBold"
            font.family: Constants.font.family
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Item {
            id: singleExamListItem
            y: 30
            width: 300
            height: singleExamListView.height
            anchors.horizontalCenter: parent.horizontalCenter

            ListView {
                id: singleExamListView
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

                model: ListModel {
                    ListElement {
                        examNameText: "Математика (профиль)"
                    }
                    ListElement {
                        examNameText: "Русский язык"
                    }
                }
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
                        contentWidth: examNameText.width < width ? width : examNameText.width

                        Text {
                            id: examNameText
                            height: 20
                            color: "#ffffff"
                            text: model.examNameText
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

        Item {
            id: choiceExamListItem
            anchors.horizontalCenter: parent.horizontalCenter
            y: 30 + singleExamListItem.height
            width: 300
            height: choiceExamListView.height

            // Создаём экземпляр ExamsWithOptionsList и передаём в него нужную модель
            ExamsWithOptionsList {
                id: choiceExamListView
                // Свойство examOptions переопределяем, передавая массив групп вариантов
                examOptions: [{
                        "header"// Здесь можно указать заголовок для группы, если он нужен
                        : "Выбор из 2 предметов",
                        "options": [{
                                "optionNameText": "Информатика"
                            }, {
                                "optionNameText": "Физика"
                            }]
                    }, {
                        "header": "Выбор из 3 предметов",
                        "options": [{
                                "optionNameText": "География"
                            }, {
                                "optionNameText": "История"
                            }, {
                                "optionNameText": "Астрономия"
                            }]
                    }]
            }
        }
    }
}
