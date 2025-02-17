// SettingsDialog.ui.qml
import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material

Rectangle {
    id: dashboardsContent
    width: 1200
    height: 810
    color: "#ffffff"

    Rectangle {
        id: backCircleDiagramZoneRectangle
        x: 20

        y: 200
        width: 730
        height: 590
        color: "#dde9db"
        radius: 10
        border.width: 0

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
    }
}
