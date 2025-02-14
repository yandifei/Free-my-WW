"""不要把QApplication和show写进去自定义的类里面去，
QApplication是只能有一个的，创建2个对象就完了
show如果是在自定义类之后则有可能出现未知bug
在未初始化 GUI 前调用 show()	窗口可能无法正确渲染
将Form对象的窗口布局器（1个）的类名设置为GlobalLayout，意为全局布局器
"""

# 去掉原来的边框，直接重写
# 导包
""" 添加路径导入自定义包
import os # 用来导入自定义包的
sys.path.append(os.getcwd())   # 添加路径到系统路径里面
package_path = f"{os.getcwd()}\\Free_my_WW_package"   # 当前目录下找包
sys.path.append(package_path)   # 添加路径到系统路径里面
package_path = os.path.dirname(package_path)   # 获取上级目录
sys.path.append(package_path)   # 添加路径到系统路径里面
print(f"{os.getcwd()}\\Free_my_WW_package")
"""
import sys

sys.path.append("D:\鸣潮脚本\Free-my-WW\Free my WW\Free_my_WW_package")  # 添加路径到系统路径里面

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt, QPoint  # Qt用来干掉边框
from PyQt6 import uic
# 自己的包
from Free_my_WW_package.SysInformation import *
from Free_my_WW_package.UserFeedback import *
from Free_my_WW_package.SysControl import limit_cursor, release_cursor

try:
    from 边框重写 import *
except ImportError:
    raise ImportError("没有导入后缀ui的文件")


