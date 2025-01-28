# 看另一个up写的
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit
import sys


# 开始程序撰写
if __name__ == '__main__':
    app = QApplication(sys.argv)    # 创建程序对象

    # 创建窗口
    win = QWidget(None)
    # win.setGeometry(200,200,1198,768)   # 设置初始窗口大小

    # 标签设置
    # label = QLabel("账号: ",win)  # 创建标签并且设置父窗口
    # label.setGeometry(20,20, 30,20)  # 设置标签窗口大小
    #
    # # 文本框设置
    # edit =  QLineEdit(win) # 创建文本框并且设置父窗口
    # edit.setPlaceholderText("请输入账号")
    # edit.setGeometry(60,20, 100,20)  # 设置标签窗口大小
    #
    # # 按钮设置
    # but = QPushButton("注册", win)    # 创建按钮并且设置父窗口
    # but.setGeometry(60,50, 40,20)

    win.resize(1198,768)    # 重新设置窗口大小为1198，768。（默认是屏幕中央位置，但不是100%有效）
    win.show()  # 展示窗口

    sys.exit(app.exec())    # 关闭窗口循环
