# 自我研究学习
import sys
import os

from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget
import PyQt6.QtCore
from PyQt6 import uic



class FreeMyWW:
    def __init__(self):
        super().__init__()
        self.win = uic.loadUi("./深入学习.ui")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("Load_Pic2.png"))    # 设置窗口图标
    # self.win.QPixmap("Load_Pic.png")  # 替换为你的图标路径
    free_my_ww = FreeMyWW()
    free_my_ww.win.show()

    sys.exit(app.exec())