class WinInit(QWidget):
    """窗口初始化（当前主显示器屏幕中央）
    这个窗口经过了处理，去掉了标题栏（因此最大化、最小化、关闭、拖拽都没了）
    参数：
    ui_file_path ： ui文件路径，可以是ui转py的文件
    edge_size ： 设置边缘大小，默认为15像素点
    win_control_button_size : 元组，全部窗口控制按钮放在一起后的宽度（x）高度（y）
    """
    def __init__(self, ui_file_path, edge_size=15,win_control_button_size = (220,30)):
        super().__init__()  # 习惯
        self.ui_file_path = ui_file_path  # ui文件路径，后缀名不一定是.ui，转为py也可以
        self.ui = None  # 为了后面创建实例对象用的
        self.import_ui()  # 创建ui对象，导入ui
        self.current_screen_xy = get_screen_resolution()  # 外部获得屏幕分辨率（影响screen_half和move_center_win）
        self.delete_title_bar()  # 重写标题栏
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # 去掉背景，为了之后的圆角重写
        append_style = self.styleSheet() + """
            QWidget {
            border-radius: 5px;
            background: #f0f0f0;  /* 窗口背景色 */
        }
        """  # 追加的样式内容
        self.setStyleSheet(append_style)  # 追加样式
        self.screen_half = int(self.current_screen_xy[0] / 2), int(self.current_screen_xy[1] / 2)  # 可用一半的屏幕（影响move_center_win）
        self.move_center_win()  # 确保窗口在屏幕中央,这个位置不能换到分辨率初始化前
        self.last_geometry = self.geometry()  # 记录上一次的位置和大小
        self.init_win_width = self.width()  # 记录最开始默认的窗口长度（后续记录用户拉条缩放改变的大小）
        self.init_win_height = self.height()  # 记录最开始默认的窗口高度（后续记录用户拉条缩放改变的大小）
        self.mouse_max_x = self.current_screen_xy[4] - 1  # 鼠标最大x位置
        self.mouse_max_y = self.current_screen_xy[5] - 1  # 鼠标最大y位置
        self.offset = QPoint()  # 获取鼠标移动的像素点，offset（消耗）
        self.edge_directions = None  # 用来记录窗口边缘的方向（'left', 'right', 'top', 'bottom', 'top-left'）
        self.dragging = False  # 初始窗口拖拽为关闭（开启的话会导致鼠标不点击也能拖拽）
        self.snap_layouts = False  # 用来记录窗口贴边功能是否开启
        # self.setMouseTracking(True)  # 启用鼠标追踪(默认关闭，用来监测鼠标是否在边缘的)
        """拖拽缩放重写"""
        self.win_control_button_size = win_control_button_size  # 记录窗口控制全部按钮的大小，用来避免在该区域打开拉伸缩放
        self.edge_size = edge_size  # 默认15个像素点为边缘
        self.resizing = False, None   # 禁止鼠标拖动窗口边缘或角落来调整窗口大小（默认关闭）,没有存放任何缩放策略

    def import_ui(self):
        """判断ui是ui文件还是ui转py文件"""
        if ".ui" in self.ui_file_path:  # 判断是否为ui文件
            uic.loadUi(self.ui_file_path, self)  # 创建ui窗口对象(实例)
        elif ".py" in self.ui_file_path:  # 判断是否为py文件
            pass  # 这里以后改进，在自己录下遍历ui转py的文件，并加入系统路径，然后通过分析用户给的路径分割包名导入
            """这里爆红不用管，因为没有导入ui转py文件，这里找不到Ui_Form的类"""
            try:  # 如果改进了这个异常处理也可以删了
                self.ui = Ui_Form()  # 创建UI实例，为了后续控件的调用
                self.ui.setupUi(self)  # 继承界面的类
            except(SyntaxError, NameError):
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
        sys_feedback(f"主显示器的逻辑分辨率: {self.current_screen_xy[0]}X{self.current_screen_xy[1]}")  # 打印当前屏幕的分辨率吧
        sys_feedback(f"主显示器屏幕的中心坐标:{self.screen_half[0]},{self.screen_half[1]}")  # 打印当前屏幕中心
        move_x = int(self.screen_half[0] - (self.width() / 2))
        move_y = int(self.screen_half[1] - (self.height() / 2))
        progress_feedback(f"Free my WW 移动坐标：{move_x},{move_y}")
        self.move(move_x, move_y)  # 把窗口移动到屏幕正中央

    def delete_title_bar(self):
        """去掉了标题栏（顺带去掉了拖拽，窗口就一直置顶无法关闭）"""
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

    def top(self):
        """窗口一直置顶，即使切换应用也还是置顶"""
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

    def window_mouse_pass_through(self):
        """主窗口鼠标穿透"""
        self.setWindowFlag(Qt.WindowType.WindowTransparentForInput)  # 窗口输入穿透

    def mousePressEvent(self, event):
        """重写鼠标事件（在按下鼠标开启拖拽功能并记录鼠标偏移量），限制光标"""
        if event.button() == Qt.MouseButton.LeftButton: # 确保是鼠标左键按下的
            if self.resizing[0]:    # 启动鼠标边缘缩放

            limit_cursor(report=False)  # 调用函数对光标范围进行限制（防止窗口过度滑到任务栏下面）
            # 记录鼠标全局位置与窗口位置的偏移量（不要把event.position()弄进去，如果开了全局监测就凉了）
            self.offset = event.globalPosition().toPoint() - self.pos()
            # print(f"鼠标相对窗口的坐标：{self.offset}，敏感|窗口内的相对坐标{event.position()},浮点数")
            # print(f"鼠标在屏幕上的位置:{event.globalPosition().toPoint()}")  # 这个就是鼠标在屏幕上的位置
            # print(f"窗口坐标:{self.pos()}")
            self.dragging = True

    def mouseMoveEvent(self, event):
        # 点击一次就扩大位置
        # if event.button() == Qt.MouseButton.RightButton:
        # self.setGeometry(self.geometry().x(), self.geometry().y(), self.init_win_width + 10,
        #                  self.init_win_height + 10)
        # self.init_win_width = self.width()  # 更新初始窗口大小
        # self.init_win_height = self.height()  # 更新初始窗口大小
        # self.setGeometry(self.geometry().x() - 10, self.geometry().y() - 10, self.init_win_width + 10,
        #                  self.init_win_height + 10)
        # self.init_win_width = self.width()  # 更新初始窗口大小
        # self.init_win_height = self.height()  # 更新初始窗口大小
        """根据当前鼠标位置计算窗口新位置"""
        mouse_current_x = event.globalPosition().toPoint().x()  # 刷新鼠标x位置，仅对这个函数有效，别的未测试
        mouse_current_y = event.globalPosition().toPoint().y()  # 刷新鼠标y位置，仅对这个函数有效，别的未测试
        # 如果当前鼠标位置低于任务栏则
        if self.snap_layouts and self.dragging:  # 检测是否开启了窗口贴边功能，一定要判断拖拽，因为开启了全局拖拽
            self.resize(self.init_win_width,self.init_win_height)
            self.move(mouse_current_x - int(self.width() / 2), mouse_current_y - 16)   # 窗口回到鼠标处
            self.snap_layouts = False  # 还原窗口，标志还原
            self.offset = event.globalPosition().toPoint() - self.pos()  # 重新记录上次的鼠标位置
        elif self.dragging:  # 启动拖拽
            self.move(event.globalPosition().toPoint() - self.offset)
        self.last_geometry = self.geometry()  # 记录上一次的位置和大小
        # 窗口边缘缩放
        # print(f"鼠标在窗口内的相对坐标{event.position().x(), event.position().y()}")
        # print(f"{self.init_win_width - self.win_control_button_size[0],self.win_control_button_size[1]}")
        if (event.position().x() >= (self.init_win_width - self.win_control_button_size[0]) and
                event.position().y() <= self.win_control_button_size[1]):  # 判断禁止在窗口控件区域启动缩放
            print(f"到达禁止区域")
            self.resizing = False, 0  # 禁止鼠标拖动窗口边缘或角落来调整窗口大小（默认关闭）,存放 0 代表禁止区域
            self.setCursor(Qt.CursorShape.ArrowCursor)  # 保持光标（把缩放的光标改回默认）
        # 左上角
        elif event.position().x() <= self.edge_size and event.position().y() <= self.edge_size:
            print("左上角")
            self.setCursor(Qt.CursorShape.SizeFDiagCursor)  # 左上
        # 右上角
        elif event.position().x() >= (self.init_win_width - self.edge_size) and event.position().y() <= self.edge_size:
            print("右上角")
            self.setCursor(Qt.CursorShape.SizeBDiagCursor)  # 右上
        # 右下角
        elif event.position().x() >= (self.init_win_width - self.edge_size) and event.position().y() >= (self.init_win_height - self.edge_size):
            print("右下角")
            self.setCursor(Qt.CursorShape.SizeFDiagCursor)  # 右下
        # 左下角
        elif event.position().x() <= self.edge_size and event.position().y() >= (self.init_win_height - self.edge_size):
            print("左下角")
            self.setCursor(Qt.CursorShape.SizeBDiagCursor)  # 左下
        elif event.position().x() <= self.edge_size:  # 左边边缘判定（小于等于默认的15个像素点）
            print("在左边缘")
            self.resizing = True, 1  # 禁止鼠标拖动窗口边缘或角落来调整窗口大小（默认关闭）,存放 1 代表在左边缘
            self.setCursor(Qt.CursorShape.SizeHorCursor)  # 左
        elif event.position().y() <= self.edge_size:
            print("在上边缘")
            self.resizing = True, 2  # 禁止鼠标拖动窗口边缘或角落来调整窗口大小（默认关闭）,存放 2 代表在上边缘
            self.setCursor(Qt.CursorShape.SizeVerCursor)  # 下
        elif event.position().x() >= (self.init_win_width - self.edge_size):
            print("在右边缘")
            self.setCursor(Qt.CursorShape.SizeHorCursor)  # 右
            self.resizing = True, 3  # 禁止鼠标拖动窗口边缘或角落来调整窗口大小（默认关闭）,存放 3 代表在右边缘
        elif event.position().y() >= (self.init_win_height - self.edge_size):
            print("在下边缘")
            self.setCursor(Qt.CursorShape.SizeVerCursor)  # 下
            self.resizing = True, 4  # 禁止鼠标拖动窗口边缘或角落来调整窗口大小（默认关闭）,存放 4 代表在下边缘
        else:
            self.setCursor(Qt.CursorShape.ArrowCursor)  # 默认光标
            self.resizing = False, None   # 设为关闭，禁止鼠标拖动窗口边缘或角落来调整窗口大小,没有任何缩放策略

    def mouseReleaseEvent(self, event):
        """鼠标松开，停止拖拽，解除光标限制"""
        if event.button() == Qt.MouseButton.LeftButton:    # 判断是不是鼠标左键松开才触发的
            self.dragging = False
            release_cursor(False)  # 调用函数对光标范围的限制（可以穿过任务栏）
        """窗口贴边功能,下面的顺序绝对不能乱，如果让上角最大化会导致左上角的失效"""
        # 鼠标在最左上角
        if event.globalPosition().toPoint().x() == 0 and event.globalPosition().toPoint().y() == 0:
            self.setGeometry(0, 0, self.screen_half[0], self.screen_half[1])
            self.snap_layouts = True  # 标志开启了窗口贴边功能
        # 鼠标在最右上角
        elif event.globalPosition().toPoint().x() == self.mouse_max_x and event.globalPosition().toPoint().y() == 0:
            self.setGeometry(self.screen_half[0], 0, self.screen_half[0], self.screen_half[1])
            self.snap_layouts = True  # 标志开启了窗口贴边功能
        # 鼠标在最右下角
        elif event.globalPosition().toPoint().x() == 0 and event.globalPosition().toPoint().y() == self.mouse_max_y:
            self.setGeometry(0, self.screen_half[1], self.screen_half[0], self.screen_half[1])
            self.snap_layouts = True  # 标志开启了窗口贴边功能
        # 鼠标在最左下角
        elif event.globalPosition().toPoint().x() == self.mouse_max_x and event.globalPosition().toPoint().y() == self.mouse_max_y:
            self.setGeometry(self.screen_half[0], self.screen_half[1], self.screen_half[0], self.screen_half[1])
            self.snap_layouts = True  # 标志开启了窗口贴边功能
        # 鼠标在顶层
        elif event.globalPosition().toPoint().y() == 0:
            self.showMaximized()  # 窗口最大化
            self.snap_layouts = True  # 标志开启了窗口贴边功能
        # 鼠标在最左边
        elif event.globalPosition().toPoint().x() == 0:
            self.setGeometry(0, 0, self.screen_half[0], self.current_screen_xy[1])  # 窗口为一半移动到左上角
            self.snap_layouts = True  # 标志开启了窗口贴边功能
        # 鼠标在最右边
        elif event.globalPosition().toPoint().x() == self.mouse_max_x:
            self.setGeometry(self.screen_half[0], 0, self.screen_half[0], self.current_screen_xy[1])  # 窗口为一半移动到右上角
            self.snap_layouts = True  # 标志开启了窗口贴边功能
        # 鼠标在最底层
        elif event.globalPosition().toPoint().y() == self.mouse_max_y:
            self.resize(self.init_win_width, self.init_win_height)  # 回到最开始的宽度和高度
            self.move_center_win()  # 把窗口移动到屏幕中央
            # 这里就没有必要加窗口贴边开启的标志了，因为这是还原

    def mouseDoubleClickEvent(self, event):
        """双击最大化/恢复"""
        if event.button() == Qt.MouseButton.LeftButton:   # 判断是不是鼠标左键双击的
            if self.snap_layouts:  # 已经开启最大化，要变为开始大样子
                # 回复原来的位置，但是宽度和高度是初始的和自己定义的
                self.setGeometry(self.last_geometry.x(),self.last_geometry.y(),self.init_win_width,self.init_win_height)
                self.snap_layouts = False
            elif not self.snap_layouts:  # 未开启最大化，要变为最大化
                self.showMaximized()  # 最大化
                self.snap_layouts = True  # 标志开启了窗口贴边功能


if __name__ == '__main__':
    Free_my_WW_app = QApplication(sys.argv)  # 管理控制事件流和设置
    # Free_my_WW_app.setAttribute(Qt.ApplicationAttribute.AA_UseDesktopOpenGL)    # OpenGL加速（图形渲染增强）
    """Free_my_WW_app.setAttribute(Qt.ApplicationAttribute.AA_MouseTracking, True)对每个继承widget的控件都打开鼠标表跟踪"""
    Free_my_WW = WinInit("./边框重写.py")  # 创建实例对象

    # Free_my_WW.window_mouse_pass_through()  # 主窗口鼠标穿透
    # Free_my_WW.top()    # 窗口一直置顶，即使切换应用也还是置顶


    Free_my_WW.show()  # 展示窗口(在未初始化 GUI 前调用 show()	窗口可能无法正确渲染)
    """
    Free_my_WW.window_background_transparency()  # 主窗口背景透明
    def window_background_transparency(self):
        ""窗口背景透明(最顶层的窗口已经背景透明，这个窗口是自己建立的)""
        self.ui.GlobalWidget.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # 窗口透明
    """
    sys.exit(Free_my_WW_app.exec())  # 安全退出界面任务
