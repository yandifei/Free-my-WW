# PyQt6学习
# 导包
from PyQt6.QtWidgets import QApplication, QWidget    # 管理主界面,控件
from PyQt6.QtWidgets import QLabel    # 标签

import sys

app = QApplication(sys.argv)    # 创建一个应用，参数是当前代码文件的路径
# print(sys.argv)   #   获取当前代码文件的路径
# print(app.arguments())  # 这个也是获取路径的，同上

window = QWidget()
window.setWindowTitle("Free my WW")
window.resize(900,600)
window.move(100,300)
window.show()

lable = QLabel()    # 创建标签实例
lable.setText("Hello World")    # 标签内容
lable.move(100,100)   # 移动标签位置
lable.resize(100,100)   # 设置标签大小
lable.setStyleSheet("background-color:yellow;padding:10px") # 设置标签背景颜色和字体大小
lable.setParent(window)    # 认爹，放进到这个实例窗口里面去
lable.show()    # 展示标签

sys.exit(app.exec()) # 开始执行程序，并且进入消息循环等待(sys.exit是安全退出，直接停止脚本)


