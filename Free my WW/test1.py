import sys

from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget


class Win(QWidget):
    def __init__(self):
        super().__init__()
        # self.setWindowFlag(Qt.WindowType.FramelessWindowHint)   # 去掉标题栏
        # self.ui = None
        # self.ui = uic.loadUi("B:\\测试.ui", self)  # 创建ui窗口对象(实例)
        # self.GlobalWidget.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # 窗口透明
        hwnd = int(self.winId())  # 转换为整数
        print(f"生成的无边框窗口句柄:{hwnd}")


app =  QApplication(sys.argv)
win = Win()
win.show()
sys.exit(app.exec())
