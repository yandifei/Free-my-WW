# 这个库是用来检测环境的
"""
硬件状态检查：
1. 检查 CPU、内存、磁盘空间(暂时没写)
2. 检查外设（暂时没写）
软件状态检查：
1. 检测电脑的分辨率和缩放
2. 检测自己写的/脚本/程序/软件是否是最新的(暂时没写)
3. 检测完整性，这个我觉得也有必要(暂时没写)
4. 检查操作系统
5. 检查脚本所需的软件/游戏是否存在。(暂时没写)
6. 检测软件/游戏的版本。(暂时没写)
7. 网络状态检查：(暂时没写，都能开有游戏了，有必要检测网络？)
"""
# 导包
import sys  # 系统包
# win32api（提供系统接口）、win32gui（图形界面操作）、win32print（打印和设备上下文相关功能）
import win32con, win32api, win32gui, win32print

# 自己的包
from UserFeedback import *  # 用户反馈

def get_operating_system():
    """
    获得当前是什么操作系统
    返回值： operating_system
    不会返回“不知道”、“空”、“假”的值，基于操作系统的标识符返回的
    如果系统完全未知或未被 Python 支持，返回值可能由底层 C 库的 uname 或其他系统调用决定，例如返回操作系统内核的名称
    """
    operating_system = sys.platform     # 使用sys的库来获得当前操作系统
    if operating_system == "win32":
        operating_system = "Windows"
    if operating_system == "linux":
        operating_system = "Linux"
    if operating_system == "darwin":
        operating_system = "macOS"
    if operating_system == "cygwin":
        operating_system = "Cygwin"
    if operating_system == "aix":
        operating_system = "IBM AIX"
    if operating_system == "freebsd":
        operating_system = "FreeBSD"
    return operating_system

def get_screen_resolution():
    """获得主显示器屏幕的当前分辨率和实际分辨率
    当前的分辨率是经过缩放后的，鼠标最大位置受限当前分辨率。实际实际分辨率是缩放的100%的分辨率
    返回值
    screen_x : 屏幕x的当前分辨率
    screen_y : 屏幕y的当前分辨率
    real_screen_x : 屏幕x的实际分辨率
    real_screen_y : 屏幕y的实际分辨率
    HDC : 桌面窗口的设备上下文句柄
    """
    screen_x = win32api.GetSystemMetrics(0)  # 获取当前水平分辨率（缩放后的水平分辨率）
    screen_y = win32api.GetSystemMetrics(1)  # 获取当前垂直分辨率（缩放后的垂直分辨率）
    # 获取真实的分辨率（1.先获取桌面窗口设备上下文的句柄。2.使用GetDeviceCaps获得真实分辨率。3.释放句柄）
    HDC = win32gui.GetDC(0)  # 获取桌面窗口的设备上下文（Device Context, DC）。0 表示桌面窗口的句柄
    if not HDC:
        raise WindowsError("未能成功获取桌面窗口的设备上下文的句柄")
    try:
        real_screen_x = win32print.GetDeviceCaps(HDC, win32con.DESKTOPHORZRES)  # 使用 GetDeviceCaps 查询设备的水平物理分辨率
        real_screen_y = win32print.GetDeviceCaps(HDC, win32con.DESKTOPVERTRES)  # 查询设备的垂直物理分辨率
    except():
        raise WindowsError("未能成功获取主显示器的真实分辨率")
    finally:
        win32gui.ReleaseDC(0, HDC)
    return screen_x, screen_y, real_screen_x, real_screen_y, HDC

def get_scaling_factor():
    """获得主显示器的缩放比例
    返回值：正常来说任意一个都是都是当前屏幕的缩放百分比
    水平缩放百分比：scaling_factor_x（百分数整型）
    垂直缩放百分比：scaling_factor_y（百分数整型）
    """
    screen_resolution = get_screen_resolution() # 调用函数获得屏幕真实和当前分辨率
    # 计算缩放比例（物理宽 / 缩放宽），四舍五入保留两位小数（如 1.5 表示 150% 缩放）。
    scaling_factor_x = round(screen_resolution[2]/screen_resolution[0], 2)
    scaling_factor_y = round(screen_resolution[3] / screen_resolution[1], 2)
    scaling_factor_x = int(scaling_factor_x * 100) # 转换为百分制整型
    scaling_factor_y = int(scaling_factor_y * 100)  # 转换为百分制整型
    return scaling_factor_x, scaling_factor_y

