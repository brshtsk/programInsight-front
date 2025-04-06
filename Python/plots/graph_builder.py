from matplotlib.figure import Figure
import numpy as np
from scipy.stats import gaussian_kde


class GraphBuilder:
    GREEN = '#53b93f'
    ORANGE = '#ed9528'
    BLUE = '#49c0de'
    PINK = '#de49a2'
    GRAY = '#696969'
    BLACK = '#000000'
    FZ = 12
    TITLE_FZ = 14

    @staticmethod
    def get_transparent_fig(a, b):
        fig = Figure(figsize=(a, b))
        fig.patch.set_alpha(0)
        ax = fig.add_subplot(111)
        ax.set_facecolor('none')
        return fig, ax

    @staticmethod
    def set_scatter_signs(ax, title, x_label, y_label, color='black'):
        """
        Для графиков с плотностью распределения
        """
        # Не устанавливаем заголовок и подписи к осям
        # ax.set_title(title, fontsize=GraphBuilder.TITLE_FZ, color=color)
        # ax.set_xlabel(x_label, fontsize=GraphBuilder.FZ, color=color)
        # ax.set_ylabel(y_label, fontsize=GraphBuilder.FZ, color=color)
        ax.ticklabel_format(style='plain', axis='x')
        ax.tick_params(axis='both', colors=color)
        ax.grid(True, axis='x', linestyle='--', linewidth=3, alpha=0.5, color=color)

        # Убираем отображение значений оси Y
        ax.tick_params(axis='y', labelleft=False)

        # Увеличиваем размер подписей по оси x
        ax.tick_params(axis='x', labelsize=26)

        # Убираем рамку графика
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)

        ax.spines['bottom'].set_color(color)
        ax.spines['left'].set_color(color)

    @staticmethod
    def set_scatter_signs_points(ax, title, x_label, y_label, color='black'):
        # Устанавливаем заголовок и подписи с увеличенным шрифтом и жирным начертанием
        ax.set_title(title, fontsize=18, fontweight='bold', color=color)
        ax.set_xlabel(x_label, fontsize=16, fontweight='bold', color=color)
        ax.set_ylabel(y_label, fontsize=16, fontweight='bold', color=color)

        ax.ticklabel_format(style='plain', axis='x')
        # Устанавливаем размеры и цвет подписей осей
        ax.tick_params(axis='both', colors=color, labelsize=16)
        ax.grid(True, linestyle='--', linewidth=1.5, alpha=0.5, color=GraphBuilder.GRAY)

        # Отключаем видимость лишних рамок
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_color(color)
        ax.spines['left'].set_color(color)

    @staticmethod
    def donut_chart(df) -> (Figure, list[dict]):
        """
        Создаёт круговую диаграмму с формами обучения и квалификациями,
        а также возвращает данные для отображения в таблице.
        :param df:
        :return:
        """
        fig, ax = GraphBuilder.get_transparent_fig(6, 6)
        list_stats_data = []

        # Обработка форм обучения
        forms = df['Форма обучения'].explode()
        counts = forms.value_counts()
        print("Формы обучения:", forms.unique())
        if len(counts) > 4:
            raise ValueError("Количество форм обучения превышает 4")
        form_colors = [GraphBuilder.GREEN, GraphBuilder.ORANGE, GraphBuilder.BLUE, GraphBuilder.PINK][:len(counts)]
        total_forms = counts.sum()
        ax.pie(
            counts.values,
            radius=1,
            wedgeprops={'width': 0.2, 'edgecolor': (1, 1, 1, 0.3)},
            colors=form_colors
        )
        for i, (form, count) in enumerate(counts.items()):
            percent = count / total_forms
            list_stats_data.append({
                "propertyNameText": form,
                "propertyValueText": str(count),
                "propertyPercentText": f"{percent * 100:.1f}%",
                "floatPercent": float(round(percent, 3)),  # Перевод из numpy.float64 в float
                "percentColor": form_colors[i],
                "barBackground": "#ffffff"
            })

        # Обработка квалификаций
        qc = df['Квалификация'].value_counts()
        print("Квалификации:", df['Квалификация'].unique())
        if len(qc) > 2:
            raise ValueError("Количество квалификаций превышает 2")
        if len(qc) > 1:
            qual_colors = [GraphBuilder.GRAY, GraphBuilder.BLACK][:len(qc)]
            total_quals = qc.sum()
            ax.pie(
                qc.values,
                radius=0.8,
                wedgeprops={'width': 0.2, 'edgecolor': (1, 1, 1, 0.3)},
                colors=qual_colors
            )
            for i, (qual, count) in enumerate(qc.items()):
                percent = count / total_quals
                list_stats_data.append({
                    "propertyNameText": qual,
                    "propertyValueText": str(count),
                    "propertyPercentText": f"{percent * 100:.1f}%",
                    "floatPercent": float(round(percent, 3)),  # Перевод из numpy.float64 в float
                    "percentColor": qual_colors[i],
                    "barBackground": "#ffffff"
                })

        return fig, list_stats_data

    @staticmethod
    def build_kde_layout(var, title, x_label, color='black'):
        # Задаём размеры графика с соотношением 5:3 (ширина: 10, высота: 6)
        fig, ax = GraphBuilder.get_transparent_fig(10, 6)
        GraphBuilder.set_scatter_signs(ax, title, x_label, 'Плотность', color)
        ls = np.linspace(min(var), max(var), 200)
        kde = gaussian_kde(var)
        ax.plot(ls, kde(ls), color=color, linewidth=4)
        return fig

    @staticmethod
    def price_kde(df):
        title = 'Распределение годовой стоимости (очное обучение)\n'
        prices = df['Стоимость (в год)'].dropna()
        prices = prices[prices <= 1_000_000] / 1000
        return GraphBuilder.build_kde_layout(prices, title, 'Стоимость, тыс. руб')

    @staticmethod
    def points_kde(df):
        title = 'Распределение проходных баллов ЕГЭ\n'
        points = df.apply(
            lambda row: row['Проходной балл на бюджет'] / row['Кол-во экзаменов']
            if row['Проходной балл на бюджет'] is not None and row['Кол-во экзаменов'] > 0 else None,
            axis=1
        ).dropna()
        return GraphBuilder.build_kde_layout(points, title, 'Баллы', 'white')

    @staticmethod
    def price_to_points_scatter(df, budget: bool):
        if budget:
            score_type = 'Проходной балл на бюджет'
        else:
            score_type = 'Проходной балл на платное'

        title = 'Зависимость стоимости и проходного балла лучших вузов\n'
        fig, ax = GraphBuilder.get_transparent_fig(9, 6)
        GraphBuilder.set_scatter_signs_points(ax, title, 'Стоимость, тыс. руб', score_type)
        filtered_df = df[df['Место в топе'] < 13].copy()
        if filtered_df.empty:
            raise ValueError("Нет данных для построения графика")
        filtered_df['Кол-во экзаменов'] = filtered_df['Кол-во экзаменов'].replace(0, np.nan)
        filtered_df[score_type] = filtered_df[score_type] / filtered_df['Кол-во экзаменов']
        grouped = filtered_df.groupby('Университет').agg(
            {'Стоимость (в год)': 'mean', score_type: 'mean'})
        grouped['Стоимость (в год)'] = grouped['Стоимость (в год)'] / 1000

        # Увеличен размер точек (s=150)
        ax.scatter(grouped['Стоимость (в год)'], grouped[score_type], color=GraphBuilder.GREEN, s=150)

        # Увеличен размер шрифта для подписей (fontsize=14)
        for uni, row in grouped.iterrows():
            ax.text(
                row['Стоимость (в год)'] + 10,
                row[score_type],
                uni,
                fontsize=14,
                fontweight='bold',
                ha='left',
                va='center',
                color=GraphBuilder.GREEN
            )
        return fig
