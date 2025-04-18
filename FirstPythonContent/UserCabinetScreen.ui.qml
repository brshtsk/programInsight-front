import QtQuick
import QtQuick.Controls
import FirstPython
import "components"

Rectangle {
    width: 340
    height: 510
    color: "#ffffff"

    Item {
        id: upperLogoItem
        anchors.right: parent.right
        anchors.rightMargin: 20
        anchors.verticalCenter: headerText.verticalCenter
        width: 160
        height: 60

        Text {
            id: projectNameText
            x: 0
            y: 0
            color: "#53b93f"
            text: "ProgramInsight"
            anchors.right: parent.right
            anchors.verticalCenter: parent.verticalCenter
            font.pixelSize: 16
            textFormat: Text.RichText
            font.family: Constants.font.family
            font.styleName: "SemiBold"
        }

        Image {
            id: image
            width: 35
            height: 35
            anchors.left: parent.left
            anchors.verticalCenter: parent.verticalCenter
            source: "resources/near-logo.svg"
            fillMode: Image.PreserveAspectFit
        }
    }

    Text {
        id: headerText
        y: 15
        text: "Личный<br>кабинет"
        font.pixelSize: 24
        textFormat: Text.RichText
        font.family: Constants.font.family
        font.styleName: "SemiBold"
        anchors.left: parent.left
        anchors.leftMargin: 30
    }

    Rectangle {
        id: userExamsHeaderRectangle
        x: 20
        y: 80
        width: 300
        height: 50
        color: "#53b93f"
        radius: 10

        Text {
            id: userExamsHeader
            x: 20
            anchors.verticalCenter: parent.verticalCenter
            text: "Сохранение предметов"
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
                text: "Подсказка:<br><br>Укажите в этом разделе предметы, которые вы собираетесь сдавать для поступления.<br>Вы можете сохранить свои предметы, чтобы в дальнейшем быстро загружать их в настройках поиска."
                visible: helpMouseArea.containsMouse
            }
        }
    }

    Rectangle {
        id: userExamsInteractionRectangle
        x: 20
        y: 140
        width: 300
        height: 350
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
                id: saveProfileExamsButton
                objectName: "saveProfileExamsButton"
                x: 0
                anchors.verticalCenter: parent.verticalCenter
                width: 150
                height: 30

                font.pixelSize: 18
                font.family: Constants.font.family
                font.styleName: "SemiBold"

                contentItem: Text {
                    scale: saveProfileExamsButton.hovered ? 1.05 : 1.0
                    font: saveProfileExamsButton.font
                    color: "#FFFFFF"
                    text: "Сохранить" // Белый цвет текста
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    Behavior on scale {
                        NumberAnimation {
                            duration: 100
                        }
                    }
                }

                background: Rectangle {
                    color: saveProfileExamsButton.pressed ? "#7dd96b" : "#53b93f"
                    radius: 10
                    scale: saveProfileExamsButton.hovered ? 1.05 : 1.0
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

        ScrollView {
            anchors.top: userExamsSettingsItem.bottom
            anchors.bottom: parent.bottom
            width: 300
            anchors.horizontalCenter: parent.horizontalCenter
            contentHeight: chosenUserExamsList.height
            clip: true

            UserExamsList {
                id: chosenUserExamsList
                objectName: "chosenUserExamsList"

                anchors.horizontalCenter: parent.horizontalCenter
                exams: [{
                        "examNameText": "Математика (профиль)",
                        "examTypeText": "ЕГЭ/ДВИ",
                        "scoreText": "82",
                        "parent": "cabinet"
                    }, {
                        "examNameText": "Русский язык",
                        "examTypeText": "ЕГЭ/ДВИ",
                        "scoreText": "97",
                        "parent": "cabinet"
                    }, {
                        "examNameText": "Личные достижения",
                        "examTypeText": "Доп баллы ЕГЭ",
                        "scoreText": "10",
                        "parent": "cabinet"
                    }, {
                        "examNameText": "Физика",
                        "examTypeText": "ЕГЭ/ДВИ",
                        "scoreText": "100",
                        "parent": "cabinet"
                    }]
            }
        }
    }
}
