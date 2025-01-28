# 保证窗口显示在屏幕中央
# 导包
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit
# QGuiApplication提供了对应用程序级别GUI功能的访问，QScreen表示一个物理屏幕
from PyQt6.QtGui import QGuiApplication, QScreen     # Qt6已经弃用视频的方法，我用AI找了Qt6的
import sys



if __name__ == '__main__':
    app = QApplication(sys.argv)    # 设置程序应用循环
    all_screens = QGuiApplication.screens()  # 使用QGuiApplication的screens()方法获取当前系统中所有屏幕的列表

    win = QWidget(None)     # 设置窗口和父亲
    win.resize(1198,768)    # 重新设置窗口大小

    # 移动窗口到指定位置
    win.move(100,0)

    # 移动窗口到屏幕中央的操作
    available_geometry = all_screens[0].availableGeometry()    # 当前屏幕可用分辨率
    print(f"当前屏幕可用的分辨率: {available_geometry}")
    center_pointer_x_y = available_geometry.center()
    print(center_pointer_x_y)   # 打印当前屏幕中心
    center_pointer_x = available_geometry.center().x()  # 当前屏幕x中心
    center_pointer_y = available_geometry.center().y()  # 当前屏幕y中心
    # 计算窗口移动到屏幕坐标方法1：
    # 计算屏幕该移动的左上角x,y坐标(必须类型强转换)
    win.move(int(center_pointer_x - win.width() / 2), int(center_pointer_y -win.height() / 2))    # 把窗口移动到屏幕正中央
    # 计算窗口移动到屏幕坐标方法2：
    # win_x, win_y, win_width, win_height = win.frameGeometry().getRect()   # 获得窗口的位置和分辨率（元组的形式返回）
    # win.move(int(center_pointer_x - win_width / 2), int(center_pointer_y - win_height / 2))   # 计算坐标并移动到屏幕中央

    win.show()  # 显示窗口

    # 进入应用程序的主事件循环，等待用户操作（如点击、按键等）
    # 当用户关闭主窗口或调用sys.exit()时，exec()方法返回，程序结束
    sys.exit(app.exec())    # 安全关闭循环




"""
    for screen in all_screens:
    # 使用屏幕的geometry()方法获取屏幕的完整几何信息（包括任务栏等）
    screen_geometry = screen.geometry()
    # 使用屏幕的availableGeometry()方法获取屏幕的可用几何信息（不包括任务栏、窗口边框等）
    available_geometry = screen.availableGeometry()
    # 打印屏幕的完整几何信息
    print(f"屏幕分辨率: {screen_geometry}")
    # 打印屏幕的可用几何信息
    print(f"屏幕可用的分辨率: {available_geometry}")
# 打印当前系统中的屏幕总数
print(f"单前屏幕总数: {len(all_screens)}")
"""
