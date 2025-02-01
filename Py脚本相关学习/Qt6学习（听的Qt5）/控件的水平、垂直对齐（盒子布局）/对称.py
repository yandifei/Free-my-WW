# 学习控件之间如何对齐
# 导包
"""
添加布局器约束之后就不用把约束的控件放到父对象里面去了
多个控件的布局要容器才能有想要的对齐方式
"""
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QGuiApplication, QScreen
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout # 垂直布局和水平布局
import sys


# 移动窗口到屏幕中心
class MoveToScreenCenter:
    def __init__(self):
        super().__init__()
        screens = QGuiApplication.screens()  # 创建屏幕的列表实例
        center_x = screens[0].availableGeometry().center().x()    # 获得第一个屏幕
        center_y = screens[0].availableGeometry().center().y()
        win.move(int(center_x - win.width() / 2),int(center_y - win.height() / 2))


# 创建窗口的类
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()      # 继承父类的方法和成员
        self.resize(900, 600)   # 设置窗口大小
        # 对称学习
        biggest_layout = QHBoxLayout    # 创建一个全局水平布局器

        # 按钮控件
        layout = QVBoxLayout()  # 创建一个垂直布局器
        # 按钮1
        btn1 =  QPushButton("按钮1")
        # 添加到布局器中
        # layout.addWidget(but1, Qt.AlignmentFlag.AlignTop)
        layout.addWidget(btn1)
        # 按钮2
        btn2 = QPushButton("按钮2")
        # 添加到布局器中
        # layout.addWidget(but1, Qt.AlignmentFlag.AlignTop)
        layout.addWidget(btn2)
        # 按钮3
        btn3 = QPushButton("按钮3")
        # 添加到布局器中
        # layout.addWidget(but3, Qt.AlignmentFlag.AlignTop)
        layout.addWidget(btn3)
        layout.addStretch() # 第一个小的布局
        self.setLayout(layout)  # 让当前窗口使用这个（布局器）排列规则

        # 标签控件
        layout2 = QHBoxLayout()   # 创建一个水平布局器
        label1 = QLabel("标题一")    # 创建标签一
        layout2.addWidget(label1)   # 水平布局约束
        label2 = QLabel("标题二")   # 创建标签二
        layout2.addWidget(label2)   # 水平布局约束
        layout2.addStretch()    # 设置间隔
        self.setLayout(layout2)


        # biggest_layout.addWidget(layout)
        # biggest_layout.addWidget(layout2)
        # self.setLayout(biggest_layout)
        # 如果参数不填默认弹簧比例相同，可以填不同的数字来搞比例的，如果填了即使是1都是最大的，没填理解为0填了理解为1
        # layout.addStretch()     # 添加一个伸缩器（可以控件之间的距离）|最直观的理解就是弹簧，放在不同的位置就扩充那里




if __name__ == '__main__':

    app = QApplication(sys.argv)    # 设置事件循环程序开始
    win = MyWindow()    # 调用创建窗口的类
    moveto_screen_center = MoveToScreenCenter()  # 调用移动到屏幕中心的实例


    win.show()  # 显示窗口

    sys.exit(app.exec())   # 退出事件循环





