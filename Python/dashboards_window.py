from PySide6.QtCore import QObject, Slot
from PySide6.QtQml import QQmlComponent
from utils import Utils
from plots.graph_builder import GraphBuilder
import os
from time import time


class DashboardsWindow(QObject):
    def __init__(self, engine, frontend_parent):
        super().__init__()
        self.engine = engine
        self.frontend_parent = frontend_parent
        self.component = None
        self.window = None

        self.load_window()

        self.frontend_parent.mainWindowClosed.connect(self.on_main_window_closed)
        self.frontend_parent.modelChanged.connect(self.on_model_changed)

    def load_window(self):
        dashboards_qml_path = Utils.resource_path('FirstPythonContent/Dashboards.qml')
        self.component = QQmlComponent(self.engine, str(dashboards_qml_path))
        if self.component.status() == QQmlComponent.Ready:
            self.window = self.component.create()
            if self.window:
                self.window.show()
                self.set_default_properties()
                self.build_plots()
                self.window.windowClosed.connect(self.on_window_closed)
            else:
                print("Не удалось создать окно дашбордов.")
        else:
            print("Ошибка при загрузке Dashboards.qml:", self.component.errorString())

    def set_default_properties(self):
        """
        Когда открывается окно дашбордов, никакие графики не должны отображаться.
        Логика отображения графиков прописана далее.
        """
        # Нужно, чтобы при пустом списке не отображался график-заглушка

        # Обнуляем список с информацией о донате
        donut_stats_list = self.window.findChild(QObject, 'donutStatsList')
        if donut_stats_list:
            donut_stats_list.setProperty('donutStatsValues', [])
        else:
            print("Элемент с objectName 'donutStatsList' не найден")

        # Убираем donut
        stats_donut_image = self.window.findChild(QObject, 'statsDonutImage')
        if stats_donut_image:
            stats_donut_image.setProperty('source', '')
            stats_donut_image.setProperty('headerVisible', False)
        else:
            print("Элемент с objectName 'statsDonutImage' не найден")

        # Убираем график распределения цен
        price_kde_image = self.window.findChild(QObject, 'priceDistributionImage')
        if price_kde_image:
            price_kde_image.setProperty('source', '')
        else:
            print("Элемент с objectName 'priceDistributionImage' не найден")

        # Убираем график распределения проходных
        score_kde_image = self.window.findChild(QObject, 'scoreDistributionImage')
        if score_kde_image:
            score_kde_image.setProperty('source', '')
        else:
            print("Элемент с objectName 'scoreDistributionImage' не найден")

        # Убираем список частых вузов
        popular_universities_list = self.window.findChild(QObject, 'popularUniversitiesList')
        if popular_universities_list:
            popular_universities_list.setProperty('universityValues', [])
        else:
            print("Элемент с objectName 'popularUniversitiesList' не найден")

    def build_plots(self):
        """
        Создаёт графики на основе данных из op_list.
        """
        if self.window is None:
            print("Окно дашбордов закрыто, не могу обновить графики")
            return

        op_list = self.frontend_parent.filtered_op_list

        # Заголовки
        op_num_text = self.window.findChild(QObject, 'opNumText')
        if op_num_text:
            op_num_text.setProperty('text', str(len(op_list)))
        else:
            print("Элемент с objectName 'opNumText' не найден")

        op_type_text = self.window.findChild(QObject, 'opTypeText')
        if op_type_text:
            op_type_text.setProperty('text', '<br>и '.join(self.frontend_parent.settings.qualifications))
        else:
            print("Элемент с objectName 'opTypeText' не найден")

        op_payment_text = self.window.findChild(QObject, 'opPaymentText')
        if op_payment_text:
            op_payment_text.setProperty('text',
                                        'Бюджет' if self.frontend_parent.settings.show_op_only_with_budget else 'Платное')
        else:
            print("Элемент с objectName 'opPaymentText' не найден")

        percentage_value_text = self.window.findChild(QObject, 'percentageValueText')
        if percentage_value_text:
            percentage_value_text.setProperty('text',
                                              str(round(len(op_list) /
                                                        len(self.frontend_parent.op_list) * 100, 1)).replace('.',
                                                                                                             ',') + '%')
        else:
            print("Элемент с objectName 'percentageValueText' не найден")

        # Показываем список частых вузов
        try:
            # Находим список ВУЗов
            popular_universities_list = self.window.findChild(QObject, 'popularUniversitiesList')
            if popular_universities_list:
                # Получаем данные для списка
                popular_universities_list.setProperty('universityValues',
                                                      self.frontend_parent.statistics.top_3_universities_to_model_dict())
            else:
                print("Элемент с objectName 'popularUniversitiesList' не найден")
        except Exception as e:
            print("Список не изменен. Ошибка при получении данных для списка ВУЗов:", e)

        df = self.frontend_parent.df

        # График donut
        try:
            # Сохраним donut_chart
            output_path = Utils.resource_path('FirstPythonContent/plots_images/donut_chart.png')
            os.makedirs(output_path.parent, exist_ok=True)
            fig, list_stats_data = GraphBuilder.donut_chart(df)
            fig.savefig(output_path, bbox_inches='tight')
            self.update_donut(list_stats_data)
        except Exception as e:
            print("Ошибка, donut не изменён", e)
            # Убираем donut, показываем текст об ошибке
            stats_donut_image = self.window.findChild(QObject, 'statsDonutImage')
            if stats_donut_image:
                stats_donut_image.setProperty('source', '')
                stats_donut_image.setProperty('headerVisible', True)
                stats_donut_image.setProperty('headerText',
                                              'Ошибка при построении графика<br>ОП по вашим настройкам не найдены')
            else:
                print("Элемент с objectName 'statsDonutImage' не найден")
            # Очищаем список с информацией о донате
            donut_stats_list = self.window.findChild(QObject, 'donutStatsList')
            if donut_stats_list:
                donut_stats_list.setProperty('donutStatsValues', [])
            else:
                print("Элемент с objectName 'donutStatsList' не найден")

        # График распределения цен
        try:
            output_path = Utils.resource_path('FirstPythonContent/plots_images/price_kde.png')
            os.makedirs(output_path.parent, exist_ok=True)
            fig = GraphBuilder.price_kde(df)
            fig.savefig(output_path, bbox_inches='tight')
            self.update_price_kde()
        except Exception as e:
            print("Ошибка, bar не изменён:", e)
            # Убираем график, показываем текст об ошибке
            price_kde_image = self.window.findChild(QObject, 'priceDistributionImage')
            if price_kde_image:
                price_kde_image.setProperty('source', '')
                price_kde_image.setProperty('headerVisible', True)
                price_kde_image.setProperty('headerText',
                                            'Не удалось построить график плотности<br>Возможно, выбрано слишком мало ОП')
            else:
                print("Элемент с objectName 'priceDistributionImage' не найден")

        # График распределения проходных баллов
        try:
            output_path = Utils.resource_path('FirstPythonContent/plots_images/score_kde.png')
            os.makedirs(output_path.parent, exist_ok=True)
            fig = GraphBuilder.points_kde(df)
            fig.savefig(output_path, bbox_inches='tight')
            self.update_score_kde()
        except Exception as e:
            print("Ошибка, bar не изменён:", e)
            # Убираем график, показываем текст об ошибке
            score_kde_image = self.window.findChild(QObject, 'scoreDistributionImage')
            if score_kde_image:
                score_kde_image.setProperty('source', '')
                score_kde_image.setProperty('headerVisible', True)
                score_kde_image.setProperty('headerText',
                                            'Не удалось построить график плотности<br>Возможно, выбрано слишком мало ОП')
            else:
                print("Элемент с objectName 'scoreDistributionImage' не найден")

    def update_donut(self, list_stats_data):
        donut_stats_list = self.window.findChild(QObject, 'donutStatsList')
        if donut_stats_list:
            donut_stats_list.setProperty('donutStatsValues', list_stats_data)
        else:
            print("Элемент с objectName 'donutStatsList' не найден")

        stats_donut_image = self.window.findChild(QObject, 'statsDonutImage')
        if stats_donut_image:
            stats_donut_image.setProperty('source', f'plots_images/donut_chart.png?cacheBust={time()}')
            stats_donut_image.setProperty('headerText', 'Статистика ОП')
            stats_donut_image.setProperty('headerVisible', True)
        else:
            print("Элемент с objectName 'statsDonutImage' не найден")

    def update_price_kde(self):
        price_kde_image = self.window.findChild(QObject, 'priceDistributionImage')
        if price_kde_image:
            price_kde_image.setProperty('source', f'plots_images/price_kde.png?cacheBust={time()}')
            price_kde_image.setProperty('headerVisible', False)
        else:
            print("Элемент с objectName 'priceKdeImage' не найден")

    def update_score_kde(self):
        score_kde_image = self.window.findChild(QObject, 'scoreDistributionImage')
        if score_kde_image:
            score_kde_image.setProperty('source', f'plots_images/score_kde.png?cacheBust={time()}')
            score_kde_image.setProperty('headerVisible', False)
        else:
            print("Элемент с objectName 'scoreDistributionImage' не найден")

    @Slot()
    def on_model_changed(self):
        """
        Слот, вызываемый при изменении модели.
        Обновляет графики на основе новых данных.
        """
        print("Модель обновлена, обновляем графики")
        self.build_plots()

    @Slot()
    def on_window_closed(self):
        """Слот, вызываемый при закрытии окна, чтобы очистить ссылку."""
        print("Окно Dashboards закрыто (либо пользователем, либо программно)")
        self.window = None

    @Slot()
    def on_main_window_closed(self):
        print("Главное окно закрыто, закрываем окно дашбордов")
        if self.window is not None:
            self.window.close()
            # self.on_window_closed() - выполняется автоматически
