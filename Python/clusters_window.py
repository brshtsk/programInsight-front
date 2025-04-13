from PySide6.QtCore import QObject, Slot, Signal
from PySide6.QtQml import QQmlComponent
from utils import Utils


class ClustersWindow(QObject):
    updateModels = Signal()  # Сигнал для уведомления Frontend об изменениях

    def __init__(self, engine, frontend_parent):
        super().__init__()
        self.engine = engine
        self.frontend_parent = frontend_parent
        self.component = None
        self.window = None
        self.new_exam_window = None
        # ToDo: рабочий список кластеров
        self.available_clusters = []

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
            result_amount_text.setProperty('text', f'Получено {len(self.available_clusters)} результатов')
        else:
            print("Элемент с objectName 'resultAmountText' не найден")

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

    @Slot()
    def on_cancel_cluster_choice_button_clicked(self):
        cancel_cluster_choice_button = self.window.findChild(QObject, 'cancelClusterChoiceButton')
        if cancel_cluster_choice_button:
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
