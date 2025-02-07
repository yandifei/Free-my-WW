# 去掉原来的边框，直接重写
# 导包
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6 import uic
from PyQt6.QtGui import QGuiApplication  # Qscreen获取屏幕分辨率
# 导入自己的包


class InitWin:

    def __init__(self,ui_path):
        super().__init__()  # 习惯
        self.ui_path = ui_path  # ui文件路径
        self.win = uic.loadUi(self.ui_path)  # 创建ui窗口对象(实例)
        self.all_screens = QGuiApplication.screens()  # 使用QGuiApplication的screens()方法获取当前系统中所有屏幕的列表
        self.init_win()

    # 初始化窗口
    def init_win(self):
        self.win.resize(1280,720)   # 确保窗口大小是1280,720
        self.get_current_screen_center()  # 获得当前屏幕可用的分辨率并移动到屏幕中央
        self.win.show()  # 展示窗口

    # 获得当前屏幕可用的分辨率并移动到屏幕中央
    def get_current_screen_center(self):
        self.current_screen_xy = self.all_screens[0].availableGeometry()  # 当前屏幕可用分辨率
        print(f"当前屏幕可用的分辨率: {self.current_screen_xy.x(),self.current_screen_xy.y()}")  # 打印当前屏幕的分辨率吧
        self.center_pointer_x_y = self.current_screen_xy.center()
        print(f"当前屏幕可用分辨率的中心是{self.center_pointer_x_y}")  # 打印当前屏幕中心
        # 计算屏幕该移动的左上角x,y坐标(必须类型强转换)
        self.win.move(int(self.center_pointer_x_y.x() - self.win.width() / 2), int(self.center_pointer_x_y.y() - self.win.height() / 2))  # 把窗口移动到屏幕正中央






if __name__ == '__main__':
    Free_my_WW_app = QApplication(sys.argv)    # 开始事件循环
    Free_my_WW_win = InitWin("./边框重写.ui")   # 创建实例对象
    sys.exit(Free_my_WW_app.exec())    # 退出事件循环