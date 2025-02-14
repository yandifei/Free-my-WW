import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QMouseEvent, QCursor


class EdgeDetectionWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 窗口基础设置
        self.setWindowTitle("边缘检测演示窗口")
        self.setGeometry(300, 300, 800, 600)


        self.setMouseTracking(True) # 启用鼠标追踪（无需按住按键即可接收移动事件）

        # 边缘检测阈值（单位：像素）
        self.edge = 10
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.border_radius = 20
        self.dragging = False

    def mousePressEvent(self, event):
        print("按下了窗口")


    def mouseMoveEvent(self, event):
        print(f"鼠标在窗口内的相对坐标{event.position().x(), event.position().y()}")
        """ 核心边缘检测逻辑 """
        # 获取鼠标相对窗口的位置
        pos = event.position().toPoint()

        # 获取窗口当前尺寸
        window_width = self.width()
        window_height = self.height()

        # 边缘区域判断
        left_edge = pos.x() <= self.edge
        right_edge = pos.x() >= window_width - self.edge
        top_edge = pos.y() <= self.edge
        bottom_edge = pos.y() >= window_height - self.edge

        # 组合判断
        is_edge = left_edge or right_edge or top_edge or bottom_edge

        if is_edge:
            # 精确判断边缘方向并设置对应光标
            if left_edge and top_edge or right_edge and bottom_edge:
                self.setCursor(Qt.CursorShape.SizeFDiagCursor)  # 左上/右下
                print("\033[92m左上或者右下\033[0m")  # 绿色文字提示
            elif left_edge and bottom_edge or right_edge and top_edge:
                self.setCursor(Qt.CursorShape.SizeBDiagCursor)  # 左下/右上
                print("\033[92m左下/右上\033[0m")  # 绿色文字提示
            elif left_edge or right_edge:
                self.setCursor(Qt.CursorShape.SizeHorCursor)  # 左右
                print("\033[92m左右\033[0m")  # 绿色文字提示
            else:
                self.setCursor(Qt.CursorShape.SizeVerCursor)  # 上下
                print("\033[92m上下\033[0m")  # 绿色文字提示
        else:
            self.setCursor(Qt.CursorShape.ArrowCursor)  # 默认光标
        print("\033[92m默认\033[0m")  # 绿色文字提示

        # super().mouseMoveEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EdgeDetectionWindow()
    window.show()
    sys.exit(app.exec())
