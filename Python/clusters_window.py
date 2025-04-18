from PySide6.QtCore import QObject, Slot, Signal, QThread
from PySide6.QtQml import QQmlComponent
from utils import Utils
from clusters_manager import ClustersManager
from time import time


class ClustersWindow(QObject):
    updateModels = Signal()  # Сигнал для уведомления Frontend об изменениях

    def __init__(self, engine, frontend_parent):
        super().__init__()
        self.engine = engine
        self.frontend_parent = frontend_parent
        self.component = None
        self.window = None
        self.new_exam_window = None

        self.load_window()

        self.frontend_parent.mainWindowClosed.connect(self.on_main_window_closed)
        self.frontend_parent.modelChanged.connect(self.on_model_changed)

    def load_window(self):
        clusters_qml_path = Utils.resource_path('FirstPythonContent/Clusters.qml')
        self.component = QQmlComponent(self.engine, str(clusters_qml_path))
        if self.component.status() == QQmlComponent.Ready:
            self.window = self.component.create()
            if self.window:
                self.window.show()
                self.connect_signals()
                self.set_properties()
                self.window.windowClosed.connect(self.on_window_closed)
            else:
                print("Не удалось создать окно кластеров.")
        else:
            print("Ошибка при загрузке Clusters.qml:", self.component.errorString())

    def connect_signals(self):
        # Выбор алгоритма кластеризации
        algotirhm_type_combobox = self.window.findChild(QObject, 'algorithmTypeComboBox')
        if algotirhm_type_combobox:
            algotirhm_type_combobox.currentIndexChanged.connect(self.algorithm_type_combobox_index_changed)
            algotirhm_type_combobox.setProperty('currentIndex', 0)  # Устанавливаем индекс по умолчанию
        else:
            print("ComboBox 'algorithmTypeComboBox' не найден!")

        # Выбор пары переменных
        pair_combobox = self.window.findChild(QObject, "pairComboBox")
        if pair_combobox:
            pair_combobox.currentIndexChanged.connect(self.pair_combobox_index_changed)
        else:
            print("ComboBox 'pairComboBox' не найден!")

        # Отменить поиск по кластерам
        cancel_cluster_choice_button = self.window.findChild(QObject, 'cancelClusterChoiceButton')
        if cancel_cluster_choice_button:
            cancel_cluster_choice_button.clicked.connect(self.on_cancel_cluster_choice_button_clicked)
        else:
            print("Кнопка 'cancelClusterChoiceButton' не найдена!")

        # Запустить кластерный анализ
        run_clusters_button = self.window.findChild(QObject, 'runClustersButton')
        if run_clusters_button:
            run_clusters_button.clicked.connect(self.on_run_clusters_button_clicked)
        else:
            print("Кнопка 'runClustersButton' не найдена!")

    def set_properties(self):
        # Доступные пары переменных
        pair_combobox = self.window.findChild(QObject, "pairComboBox")
        if pair_combobox:
            if 'Магистратура' not in self.frontend_parent.settings.qualifications:
                pair_model = ["Стоимость / Проходной", "Стоимость / Проходной ₽", "Места / Проходной",
                              "Места ₽ / Проходной ₽", "Стоимость / Места ₽", "Стоимость / Рейтинг"]
            else:
                pair_model = ["Стоимость / Места ₽", "Стоимость / Рейтинг"]
            pair_combobox.setProperty('model', pair_model)
        else:
            print("ComboBox 'pairComboBox' не найден!")

        # Скрытие графика кластеров, уведомление пользователю
        clusters_image = self.window.findChild(QObject, 'clustersImage')
        if clusters_image:
            clusters_image.setProperty('visible', False)
            clusters_image.setProperty('headerVisible', True)
            clusters_image.setProperty('headerText', 'Запустите анализ, чтобы продолжить')
        else:
            print("Элемент 'clustersImage' не найден!")

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

        result_amount_text = self.window.findChild(QObject, 'resultAmountText')
        if result_amount_text:
            result_amount_text.setProperty('text', 'Получено 0 результатов')
        else:
            print("Элемент с objectName 'resultAmountText' не найден")

        clusters_list = self.window.findChild(QObject, 'clustersList')
        if clusters_list:
            clusters_list.setProperty('clusters', [])
        else:
            print("Элемент с objectName 'clustersList' не найден")

    @Slot()
    def on_model_changed(self):
        """
        Слот, вызываемый при изменении модели.
        Обновляет окно дашбордов.
        """
        print("Модель обновлена, обновляем окно кластеров")
        self.set_properties()

    @Slot()
    def algorithm_type_combobox_index_changed(self):
        # Получаем выбранный индекс
        algorithm_type_combobox = self.window.findChild(QObject, 'algorithmTypeComboBox')
        if algorithm_type_combobox:
            index = algorithm_type_combobox.property('currentIndex')
            # 0 - Автоматически, 1 - K-Means, 2 - Mean Shift, 3 - DBSCAN
            v = ["Автоматически", "K-Means", "Mean Shift", "DBSCAN"]
            print('Выбранный алгоритм кластеризации:', v[index])
        else:
            print("ComboBox 'algorithmTypeComboBox' не найден!")

    @Slot()
    def pair_combobox_index_changed(self):
        # Получаем выбранный индекс
        pair_combobox = self.window.findChild(QObject, 'pairComboBox')
        if pair_combobox:
            index = pair_combobox.property('currentIndex')
            print('Выбранный индекс пары:', index)
        else:
            print("ComboBox 'pairComboBox' не найден!")

    class ClusterThreadWorker(QObject):
        started = Signal()
        finished = Signal(list)  # вернёт модель кластеров

        def __init__(self, data, algorithm, vars):
            super().__init__()
            self.data = data
            self.algorithm = algorithm
            self.vars = vars

        @Slot()
        def run(self):
            self.started.emit()
            try:
                clusters_manager = ClustersManager(self.data, self.algorithm, self.vars)

                print()
                print('=================================')
                print('Запускаем кластерный анализ...')
                print('Алгоритм:', clusters_manager.algorithm)
                print('Пара переменных:', clusters_manager.vars)
                print('=================================')
                print()

                clusters_manager.run_algorithm()
                model = clusters_manager.get_model()
            except Exception as e:
                print("Ошибка в кластерном анализе, возможно:", e)
                model = []
            self.finished.emit(model)

    @Slot()
    def on_run_clusters_button_clicked(self):
        try:
            # Получаем выбранный индекс
            run_cluster_button = self.window.findChild(QObject, 'runClustersButton')
            if run_cluster_button:
                print("Запускаем кластерный анализ...")

                # Убираем отображение кластеров
                clusters_image = self.window.findChild(QObject, 'clustersImage')
                if clusters_image:
                    clusters_image.setProperty('visible', False)
                    clusters_image.setProperty('headerVisible', True)
                    clusters_image.setProperty('headerText', 'Запускаем анализ...')
                else:
                    print("Элемент 'clustersImage' не найден!")

                # Получаем алгоритм и пару переменных
                algorithm_type_combobox = self.window.findChild(QObject, 'algorithmTypeComboBox')
                if algorithm_type_combobox:
                    index = algorithm_type_combobox.property('currentIndex')
                    v = ["Автоматически", "K-Means", "Mean Shift", "DBSCAN"]
                    algorithm = v[index]
                else:
                    print("ComboBox 'algorithmTypeComboBox' не найден!")

                pair_combobox = self.window.findChild(QObject, 'pairComboBox')
                if pair_combobox:
                    index = pair_combobox.property('currentIndex')

                    if 'Магистратура' not in self.frontend_parent.settings.qualifications:
                        #     pair_model = ["Стоимость / Проходной", "Стоимость / Проходной ₽", "Места / Проходной",
                        #                   "Места ₽ / Проходной ₽", "Стоимость / Места ₽", "Стоимость / Рейтинг"]
                        df_pairs = [('Стоимость (в год)', 'Проходной балл на бюджет'),
                                    ('Стоимость (в год)', 'Проходной балл на платное'),
                                    ('Кол-во бюджетных мест', 'Проходной балл на бюджет'),
                                    ('Кол-во платных мест', 'Проходной балл на платное'),
                                    ('Стоимость (в год)', 'Кол-во платных мест'),
                                    ('Стоимость (в год)', 'Место в топе')]
                    else:
                        #     pair_model = ["Стоимость / Места ₽", "Стоимость / Рейтинг"]
                        df_pairs = [('Стоимость (в год)', 'Кол-во платных мест'),
                                    ('Стоимость (в год)', 'Место в топе')]

                    vars = df_pairs[index]
                else:
                    print("ComboBox 'pairComboBox' не найден!")

                self.worker = self.ClusterThreadWorker(self.frontend_parent.filtered_op_list,
                                                       algorithm, vars)
                self.thread = QThread(self)
                self.worker.moveToThread(self.thread)

                self.worker.started.connect(lambda: self._show_message("Запускаем анализ..."))
                # Когда закончили — обновим GUI
                self.worker.finished.connect(self._on_clusters_ready)
                self.worker.finished.connect(self.thread.quit)
                self.worker.finished.connect(self.worker.deleteLater)
                self.thread.finished.connect(self.thread.deleteLater)

                self.thread.started.connect(self.worker.run)
                self.thread.start()

            #     # Создаем менеджера кластеров
            #     clusters_manager = ClustersManager(self.frontend_parent.filtered_op_list, algorithm, vars)
            #
            #     print()
            #     print('=================================')
            #     print('Запускаем кластерный анализ...')
            #     print('Алгоритм:', clusters_manager.algorithm)
            #     print('Пара переменных:', clusters_manager.vars)
            #     print('=================================')
            #     print()
            #
            #     # Запускаем алгоритм
            #     clusters_manager.run_algorithm()
            #
            #     # Выводим информацию в модель
            #     model = clusters_manager.get_model()
            #
            #     clusters_list = self.window.findChild(QObject, 'clustersList')
            #     if clusters_list:
            #         clusters_list.setProperty('clusters', model)
            #     else:
            #         print("Элемент с objectName 'clustersList' не найден")
            #
            #     result_amount_text = self.window.findChild(QObject, 'resultAmountText')
            #     if result_amount_text:
            #         result_amount_text.setProperty('text', f'Получено {len(clusters_manager.clusters)} результатов')
            #     else:
            #         print("Элемент с objectName 'resultAmountText' не найден")
            #
            #     # Отображаем график кластеров
            #     clusters_image = self.window.findChild(QObject, 'clustersImage')
            #     if clusters_image:
            #         clusters_image.setProperty('visible', True)
            #         clusters_image.setProperty('headerVisible', False)
            #         clusters_image.setProperty('source',
            #                                    f'plots_images/clusters_result.png?cacheBust={time()}')
            #     else:
            #         print("Элемент 'clustersImage' не найден!")
            # else:
            #     print("Кнопка 'runClustersButton' не найдена!")
        except Exception as e:
            print("Ошибка при запуске кластерного анализа, возможно:", e)
            try:
                clusters_image = self.window.findChild(QObject, 'clustersImage')
                if clusters_image:
                    clusters_image.setProperty('visible', False)
                    clusters_image.setProperty('headerVisible', True)
                    clusters_image.setProperty('headerText',
                                               'Не удалось провести кластерный анализ<br>Вероятно, недостаточно данных')
                else:
                    print("Элемент 'clustersImage' не найден!")
            except Exception as e:
                print("Ошибка при выводе сообщения пользователю (вероятно, окно закрыто):", e)

    def _show_message(self, message):
        clusters_image = self.window.findChild(QObject, 'clustersImage')
        if clusters_image:
            clusters_image.setProperty('visible', False)
            clusters_image.setProperty('headerVisible', True)
            clusters_image.setProperty('headerText', message)
        else:
            print("Элемент 'clustersImage' не найден!")

    def _on_clusters_ready(self, model):
        clusters_list = self.window.findChild(QObject, 'clustersList')
        if clusters_list:
            clusters_list.setProperty('clusters', model)
        else:
            print("Элемент с objectName 'clustersList' не найден")

        result_amount_text = self.window.findChild(QObject, 'resultAmountText')
        if result_amount_text:
            result_amount_text.setProperty('text', f'Получено {len(model)} результатов')
        else:
            print("Элемент с objectName 'resultAmountText' не найден")

        # Отображаем график кластеров
        clusters_image = self.window.findChild(QObject, 'clustersImage')
        if clusters_image:
            clusters_image.setProperty('visible', True)
            clusters_image.setProperty('headerVisible', False)
            clusters_image.setProperty('source',
                                       f'plots_images/clusters_result.png?cacheBust={time()}')
        else:
            print("Элемент 'clustersImage' не найден!")

    @Slot()
    def on_cancel_cluster_choice_button_clicked(self):
        cancel_cluster_choice_button = self.window.findChild(QObject, 'cancelClusterChoiceButton')
        if cancel_cluster_choice_button:
            # ToDo: работа с выбором/отменой кластеров
            pass
        else:
            print("Кнопка 'cancelClusterChoiceButton' не найдена!")

    @Slot()
    def on_main_window_closed(self):
        print("Главное окно закрыто, закрываем окно кластеров")
        if self.window is not None:
            self.window.close()
            # self.on_window_closed() - выполняется автоматически

    @Slot()
    def on_window_closed(self):
        print("Окно кластеров закрыто (либо пользователем, либо программно)")
        self.window = None
