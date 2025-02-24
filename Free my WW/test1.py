# import sys
#
# from PyQt6.QtCore import Qt
# from PyQt6.QtWidgets import QApplication, QWidget
#
#
# class Win(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowFlag(Qt.WindowType.FramelessWindowHint)   # 去掉标题栏
#         hwnd = int(self.winId())  # 转换为整数
#         print(hwnd)
#
# app =  QApplication(sys.argv)
# win = Win()
# win.show()
# sys.exit(app.exec())
# 获取当前样式
import win32con
import win32gui


def a(hwnd):
    # 获取当前样式
    current_style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
    # 移除可调整大小、最大化、最小化
    new_style = current_style & ~win32con.WS_THICKFRAME & ~win32con.WS_MAXIMIZEBOX & ~win32con.WS_MINIMIZEBOX
    # 应用新样式
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, new_style)
    # 强制窗口重绘
    """强制窗口重绘
    SWP_NOMOVE保持窗口当前位置不变，忽略 SetWindowPos 函数中传入的 x 和 y 坐标参数。
    SWP_NOSIZE保持窗口当前尺寸不变，忽略 SetWindowPos 函数中传入的 cx 和 cy（宽度和高度）参数。
    SWP_FRAMECHANGED强制窗口重新计算非客户区（Non-Client Area，如标题栏、边框等）
    """
    win32gui.SetWindowPos(
        hwnd,
        win32con.HWND_TOP,
        0, 0, 0, 0,
        win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_FRAMECHANGED
    )

a(264350)