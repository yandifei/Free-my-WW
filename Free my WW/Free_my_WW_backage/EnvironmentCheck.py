# 这个库是用来检测环境的
import time

pass
"""
硬件状态检查：
1. 检测电脑的分辨率和缩放
2. 检查 CPU、内存、磁盘空间(暂时没写)
3. 检查外设（暂时没写）
软件状态检查：
1. 检测自己写的/脚本/程序/软件是否是最新的(暂时没写)
2. 检测完整性，这个我觉得也有必要(暂时没写)
3. 检查操作系统
4. 检查脚本所需的软件/游戏是否存在。(暂时没写)
5. 检测软件/游戏的版本。(暂时没写)
6. 网络状态检查：(暂时没写，都能开有游戏了，有必要检测网络？)
"""
# 导包
import os   # 路径包
import  sys # 系统包
from ctypes import windll # 内置的库，不用下载（用来调用c语言的动态链接库）
# 自己的包
from UserFeedback import UserFeedback # 用户反馈


#创建检测的类
class EnvironmentCheck:
    def __init__(self):
        super().__init__()
        self.check_screen_resolution()  # 检测屏幕分辨率


    def check_screen_resolution(self):
        """检测屏幕分辨率是否符合1920X1080 """
        get_screen_resolution() # 调用获得屏幕的分辨率和缩放的函数




def get_screen_resolution():
    """获得屏幕的分辨率和缩放
    使用ctypes内置的库调用windll.user32的动态链接库来获得屏幕的分辨率和缩放
    返回值
    屏幕x的分辨率:screen_x
    屏幕y的分辨率:screen_y
    """
    win32_dll = windll.user32  # 调用win32的动态链接库
    screen_x, screen_y = win32_dll.GetSystemMetrics()  # 获得当前屏幕的分辨率
    return screen_x, screen_y


# def get_scaling_factor():
#     # 获取缩放比例
#     user32 = windll.user32
#     hdc = user32.GetDC(0)
#     print(hdc)
#     scale_factor = windll.gdi32.GetDeviceCaps(hdc, 118)  # 118 是 LOGPIXELSX
#     user32.ReleaseDC(0, hdc)
#     return scale_factor / 96  # 96 是 100% 缩放时的 DPI



if __name__ == '__main__':
    UserFeedback.sys_feedback()