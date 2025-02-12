import sys
from PyQt6.QtCore import Qt, QPoint, QRect
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel


class FramelessWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置无边框窗口
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        QLabel("hello world")
        self.setMinimumSize(400, 300)

        # 边缘检测参数
        self.border_width = 20
        self._is_resizing = False
        self.resize_direction = None
        self.start_pos = QPoint()
        self.start_geometry = QRect()

        # 支持拖拽的中央控件
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

    def get_resize_direction(self, pos):
        """根据鼠标位置判断调整方向"""
        rect = self.rect()
        directions = {
            "left": (pos.x() <= self.border_width),
            "right": (pos.x() >= rect.width() - self.border_width),
            "top": (pos.y() <= self.border_width),
            "bottom": (pos.y() >= rect.height() - self.border_width)
        }

        # 组合方向
        direction = []
        if directions["left"]: direction.append("left")
        if directions["right"]: direction.append("right")
        if directions["top"]: direction.append("top")
        if directions["bottom"]: direction.append("bottom")

        return "+".join(direction) if direction else None

    def update_cursor(self, direction):
        """根据方向更新鼠标样式"""
        cursors = {
            "left": Qt.CursorShape.SizeHorCursor,
            "right": Qt.CursorShape.SizeHorCursor,
            "top": Qt.CursorShape.SizeVerCursor,
            "bottom": Qt.CursorShape.SizeVerCursor,
            "left+top": Qt.CursorShape.SizeFDiagCursor,
            "right+bottom": Qt.CursorShape.SizeFDiagCursor,
            "right+top": Qt.CursorShape.SizeBDiagCursor,
            "left+bottom": Qt.CursorShape.SizeBDiagCursor
        }
        self.setCursor(cursors.get(direction, Qt.CursorShape.ArrowCursor))

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.start_pos = event.globalPosition().toPoint()
            self.start_geometry = self.geometry()
            self.resize_direction = self.get_resize_direction(event.position().toPoint())

            if self.resize_direction:
                self._is_resizing = True
            else:
                # 非边缘区域拖拽窗口
                self._is_dragging = True
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        pos = event.position().toPoint()

        # 更新光标形状
        if not self._is_resizing:
            direction = self.get_resize_direction(pos)
            self.update_cursor(direction)

        # 调整窗口大小
        if self._is_resizing:
            delta = event.globalPosition().toPoint() - self.start_pos
            new_geo = self.start_geometry

            if "left" in self.resize_direction:
                new_geo.setLeft(new_geo.left() + delta.x())
            if "right" in self.resize_direction:
                new_geo.setRight(new_geo.right() + delta.x())
            if "top" in self.resize_direction:
                new_geo.setTop(new_geo.top() + delta.y())
            if "bottom" in self.resize_direction:
                new_geo.setBottom(new_geo.bottom() + delta.y())

            # 限制最小尺寸
            if new_geo.width() > self.minimumWidth() and new_geo.height() > self.minimumHeight():
                self.setGeometry(new_geo)

        # 窗口拖拽
        elif self._is_dragging:
            delta = event.globalPosition().toPoint() - self.start_pos
            self.move(self.pos() + delta)
            self.start_pos = event.globalPosition().toPoint()

        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self._is_resizing = False
        self._is_dragging = False
        self.setCursor(Qt.CursorShape.ArrowCursor)
        super().mouseReleaseEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FramelessWindow()
    window.show()
    sys.exit(app.exec())