class EnvironmentCheck:
    """检测环境的类
    硬件状态检查：
    1. 检查 CPU、内存、磁盘空间(暂时没写)
    2. 检查外设（暂时没写）
    软件状态检查：
    1. 检测电脑的分辨率和缩放
    2. 检测自己写的/脚本/程序/软件是否是最新的(暂时没写)
    3. 检测完整性，这个我觉得也有必要(暂时没写)
    4. 检查操作系统
    5. 检查脚本所需的软件/游戏是否存在。(暂时没写)
    6. 检测软件/游戏的版本。(暂时没写)
    7. 网络状态检查：(暂时没写，都能开有游戏了，有必要检测网络？)
    """
    def __init__(self, check_all=False):
        """一条龙检测电脑环境
        参数为True时启动一条龙检测，否则就不执行任何操作，用户自己调用检测吧
        参数：check_all
        """
        super().__init__()
        self.check_all = check_all  # 检测全部的标志
        if self.check_all:  # 开始逐条检测需要的环境条件
            pass # 检查CPU、内存、磁盘空间(暂时没写)
            pass # 检查外设（暂时没写）软件状态检查
            self.check_operating_system()  # 检查操作系统
            self.check_screen_resolution()  # 检测屏幕分辨率（检测电脑的分辨率和缩放，上）
            self.check__scaling_factor()    # 检测显示器缩放（检测电脑的分辨率和缩放，下）
            pass # 检测自己写的 / 脚本 / 程序 / 软件是否是最新的(暂时没写)
            pass # 检测完整性，这个我觉得也有必要(暂时没写)
            pass # 检查脚本所需的软件 / 游戏是否存在。(暂时没写)
            pass # 检测软件 / 游戏的版本。(暂时没写)
            pass # 网络状态检查：(暂时没写，都能开有游戏了，有必要检测网络？)

    @staticmethod
    def check_operating_system():
        operating_system = get_operating_system()
        sys_feedback(f"您电脑的操作系统或标识符:{operating_system}")
        if operating_system == "Windows":
            progress_feedback("电脑操作系统符合要求")
        else:
            raise OSError(f"检测到操作系统为{operating_system}，请在操作系统为Windows的电脑上使用脚本")

    @staticmethod
    def check_screen_resolution():
        """检测主显示器物理分辨率是否符合1920X1080
        物理分辨率是没有经过缩放处理的，缩放100%的
        逻辑分辨率是经过缩放后的即当前主显示器的屏幕分辨率，对着自己屏幕的你看的就是逻辑分辨率
        """
        # 调用获得主显示器物理分辨率的函数（大众用物理分辨率交流的）
        screen_resolution = get_screen_resolution()
        sys_feedback(f"桌面窗口的设备上下文句柄：{screen_resolution[4]}")
        # 调用反馈函数（特别强调这里的是物理分辨率）
        sys_feedback(f"主显示器的分辨率：{screen_resolution[2]}X{screen_resolution[3]}")
        # 判断
        if screen_resolution[2] == 1920 and screen_resolution[3] == 1080:
            progress_feedback("当前屏幕分辨率符合要求")
        else:
            raise ValueError(f"当前分辨率：{screen_resolution[2]}X{screen_resolution[3]}，请在电脑设置中将分辨率调至1920X1080")

    @staticmethod
    def check__scaling_factor():
        """
        检查当前屏幕缩放是否是100%
        """
        scaling_factor = get_scaling_factor()   # 调用函数获得缩放
        if scaling_factor[0] is not scaling_factor[1]:
            raise Warning(f"水平与垂直的缩放比例不同，水平缩放比例：{scaling_factor[0]}，垂直缩放比例：{scaling_factor[1]}")
        sys_feedback(f"当前屏幕缩放：{scaling_factor[0]}%")    # 获取失败已经在函数里处理，这里没有必要了
        if scaling_factor[0] == 100:
            progress_feedback("当前屏幕缩放符合要求")
        else:
            raise RuntimeError(f"当前屏幕缩放：{scaling_factor[0]}%，需要缩放的是100%，请调整后重启电脑")

if __name__ == '__main__':
    get_operating_system()
    get_screen_resolution()
    get_scaling_factor()

    environment_check = EnvironmentCheck(True)
