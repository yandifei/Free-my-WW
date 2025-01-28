# 学习改变最上角的图标
"""
许多程序为了全体好看直接把最上面的标题栏给干掉了，像360，edge浏览器，pycharm等等
重新画关闭，最小化等按钮，以及放大缩小的功能
"""
# 导包
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit
from PyQt6.QtGui import QGuiApplication, QScreen
from PyQt6.QtGui import QIcon   # 图标录入
from PyQt6.QtCore import Qt     # 去掉标题栏
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)    # 进入应用程序的主事件循环，等待用户操作（如点击、按键等）
    win = QWidget(None) # 创建窗口
    # win.setWindowFlags(Qt.WindowType.FramelessWindowHint)   # 无窗口提示
    # win.QtCore.Qt.WindowType
    # win.move(0, 0)  # 初始化窗口位置
    # win.resize(1198, 768)  # 设置窗口大小
    # win.setWindowTitle("鸣潮图标")     # 设置窗口标题
    # win.setWindowIcon(QIcon("鸣潮图标.png")) # 设置最左上角的图标
    # win_label = QWidget(win)   # 设置一个窗口来当标题
    # win_label.resize(200,300)
    # win_label.setWindowTitle("鸣潮图标")     # 设置窗口标题
    # win_label.setWindowIcon(QIcon("鸣潮图标.png")) # 设置最左上角的图标

    # 确保窗口在屏幕中间|使用QGuiApplication的screens()方法获取当前系统中所有屏幕的列表
    GUIapp = QGuiApplication.screens()     # 创建屏幕的列表实例
    center_x = GUIapp[0].availableGeometry().center().x()   # 获得屏幕x的中心
    center_y = GUIapp[0].availableGeometry().center().y()   # 获得屏幕y的中心
    win.move(int(center_x - win.width() / 2), int(center_y - win.height() / 2))     # 移动窗口到屏幕中心

    win.show()  # 展示窗口
    sys.exit(app.exec())    # 关闭程序主事件循环