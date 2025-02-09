# 去掉原来的边框，直接重写
# 导包
import sys
from traceback import print_tb
from tracemalloc import Frame

sys.path.append("D:\\鸣潮脚本\\Free-my-WW\\Free my WW\\Free_my_WW_package")

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt, QPoint # Qt用来干掉边框
from PyQt6 import uic

from Free_my_WW_package.EnvironmentCheck import *
import Free_my_WW_package.UserFeedback
from 边框重写 import *

class WinShow:
    """展示窗口（当前主显示器屏幕中央）
    这个窗口经过了处理，去掉了标题栏（因此最大化、最小化、关闭、拖拽都没了）
    图标得自己画，拖拽这里会写回来
    """
    def __init__(self,ui_file_path):
        super().__init__()  # 习惯
        self.ui_file_path = ui_file_path  # ui文件路径，后缀名不一定是.ui，转为py也可以
        self.Free_my_WW_app = QApplication(sys.argv)  # 开始事件循环

        if ".ui" in self.ui_file_path:  # 判断是否为ui文件
            self.Free_my_WW_win = uic.loadUi(self.ui_file_path)  # 创建ui窗口对象(实例)
        elif ".py" in self.ui_file_path:  # 判断是否为py文件
            pass # 这里以后改进，在自己录下遍历ui转py的文件，并加入系统路径，然后通过分析用户给的路径分割包名导入
            self.Free_my_WW_win = QWidget()  # 创建窗口实例
            """这里爆红不用管，因为没有导入ui转py文件，这里找不到Ui_Form的类"""
            try:    # 如果改进了这个异常处理也可以删了
                # sys.path.append(f"{os.getcwd()}\\{self.ui_file_path}")
                # importlib.import_module(self.ui_file_path)  # 通过包名导入包
                Ui_Form().setupUi(self.Free_my_WW_win)  # 继承界面的类
            except(SyntaxError,NameError):
                raise SyntaxError("未能导入该模块，请检查是否在同一目录下")

        self.dragging = False  # 初始窗口拖拽为关闭（开启的话会导致鼠标不点击也能拖拽）
        self.offset = QPoint()  # 获取鼠标移动的像素点，offset（消耗）
        self.current_screen_xy = get_screen_resolution()    # 获得屏幕分辨率率
        self.move_center_win()  # 确保窗口在屏幕中央
        self.delete_title_bar() # 重写标题栏
        self.Free_my_WW_win.show()  # 展示窗口
        sys.exit(self.Free_my_WW_app.exec())  # 退出事件循环


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
        move_x = int(current_screen_center_x - (self.Free_my_WW_win.width() / 2))
        move_y = int(current_screen_center_y - (self.Free_my_WW_win.height() / 2))
        progress_feedback(f"Free my WW 移动坐标：{move_x},{move_y}")
        self.Free_my_WW_win.move(move_x,move_y)  # 把窗口移动到屏幕正中央

    def delete_title_bar(self):
        # 去掉了标题栏（顺带去掉了拖拽，窗口就一直置顶无法关闭）
        self.Free_my_WW_win.setWindowFlag(Qt.WindowType.FramelessWindowHint)

    def mousePressEvent(self, event):
        """重写鼠标事件（在按下鼠标开启拖拽功能）"""
        if event.button() == Qt.MouseButton.LeftButton:
            print(event.button())
            print(Qt.MouseButton.LeftButton)
            # 记录鼠标全局位置与窗口位置的偏移量
            self.offset = event.globalPosition().toPoint() - self.pos()
            self.dragging = True

    def mouseMoveEvent(self, event):
        if self.dragging:
            # 根据当前鼠标位置计算窗口新位置
            new_pos = event.globalPosition().toPoint() - self.offset
            self.move(new_pos)

    def mouseReleaseEvent(self, event):
        self.dragging = False

    #双击最大化/恢复
    def mouseDoubleClickEvent(self, event):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def top(self):
        """窗口一直置顶，即使切换应用也还是置顶"""
        self.Free_my_WW_win.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)




if __name__ == '__main__':
    Free_my_WW = WinShow("./边框重写.py")   # 创建实例对象

    class DraggableWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()
            self.dragging = False  # 初始状态修正
            self.offset = QPoint()  # 更明确的变量名

        def initUI(self):
            self.resize(400, 300)
            self.setWindowTitle('Professional Draggable Window')
            self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
            # 建议添加窗口阴影
            self.setStyleSheet("""
                background: white;
                border: 1px solid #cccccc;
                border-radius: 4px;
            """)




    # if __name__ == '__main__':
    #     app = QApplication(sys.argv)
    #     window = DraggableWindow()
    #     window.show()
    #     sys.exit(app.exec())

