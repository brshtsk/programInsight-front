from typing import List, Tuple
from plots.cluster_analyzer import ClusterAnalyzer
from data_converter import DataConverter
from op import Op
from utils import Utils


class ClusterTemplate:
    def __init__(self, name: str, rgb_background: str, rgb_text_color: str):
        self.name = name
        self.rgb_background = rgb_background
        self.rgb_text_color = rgb_text_color


class Cluster:
    def __init__(self, template: ClusterTemplate, op_urls: List[str]):
        self.name = template.name
        self.rgb_background = template.rgb_background
        self.rgb_text_color = template.rgb_text_color
        if len(op_urls) == 0:
            raise ValueError("Список op_urls не должен быть пустым")
        self.op_urls = op_urls

    def to_model(self):
        model = {
            "clusterNameText": self.name,
            "clusterSizeText": str(len(self.op_urls)),
            "clusterCardColor": self.rgb_background,
            "clusterNameColor": self.rgb_text_color,
        }
        return model


class ClustersManager:
    # Шаблоны с названиями кластеров и цветами
    cluster_templates = [
        ClusterTemplate("Розовый кластер", "#ff69b4", "#ffffff"),  # 1
        ClusterTemplate("Фиолетовый кластер", "#b415ed", "#ffffff"),  # 2
        ClusterTemplate("Желтый кластер", "#e0f520", "#000000"),  # 3
        ClusterTemplate("Зеленый кластер", "#53b93f", "#ffffff"),  # 4
        ClusterTemplate("Оранжевый кластер", "#ffa500", "#000000"),  # 5
        ClusterTemplate("Голубой кластер", "#00bfff", "#ffffff"),  # 6
        ClusterTemplate("Синий кластер", "#1e90ff", "#ffffff"),  # 7
        ClusterTemplate("Бирюзовый кластер", "#40e0d0", "#000000"),  # 8
        ClusterTemplate("Серый кластер", "#808080", "#ffffff"),  # 9
        ClusterTemplate("Коричневый кластер", "#a52a2a", "#ffffff"),  # 10
        ClusterTemplate("Черный кластер", "#000000", "#ffffff"),  # 11
        ClusterTemplate("Белый кластер", "#ffffff", "#000000"),  # 12
        ClusterTemplate("Лиловый кластер", "#c8a2c8", "#000000"),  # 13
        ClusterTemplate("Мятный кластер", "#98ff98", "#000000"),  # 14
        ClusterTemplate("Малиновый кластер", "#dc143c", "#ffffff"),  # 15
    ]

    def __init__(self, op_list: List[Op], algorithm: str, vars: Tuple[str]):
        self.op_list = op_list
        self.algorithm = algorithm  # ("Автоматически"/"K-Means"/"Mean Shift"/"DBSCAN")
        self.vars = vars  # (('Проходной балл на бюджет', 'Стоимость (в год)')/...) - пара переменных,
        self.clusters = []

    def run_algorithm(self):
        """
        Запускает алгоритм кластеризации и возвращает результат.
        """
        df = DataConverter.list_op_to_dataframe(self.op_list)

        if len(df) == 0:
            raise ValueError("Нет данных для кластеризации")

        analyzer = ClusterAnalyzer(df, self.vars[0], self.vars[1])

        if self.algorithm == "Автоматически":
            n = len(df)
            if n < 100:
                self.algorithm = "K-Means"
            elif n < 500:
                self.algorithm = "Mean Shift"
            else:
                self.algorithm = "DBSCAN"

        if self.algorithm == "K-Means":
            clusters_dict = analyzer.kmeans_cluster_data()
        elif self.algorithm == "Mean Shift":
            clusters_dict = analyzer.mean_shift_cluster_data()
        else:
            clusters_dict = analyzer.dbscan_cluster_data()

        self.clusters = []

        i = 0
        for cluster in clusters_dict:
            urls = clusters_dict[cluster]
            if i < len(self.cluster_templates):
                self.clusters.append(
                    Cluster(self.cluster_templates[i], urls)
                )
            i += 1

        # График кластеров
        fig = analyzer.show_clusters()
        fig.savefig(Utils.resource_path('FirstPythonContent/plots_images/clusters_result.png'))

    def get_model(self):
        model = []
        for cluster in self.clusters:
            model.append(cluster.to_model())
        return model

    def clear(self):
        """
        Очищает список кластеров.
        """
        self.clusters = []
