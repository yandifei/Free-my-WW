import sys
from PyQt6.QtCore import Qt, QPoint, QRect
from PyQt6.QtGui import QMouseEvent, QPainter, QColor, QPen, QBrush
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel


class FramelessWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 窗口基础设置
        self.setWindowTitle("无边框可缩放窗口")
        self.setMinimumSize(400, 300)

        # 关键设置：无边框 + 透明背景（用于圆角效果）
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # 窗口边缘检测参数
        self.margin = 8  # 边缘检测宽度
        self.dragging = False  # 是否正在拖拽
        self.drag_edge = None  # 拖拽的边缘方向
        self.drag_start_pos = QPoint()  # 拖拽起始位置
        self.drag_window_geo = QRect()  # 拖拽开始时的窗口几何信息

        # 创建内容控件（示例）
        self.central_widget = QLabel("拖拽边缘调整大小\n点击空白区域移动窗口", self)
        self.central_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.central_widget.setStyleSheet("""
            QLabel {
                background-color: #F0F0F0;
                border: 2px dashed #808080;
                border-radius: 10px;
                font: bold 14px;
                qproperty-alignment: AlignCenter;
            }
        """)
        self.setCentralWidget(self.central_widget)

    # 核心功能：边缘检测和光标设置
    def get_edge(self, pos: QPoint) -> str:
        """ 检测鼠标所在的边缘区域 """
        edges = []
        if pos.x() <= self.margin:
            edges.append("left")
        if pos.x() >= self.width() - self.margin:
            edges.append("right")
        if pos.y() <= self.margin:
            edges.append("top")
        if pos.y() >= self.height() - self.margin:
            edges.append("bottom")
        return "-".join(edges) if edges else None

    def update_cursor(self, edge: str):
        """ 根据边缘区域更新光标形状 """
        cursors = {
            "left": Qt.CursorShape.SizeHorCursor,
            "right": Qt.CursorShape.SizeHorCursor,
            "top": Qt.CursorShape.SizeVerCursor,
            "bottom": Qt.CursorShape.SizeVerCursor,
            "top-left": Qt.CursorShape.SizeFDiagCursor,
            "top-right": Qt.CursorShape.SizeBDiagCursor,
            "bottom-left": Qt.CursorShape.SizeBDiagCursor,
            "bottom-right": Qt.CursorShape.SizeFDiagCursor
        }
        self.setCursor(cursors.get(edge, Qt.CursorShape.ArrowCursor))

    # 鼠标事件处理
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            pos = event.position().toPoint()
            edge = self.get_edge(pos)

            if edge:  # 边缘拖拽缩放
                self.dragging = True
                self.drag_edge = edge
                self.drag_start_pos = event.globalPosition().toPoint()
                self.drag_window_geo = self.geometry()
            else:  # 窗口移动
                self.drag_start_pos = event.globalPosition().toPoint()
                self.drag_window_pos = self.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.dragging:  # 处理窗口缩放
            delta = event.globalPosition().toPoint() - self.drag_start_pos
            new_geo = self.drag_window_geo

            # 根据拖拽方向调整窗口几何
            if "left" in self.drag_edge:
                new_geo.setLeft(new_geo.left() + delta.x())
            if "right" in self.drag_edge:
                new_geo.setRight(new_geo.right() + delta.x())
            if "top" in self.drag_edge:
                new_geo.setTop(new_geo.top() + delta.y())
            if "bottom" in self.drag_edge:
                new_geo.setBottom(new_geo.bottom() + delta.y())

            # 确保窗口不小于最小尺寸
            if new_geo.width() < self.minimumWidth():
                if "left" in self.drag_edge:
                    new_geo.setLeft(new_geo.right() - self.minimumWidth())
                else:
                    new_geo.setWidth(self.minimumWidth())
            if new_geo.height() < self.minimumHeight():
                if "top" in self.drag_edge:
                    new_geo.setTop(new_geo.bottom() - self.minimumHeight())
                else:
                    new_geo.setHeight(self.minimumHeight())

            self.setGeometry(new_geo)
        else:  # 处理窗口移动和光标更新
            if event.buttons() == Qt.MouseButton.LeftButton:
                self.move(self.pos() + event.globalPosition().toPoint() - self.drag_start_pos)
                self.drag_start_pos = event.globalPosition().toPoint()
            else:
                edge = self.get_edge(event.position().toPoint())
                self.update_cursor(edge)

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.dragging = False
        self.drag_edge = None

    # 可选：添加窗口阴影和圆角（需要重写paintEvent）
    def paintEvent(self, event):
        # 创建带有阴影的圆角矩形
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # 绘制阴影
        shadow_color = QColor(0, 0, 0, 50)
        painter.setPen(QPen(shadow_color, 8))
        painter.drawRoundedRect(self.rect().adjusted(4, 4, -4, -4), 10, 10)

        # 绘制主背景
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(self.rect(), 10, 10)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FramelessWindow()
    window.show()
    sys.exit(app.exec())