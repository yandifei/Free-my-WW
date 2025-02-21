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
# ui模块
import Free_my_WW_UI.images.Free_my_WW_QRC  # 导入qrc转换py的文件
# from UI_connect import *              # 界面连接

from Free_my_WW_package.FileOperations import *
sys.path.append(f"{os.getcwd()}\\Free_my_WW_package")    # 从当前目录下加路径（其实这里加不加无所谓）
Free_my_WW_app = QApplication(sys.argv)  # 管理控制事件流和设置
Free_my_WW = FramelessWindow(f"{os.getcwd()}/Free_my_WW_UI/Free_my_WW_UI.ui",15,(220,30))  # 创建实例对象
Free_my_WW.show()  # 展示窗口(在未初始化 GUI 前调用 show()	窗口可能无法正确渲染)
sys.exit(Free_my_WW_app.exec())  # 安全退出界面任务

