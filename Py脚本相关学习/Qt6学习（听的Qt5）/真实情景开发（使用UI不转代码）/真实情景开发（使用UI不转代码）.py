# 不需要转换代码，直接使用Qt保存的界面开发就可以了
# 导包
import sys
import os
import time

from PyQt6.QtCore import QThread
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QPushButton, QLabel
from PyQt6 import uic

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = None
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("登录界面.ui")
        # print(self.ui)  # ui文件中最顶层的对象（Form）
        # print(self.ui.__dict__)     # 最顶层对象的所有属性（key: value方式显示）
        # print(self.ui.label)    # ui文件的label控件
        # print(self.ui.label.text())     # label控件的文字
        self.user_name = self.ui.lineEdit    # 获取用户名
        self.password = self.ui.lineEdit_2   # 密码
        self.login_btn = self.ui.pushButton  # 登录按钮
        self.forget_btn = self.ui.pushButton_2   # 忘记密码按钮
        self.text_browser = self.ui.textBrowser  # 文本显示区域

        # 给登录按钮被点击绑定槽函数
        self.login_btn.clicked.connect(self.login)   # 添加的函数不能写括号，不然什么收调用都不知道

    def login(self):
        """实现登录的逻辑"""
        print("正在登录。。。。。。")
        # 提取用户名和密码
        print(self.user_name.text())
        user_name = self.user_name.text()
        print(self.password.text())
        password = self.password.text()

        self.thread = MyThreading()  # 创建线程对象
        self.thread.start()    # 启动线程

        if user_name == "yandifei" and password == "yandifei":
            self.text_browser.setText(f"欢迎{user_name}")
            self.text_browser.repaint()
        else:
            self.text_browser.setText("账号或密码输入错误。。。。请重试")
            self.text_browser.repaint()

# QUI线程调用
class MyThreading(QThread):
    def run(self):
        for i in range(10):
            print(f"正在登录服务器...{i + 1}")
            time.sleep(1)



if __name__ == '__main__':
    app = QApplication(sys.argv)    # 开始界面事件循环

    win = MyWindow()
    win.ui.show()   # 展示UI文件的窗口

    sys.exit(app.exec())    # 退出界面事件循环