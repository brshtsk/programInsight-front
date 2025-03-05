// SettingsDialog.ui.qml
import QtQuick
import QtQuick.Controls
import QtQuick.Studio.Application
import FirstPython

Rectangle {
    id: dashboardsContent
    width: 1200
    height: 810
    color: "#ffffff"

    Rectangle {
        id: rectangle
        x: 20
        y: 250
        width: 810
        height: 540
        color: "#dde9db"
        radius: 10
        border.width: 0

        Image {
            id: statisticsSircleImage
            x: 470
            y: 200
            width: 310
            height: 310
            source: "resources/circle_diagram.png"
            fillMode: Image.PreserveAspectFit
        }

        Text {
            id: statisticSircleText
            x: 566
            y: 344
            color: "#373737"
            text: "Статистика по результатам"
            font.pixelSize: 18
            textFormat: Text.RichText
            font.family: Constants.font.family
            font.styleName: "Condensed SemiBold"
        }
    }

    Text {
        id: headerText
        x: 20
        y: 20
        text: "Дашборды"
        font.pixelSize: 24
        font.family: Constants.font.family
        font.styleName: "SemiBold"
        width: 150
        height: 30
        textFormat: Text.RichText
    }
}
