# 保证窗口显示在屏幕中央
# 导包
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QScreen     # Qt6已经启用视频的方法
import sys



if __name__ == '__main__':
    app = QApplication(sys.argv)    # 设置程序应用循环

    win = QWidget(None)     # 设置窗口和父亲

    win.resize(1198,768)    # 重新设置窗口大小

    # 移动窗口到指定位置
    win.move(0,0)

    # 移动窗口到屏幕中央的操作
    center_pointer = Q

    win.show()  # 显示窗口
    sys.exit(app.exec())    # 安全关闭循环



