import QtQuick 2.15


Item {
    id: root
    property real progress: 0.75  // Процент заполнения (0.0 - 1.0)
    property color progressColor: "#007aff"  // Цвет прогресса
    property color backgroundColor: "#d0d0d0"  // Цвет фона
    property int strokeWidth: 8  // Толщина линии
    width: 100
    height: 100

    Canvas {
        id: canvas
        anchors.fill: parent
        onPaint: {
            var ctx = getContext("2d");
            ctx.reset();

            var centerX = width / 2;
            var centerY = height / 2;
            var radius = width / 2 - strokeWidth / 2;
            var startAngle = -Math.PI / 2; // Начинаем сверху
            var endAngle = startAngle + (2 * Math.PI * progress); // Вычисляем дугу

            // Фон (серый круг)
            ctx.beginPath();
            ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
            ctx.lineWidth = strokeWidth;
            ctx.strokeStyle = backgroundColor;
            ctx.stroke();

            // Прогресс (синяя дуга)
            ctx.beginPath();
            ctx.arc(centerX, centerY, radius, startAngle, endAngle);
            ctx.lineWidth = strokeWidth;
            ctx.strokeStyle = progressColor;
            ctx.lineCap = "round";  // Скруглённые концы
            ctx.stroke();
        }
    }

    // Обновляем canvas при изменении прогресса
    onProgressChanged: canvas.requestPaint()
}
