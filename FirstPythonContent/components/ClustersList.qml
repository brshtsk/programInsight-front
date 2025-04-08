import QtQuick
import QtQuick.Controls
import FirstPython

Item {
    id: clustersList
    width: 300
    height: clustersListView.height

    // property var clusters: [
    //     {
    //         clusterNameText: "Розовый кластер",
    //         clusterSizeText: "16",
    //         clusterCardColor: "#ff69b4",
    //         clusterNameColor: "#ffffff"
    //     },
    //     {
    //         clusterNameText: "Фиолетовый кластер",
    //         clusterSizeText: "14",
    //         clusterCardColor: "#b415ed",
    //         clusterNameColor: "#ffffff"
    //     },
    //     {
    //         clusterNameText: "Синий кластер",
    //         clusterSizeText: "21",
    //         clusterCardColor: "#1552ed",
    //         clusterNameColor: "#ffffff"
    //     },
    // ]

    property var clusters

    ListView {
        id: clustersListView
        objectName: "clustersListView"
        anchors.horizontalCenter: parent.horizontalCenter
        y: 0
        width: 300
        height: contentHeight
        spacing: 5
        clip: true

        // Добавляем отступ перед первым элементом
        header: Rectangle {
            width: listView.width
            height: 10
            color: "#00ffffff"
        }

        // Добавляем отступ после последнего элемента
        footer: Rectangle {
            width: listView.width
            height: 10
            color: "#00ffffff"
        }

        model: clustersList.clusters
        delegate: ClustersListViewCard {

        }
    }
}
