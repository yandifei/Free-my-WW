# 主要（main）文件
# 导包
# 自带的包
import os
import sys
import sys
# 第三方模块
from PyQt6.QtWidgets import QApplication
# 自己写的包
from Free_my_WW_package.UserFeedback import *           # 用户反馈
from Free_my_WW_package.EnvironmentCheck import *       # 环境检测
from Free_my_WW_package.SysInformation import *         # 系统信息
from Free_my_WW_package.SysControl import  *            # 系统控制
from Free_my_WW_package.frameless_window import *       # 去标题栏
from Free_my_WW_package.UI_design import *              # 界面连接



sys_feedback(f"当前目录下的文件有{os.listdir()}")  # 查看当前目录下的文件
sys.path.append(f"{os.getcwd()}+Free_my_WW_package")    # 从当前目录下加路径（其实这里加不加无所谓）
sys_feedback(1)
#
#
# Free_my_WW_app = QApplication(sys.argv)  # 管理控制事件流和设置
# # Free_my_WW_app.setAttribute(Qt.ApplicationAttribute.AA_UseDesktopOpenGL)    # OpenGL加速（图形渲染增强）
# """Free_my_WW_app.setAttribute(Qt.ApplicationAttribute.AA_MouseTracking, True)对每个继承widget的控件都打开鼠标表跟踪"""
# Free_my_WW = WinInit("./测试.ui")  # 创建实例对象
#
# # Free_my_WW.window_mouse_pass_through()  # 主窗口鼠标穿透
# # Free_my_WW.top()    # 窗口一直置顶，即使切换应用也还是置顶
#
#
# Free_my_WW.show()  # 展示窗口(在未初始化 GUI 前调用 show()	窗口可能无法正确渲染)
# """
# Free_my_WW.window_background_transparency()  # 主窗口背景透明
# def window_background_transparency(self):
#     ""窗口背景透明(最顶层的窗口已经背景透明，这个窗口是自己建立的)""
#     self.ui.GlobalWidget.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # 窗口透明
# """
# sys.exit(Free_my_WW_app.exec())  # 安全退出界面任务