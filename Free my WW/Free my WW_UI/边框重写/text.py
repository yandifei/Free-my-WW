import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, QRect, QPoint
from PyQt6.QtGui import QCursor, QMouseEvent


class FramelessResizableWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("无标题栏可拉伸缩放窗口示例")
        self.setMinimumSize(400, 300)  # 设置最小窗口尺寸

        # 隐藏标题栏
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # 主内容区域
        content = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("无标题栏窗口内容区域", self))
        content.setLayout(layout)
        self.setCentralWidget(content)

        # 窗口边缘检测参数
        self.margin = 20  # 边缘检测的像素宽度
        self.dragging = False  # 是否正在拖拽
        self.drag_edge = None  # 当前拖拽的边缘（'left', 'right', 'top', 'bottom', 'top-left' 等）
        self.drag_start_pos = None  # 拖拽起始位置
        self.drag_window_geometry = None  # 拖拽起始时的窗口几何形状

        # 初始光标
        self.setCursor(Qt.CursorShape.ArrowCursor)

    # --- 核心逻辑：边缘检测和光标切换 ---
    def get_edge(self, pos: QPoint) -> str:
        """根据鼠标位置返回当前所在的边缘区域"""
        rect = self.rect()
        x, y = pos.x(), pos.y()

        edges = []
        if x <= self.margin:
            edges.append("left")
        if x >= rect.width() - self.margin:
            edges.append("right")
        if y <= self.margin:
            edges.append("top")
        if y >= rect.height() - self.margin:
            edges.append("bottom")

        # 组合边缘（如 'top-left'）
        if len(edges) == 0:
            return None
        elif len(edges) == 1:
            return edges[0]
        else:
            return "-".join(edges)

    def update_cursor(self, edge: str):
        """根据边缘区域设置光标形状"""
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
        if edge in cursors:
            self.setCursor(cursors[edge])
        else:
            self.setCursor(Qt.CursorShape.ArrowCursor)

    # --- 鼠标事件处理 ---
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            pos = event.position().toPoint()
            edge = self.get_edge(pos)

            # 如果在边缘区域，则触发窗口缩放
            if edge:
                self.drag_start_pos = event.globalPosition().toPoint()
                self.drag_edge = edge
                self.drag_window_geometry = self.geometry()
                self.dragging = True
            # 否则触发窗口移动
            else:
                self.drag_start_pos = event.globalPosition().toPoint()
                self.drag_window_pos = self.pos()
                self.dragging = "move"
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.dragging == "move":
            # 处理窗口移动
            delta = event.globalPosition().toPoint() - self.drag_start_pos
            self.move(self.drag_window_pos + delta)
        elif self.dragging:
            # 处理窗口缩放
            delta = event.globalPosition().toPoint() - self.drag_start_pos
            new_geo = self.drag_window_geometry

            if "left" in self.drag_edge:
                new_geo.setLeft(new_geo.left() + delta.x())
            if "right" in self.drag_edge:
                new_geo.setRight(new_geo.right() + delta.x())
            if "top" in self.drag_edge:
                new_geo.setTop(new_geo.top() + delta.y())
            if "bottom" in self.drag_edge:
                new_geo.setBottom(new_geo.bottom() + delta.y())

            # 确保窗口不小于最小尺寸
            new_geo = new_geo.normalized()
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
        else:
            # 更新光标形状
            edge = self.get_edge(event.position().toPoint())
            self.update_cursor(edge)
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.dragging = False
        self.drag_edge = None
        super().mouseReleaseEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FramelessResizableWindow()
    window.show()
    sys.exit(app.exec())