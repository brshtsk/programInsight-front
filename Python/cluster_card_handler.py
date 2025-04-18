from utils import Utils
from PySide6.QtCore import QObject, Slot
from PySide6.QtQml import QQmlComponent
from PySide6.QtCore import QUrl
from typing import List
from clusters_manager import Cluster


class ClusterHandler(QObject):
    def __init__(self, engine, frontend_parent, clusters_window):
        super().__init__()
        self.engine = engine
        self.frontend_parent = frontend_parent
        self.components = []
        self.windows = []
        self.clusters_window = clusters_window

    @Slot(str)
    def handleCardClicked(self, cluster_name):
        print(f"Клик по кластеру: {cluster_name}")
        # Найдем кластер по имени
        cluster = next((cluster for cluster in self.clusters_window.clusters if cluster.name == cluster_name), None)
        if cluster:
            print(f"ОП в кластере {cluster_name}: {cluster.op_urls}")
            # В настройках задаем фильтр по кластеру
            self.frontend_parent.settings.filter_by_cluster = True
            self.frontend_parent.settings.cluster_urls = cluster.op_urls
            # Обновляем модель
            self.clusters_window.updateModels.emit()
        else:
            print(f"Кластер {cluster_name} не найден")
