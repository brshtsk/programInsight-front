class ClusterTemplate:
    def __init__(self, name: str, rgb_background: str, rgb_text_color: str):
        self.name = name
        self.rgb_background = rgb_background
        self.rgb_text_color = rgb_text_color


class Templates:
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
