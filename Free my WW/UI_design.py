# UI槽函数设计
"""用自己写的无边框自定义标题的框架
这里是设计UI功能的，对接槽函数
"""
# 导包
# 自带的包
# import os
# import sys

from PyQt6.QtGui import QIcon
# 第三方模块
from PyQt6.QtWidgets import QSystemTrayIcon, QSplashScreen
# 自己写的包
# from Free_my_WW_package.UserFeedback import *           # 用户反馈
# from Free_my_WW_package.EnvironmentCheck import *       # 环境检测
# from Free_my_WW_package.SysInformation import *         # 系统信息
# from Free_my_WW_package.SysControl import  *            # 系统控制
from Free_my_WW_package.frameless_window import *       # 去标题栏
# ui模块
import Free_my_WW_UI.images.Free_my_WW_QRC  # 导入qrc转换py的文件


class Free_my_WW_ui(FramelessWindow):
    def __init__(self, ui_file_path, edge_size=10,win_control_button_size = (0,0)):
        super().__init__(ui_file_path, edge_size, win_control_button_size)
        """+++++++++++++++++++++++++++++++++标题栏相关+++++++++++++++++++++++++++++++++++++++"""
        # self.show_or_hide = QShortcut(QKeySequence("Win+Esc"), self) # 设置快捷键
        # self.show_or_hide.connect(self.show_or_hide_win)  #
        # QResource.registerResource("D:\\鸣潮脚本\\Free-my-WW\\Free my WW\\Free_my_WW_UI\\images\\Free_my_WW_QRC.qrc")    # 注册资源文件
        self.ui.Close.clicked.connect(self.close_win)   # 关闭按钮
        self.ui.MaxOrRestore.clicked.connect(self.max_or_restore)    # 最大化和恢复
        self.ui.Min.clicked.connect(self.min_win)   # 窗口最小化
        # 系统托盘相关
        self.min_to_sys = QSystemTrayIcon(self)  # 创建系统托盘的对象
        self.min_to_sys.activated.connect(self.system_tray_function)    # 完善系统托盘的功能
        # self.min_to_sys.setToolTip("text")
        self.ui.SystemTray.clicked.connect(self.system_tray)    # 最小化到系统托盘
        self.ui.HideToWindow.clicked.connect(self.hide_win) # 窗口隐藏（不显示系统托盘，只能在任务管理器里面找到）
        # self.free_my_ww_hwnd = self.print_free_my_ww_hwnd()  # 获得并打印窗口句柄
        print(f"当前的窗口句柄:{int(self.winId())}")  # 获取整数句柄


        """++++++++++++++++++++++++++++++++++开始真正的主界面设计+++++++++++++++++++++++++++++++++++++++++++++++"""
        # append_style = self.styleSheet() + """
        #                 QWidget {
        #                 background: #0055ff;  /* 窗口背景色 */
        #             }
        #             """  # 追加的样式内容
        # self.setStyleSheet(append_style)  # 追加样式





    """---------------------------------标题栏相关函数----------------------------------------------"""
    def close_win(self):
        """关闭窗口"""
        self.close()
        QApplication.quit()  # 终止应用程序

    def max_or_restore(self):
        """最大化和恢复（抄之前的函数）"""
        if self.isMaximized():  # 已经开启最大化，要变为开始大样子
            # 回复屏幕中央，但是宽度和高度是初始的和自己定义的
            self.setGeometry(self.original_geometry)  # 回到原始的位置和大小
            self.snap_layouts = False
        elif not self.isMaximized():  # 未开启最大化，要变为最大化
            self.showMaximized()  # 最大化
            """最大化之后必须记得及时更新窗口大小"""
            self.snap_layouts = True  # 标志开启了窗口贴边功能

    def min_win(self):
        """最小化窗口"""
        self.showMinimized()

    def system_tray(self):
        """系统托盘（启动系统托盘的同时隐藏窗口）"""

        self.min_to_sys.setIcon(QIcon(f"{os.getcwd()}/Free_my_WW_UI/images/logo.png"))  # 设置系统托盘的图标
        self.hide()  # 隐藏窗口
        self.min_to_sys.show()  # 显示系统托盘

    def hide_win(self):
        """深度隐藏(放到后台里面去了)
        窗口隐藏（不显示系统托盘，只能在任务管理器里面找到）"""
        self.min_to_sys.hide()  # 隐藏窗口
        self.hide()

    def system_tray_function(self, signal):
        if signal == QSystemTrayIcon.ActivationReason.Trigger:  # 点击系统托盘
            # if self.isMinimized() or self.isMaximized():  # 处于最小化或最大化状态按托盘图标
            #     self.showNormal()   # 恢复窗口原来的状态
            # if self.isHidden():
            #     self.show() # 展示窗口（隐藏状态）
            pass  # 功能未添加太多
            self.showNormal()  # 恢复窗口原来的状态

    def show_or_hide_win(self):
        """通过快捷键隐藏或显示窗口"""
        self.min_to_sys.hide()  # 隐藏系统托盘
        if self.isHidden():  # 如果窗口是隐藏的则显示窗口
            self.show()
        else:
            self.hide()  # 隐藏窗口

    def window_background_transparency(self):
        """窗口背景透明(最顶层的窗口已经背景透明，这个窗口是自己建立的)"""
        self.ui.GlobalWidget.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # 窗口透明





if __name__ == '__main__':
    Free_my_WW_app = QApplication(sys.argv)  # 管理控制事件流和设置
    Free_my_WW = Free_my_WW_ui(f"{os.getcwd()}/Free_my_WW_UI/Free_my_WW_UI.py",4,(220,30))  # 创建实例对象
    # Free_my_WW.window_background_transparency()  # 主窗口背景透明
    Free_my_WW.show()  # 展示窗口(在未初始化 GUI 前调用 show()	窗口可能无法正确渲染)
    sys.exit(Free_my_WW_app.exec())  # 安全退出界面任务