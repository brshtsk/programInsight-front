pragma Singleton
import QtQuick
import QtQuick.Studio.Application

QtObject {
    readonly property int width: 1920
    readonly property int height: 1080

    property string relativeFontDirectory: "fonts"

    // Загружаем шрифт из каталога
    readonly property FontLoader robotoLoader: FontLoader {
        // Формируем URL относительно файла Constants.qml
        source: Qt.resolvedUrl("../FirstPythonContent/" + relativeFontDirectory + "/Roboto-VariableFont_wdth,wght.ttf")
    }

    // Можно задать шрифт по умолчанию через свойства font
    readonly property font font: Qt.font({
        family: robotoLoader.name,  // Используем имя загруженного шрифта
        pixelSize: Qt.application.font.pixelSize
    })
    readonly property font largeFont: Qt.font({
        family: robotoLoader.name,
        pixelSize: Qt.application.font.pixelSize * 1.6
    })

    readonly property color backgroundColor: "#EAEAEA"


    property StudioApplication application: StudioApplication {
        fontPath: Qt.resolvedUrl("../FirstPythonContent/" + relativeFontDirectory)
    }
}
