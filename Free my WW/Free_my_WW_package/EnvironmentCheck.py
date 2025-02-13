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
# 自己的包
from UserFeedback import *  # 用户反馈
from SysInformation import *    # 获取系统信息

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
        sys_feedback(f"桌面窗口的设备上下文句柄：{screen_resolution[6]}")
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
    environment_check = EnvironmentCheck(True)