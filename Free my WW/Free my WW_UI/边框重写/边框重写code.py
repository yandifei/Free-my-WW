# 去掉原来的边框，直接重写
# 导包
import sys
sys.path.append("D:\\鸣潮脚本\\Free-my-WW\\Free my WW\\Free_my_WW_package")

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt, QPoint # Qt用来干掉边框
from PyQt6 import uic

from Free_my_WW_package.EnvironmentCheck import *
import Free_my_WW_package
from 边框重写 import *

class WinShow(QWidget):
    """展示窗口（当前主显示器屏幕中央）
    这个窗口经过了处理，去掉了标题栏（因此最大化、最小化、关闭、拖拽都没了）
    图标得自己画，拖拽这里会写回来
    """
    def __init__(self,ui_file_path):
        super().__init__()  # 习惯
        self.current_screen_xy = get_screen_resolution()  # 获得屏幕分辨率率
        self.ui_file_path = ui_file_path  # ui文件路径，后缀名不一定是.ui，转为py也可以
        self.import_ui()    # 创建ui对象，导入ui
        self.delete_title_bar() # 重写标题栏
        self.move_center_win()  # 确保窗口在屏幕中央
        self.dragging = False  # 初始窗口拖拽为关闭（开启的话会导致鼠标不点击也能拖拽）
        self.offset = QPoint()  # 获取鼠标移动的像素点，offset（消耗）
        self.show()  # 展示窗口

    def import_ui(self):
        """判断ui是ui文件还是ui转py文件"""
        if ".ui" in self.ui_file_path:  # 判断是否为ui文件
            uic.loadUi(self.ui_file_path, self)  # 创建ui窗口对象(实例)
        elif ".py" in self.ui_file_path:  # 判断是否为py文件
            pass # 这里以后改进，在自己录下遍历ui转py的文件，并加入系统路径，然后通过分析用户给的路径分割包名导入
            """这里爆红不用管，因为没有导入ui转py文件，这里找不到Ui_Form的类"""
            try:    # 如果改进了这个异常处理也可以删了
                Ui_Form().setupUi(self)  # 继承界面的类
            except(SyntaxError,NameError):
                raise SyntaxError("未能导入该模块，请检查是否在同一目录下")
        else:
            raise NameError("输入入的既不是ui文件，也不是ui转py文件")

    def move_center_win(self):
        """把窗口移动到屏幕中央
        计算主显示器屏幕中央的逻辑分辨率
        获得计算窗口大小并除2
        计算窗口移动位置
        把窗口移动到指定位置，移动后窗口显示在屏幕中央
        """
        sys_feedback(f"主显示器的逻辑分辨率: {self.current_screen_xy[0]}X{self.current_screen_xy[1]}")   # 打印当前屏幕的分辨率吧
        current_screen_center_x = self.current_screen_xy[0] / 2    # 计算水平中心
        current_screen_center_y = self.current_screen_xy[1] / 2    # 计算垂直中心
        sys_feedback(f"主显示器屏幕的中心坐标:{current_screen_center_x},{current_screen_center_y}")  # 打印当前屏幕中心
        move_x = int(current_screen_center_x - (self.width() / 2))
        move_y = int(current_screen_center_y - (self.height() / 2))
        progress_feedback(f"Free my WW 移动坐标：{move_x},{move_y}")
        self.move(move_x,move_y)  # 把窗口移动到屏幕正中央

    def delete_title_bar(self):
        # 去掉了标题栏（顺带去掉了拖拽，窗口就一直置顶无法关闭）
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

    def mousePressEvent(self, event):
        """重写鼠标事件（在按下鼠标开启拖拽功能并记录鼠标偏移量）"""
        if event.button() == Qt.MouseButton.LeftButton:
            # 记录鼠标全局位置与窗口位置的偏移量
            self.offset = event.globalPosition().toPoint() - self.pos()
            self.dragging = True

    def mouseMoveEvent(self, event):
        """根据当前鼠标位置计算窗口新位置"""
        if self.dragging:
            self.move(event.globalPosition().toPoint() - self.offset)

    def mouseReleaseEvent(self, event):
        """鼠标松开，停止拖拽"""
        self.dragging = False

    def mouseDoubleClickEvent(self, event):
        """双击最大化/恢复"""
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def top(self):
        """窗口一直置顶，即使切换应用也还是置顶"""
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)




if __name__ == '__main__':
    Free_my_WW_app = QApplication(sys.argv)  # 管理控制事件流和设置
    Free_my_WW = WinShow("./边框重写.ui")   # 创建实例对象
    sys.exit(Free_my_WW_app.exec()) # 安全退出界面任务

