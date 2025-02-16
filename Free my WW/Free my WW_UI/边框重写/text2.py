import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtCore import Qt, QPoint

class MouseTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.delta = QPoint(0,0)
        self.last_pos = QPoint(0,0)  # 记录上一次鼠标位置
        self.current_pos = QPoint(0,0)

    def initUI(self):
        self.setWindowTitle('实时鼠标追踪')
        self.setGeometry(100, 100, 400, 300)
        self.label = QLabel("移动鼠标查看坐标变化", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.resize(400, 300)

        # 关键设置：启用鼠标追踪（即使不按下按钮也会触发移动事件）
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.current_pos = event.pos()  # 获取当前鼠标位置
        if not self.last_pos.isNull():
            self.delta = self.current_pos - self.last_pos  # 计算变化量
            self.label.setText(
                f"实时坐标: ({self.current_pos.x()}, {self.current_pos.y()})\n"
                f"位移变化: ({self.delta.x()}, {self.delta.y()})"
            )

    def mouseReleaseEvent(self, event):
        self.resize(500,500)


        self.last_pos = self.current_pos  # 更新最后位置
        super().mouseMoveEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MouseTracker()
    window.show()
    sys.exit(app.exec())