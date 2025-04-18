from typing import List, Tuple
from plots.cluster_analyzer import ClusterAnalyzer
from data_converter import DataConverter
from op import Op
from utils import Utils
from clusters_templates import ClusterTemplate, Templates


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
    def __init__(self, op_list: List[Op], algorithm: str, vars: Tuple[str]):
        self.op_list = op_list
        self.algorithm = algorithm  # ("Автоматически"/"K-Means"/"Mean Shift"/"DBSCAN")
        self.vars = vars  # (('Проходной балл на бюджет', 'Стоимость (в год)')/...) - пара переменных,
        self.clusters = []
        self.analyzer = None

    def run_algorithm(self):
        """
        Запускает алгоритм кластеризации и возвращает результат.
        """
        df = DataConverter.list_op_to_dataframe(self.op_list)

        if len(df) == 0:
            raise ValueError("Нет данных для кластеризации")

        self.analyzer = ClusterAnalyzer(df, self.vars[0], self.vars[1])

        if self.algorithm == "Автоматически":
            n = len(df)
            if n < 100:
                self.algorithm = "K-Means"
            elif n < 500:
                self.algorithm = "Mean Shift"
            else:
                self.algorithm = "DBSCAN"

        if self.algorithm == "K-Means":
            clusters_dict = self.analyzer.kmeans_cluster_data()
        elif self.algorithm == "Mean Shift":
            clusters_dict = self.analyzer.mean_shift_cluster_data()
        else:
            clusters_dict = self.analyzer.dbscan_cluster_data()

        self.clusters = []

        other_template_urls = []

        for cluster in clusters_dict:
            urls = clusters_dict[cluster]
            try:
                template = Templates.cluster_templates[int(cluster)]
                self.clusters.append(Cluster(template, urls))
            except:
                other_template_urls += urls

        if len(other_template_urls) > 0:
            other_template = ClusterTemplate("Остальные ОП", "#373737", "#ffffff")
            self.clusters.append(Cluster(other_template, other_template_urls))

        # График кластеров
        fig = self.analyzer.show_clusters()
        fig.savefig(Utils.resource_path('FirstPythonContent/plots_images/clusters_result.png'))

    def highlight_cluster(self, cluster: Cluster):
        """
        Подсвечивает кластер на графике.
        """
        cluster_color = cluster.rgb_background
        if self.analyzer:
            fig = self.analyzer.show_clusters(cluster_color)
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
