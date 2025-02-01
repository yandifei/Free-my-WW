# 对表单类型的界面进行布局的布局管理器
"""
标签加控件（输入框、按钮等等）
"""
# 导包
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QFormLayout, QLineEdit, QPushButton, QWidget, QApplication


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 设定当前Widget的宽高(可以拉伸大小)
        # self.resize(300, 200)
        # 禁止改变宽高(不可以拉伸)

        # 外部容器
        container = QVBoxLayout()

        # 表单容器
        from_layout = QFormLayout()

        # 创建一个输入框
        edit = QLineEdit()
        edit.setPlaceholderText("请输入账号")
        from_layout.addRow("账号：", edit)

        # 创建另有一个输入框
        edit2 = QLineEdit()
        edit2.setPlaceholderText("请输入密码")
        from_layout.addRow("密码", edit2)

        # 将from_layout添加到垂直布局器中
        container.addLayout(from_layout)

        # 按钮
        login_btn = QPushButton("登录")
        login_btn.setFixedSize(100, 30)

        # 把按钮添加到容器中，并且指定它的对齐方式
        container.addWidget(login_btn, alignment=Qt.AlignmentFlag.AlignRight)

        # 设置全局布局器
        self.setLayout(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = MyWindow()
    win.show()

    sys.exit(app.exec())
