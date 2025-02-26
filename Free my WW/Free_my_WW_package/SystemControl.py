# 这个库是用来获取系统信息（windows）的
# 导包
import os
import sys  # 系统包
import platform # 访问底层平台的标识数据
# win32api（提供系统接口）、win32gui（图形界面操作）、win32print（打印和设备上下文相关功能）
import win32con, win32api, win32gui, win32print
# 自己的包
from Free_my_WW_package.UserFeedback import *  # 用户反馈

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

def get_login_name():
    """获得控制终端的用户名
    返回值：返回通过控制终端进程进行登录的用户名
    """
    return os.getlogin()

def get_process_id(father=False):
    """获得当前的进程ID或父进程ID
    参数：father，默认False，如果为true则返回父进程
    返回值：默认返回当前进程ID，如果参数为true则返回父进程ID
    """
    if father:
        return os.getppid()
    else:
        return os.getpid()

def change_environment_value(key, value,mod=False):
    """修改或删除环境变量，我修改了但是设置里面没变
    参数（都是字符串）mod为True是填好key就行：
    key ：需要添加的环境变量
    value ：环境变量的值
    mod : 默认为False，添加环境变量，为True是删除环境变量
    """
    if mod:
        os.unsetenv(key)
    else:
        os.putenv(key, value)

def error(code):
    """参数code是自定义的错误代码
    error_code = 2
    message = os.strerror(error_code)
    print(f"错误码 {error_code}: {message}")
    # 输出：错误码 2: No such file or directory
    """
    os.strerror(code)
    pass    # 以后再搞，把报错全变成对应的错误代码和中文错误信息

def get_computer_type():
    """获得计算机的类型
    返回值：如：'AMD64' 。 如果该类型无法确定则会返回无法确定该类型。
    """
    if platform.machine():
        return platform.machine()
    else:
        return "无法确定该类型"

def get_system_information():
    """获得系统信息
    返回一个标识底层平台的字符串，其中带有尽可能多的有用信息。
    """
    return platform.platform()

def get_hostname():
    """获得主机名称（）
        返回计算机的主机名称（即网络名称,可能不是完整限定名称！）。 如果该值无法确定则会返回一个空字符串。
    """
    return platform.node()

def get_cup_name():
    """获得真实处理器的名称
    返回（真实的）处理器名称，例如 'Intel64'。
    如果该值无法确定则将返回“无法获得真实的处理器名称”。
    """
    if platform.processor():
        return platform.processor()
    else:
        return "无法获得真实的处理器名称"

def get_python_version():
    """获取python的版本"""
    return platform.python_version()

def get_screen_resolution():
    """获得主显示器屏幕的当前分辨率、实际分辨率、可用分辨率、桌面窗口的设备上下文句柄
    当前的分辨率是经过缩放后的，鼠标最大位置受限当前分辨率。实际实际分辨率是缩放的100%的分辨率
    返回值
    screen_x : 屏幕x的当前分辨率
    screen_y : 屏幕y的当前分辨率
    real_screen_x : 屏幕x的实际分辨率
    real_screen_y : 屏幕y的实际分辨率
    available_screen_x : 屏幕x的可用分辨率（不包括菜单栏）
    available_screen_y : 屏幕y的可用分辨率（不包括菜单栏）
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
    # 获得主显示器的可用分辨率（使用win32api.GetMonitorInfo函数获取当前主显示器的信息）
    # win32con.MONITOR_DEFAULTTOPRIMARY表示获取主显示器，这里0表示获取与窗口关联的显示器
    monitor_info = win32api.GetMonitorInfo(win32api.MonitorFromWindow(0, win32con.MONITOR_DEFAULTTOPRIMARY))
    # "Work"键的值是一个包含四个整数的元组，表示工作区的坐标：(left, top, right, bottom)
    available_screen_x = monitor_info["Work"][2] - monitor_info["Work"][0]  # 右边界减左边界
    available_screen_y = monitor_info["Work"][3] - monitor_info["Work"][1]  # 下边界减上边界
    return screen_x, screen_y, real_screen_x, real_screen_y, available_screen_x, available_screen_y, HDC

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

def get_cpu_count():
    """获得系统中逻辑CPU的数量
    返回值：
    如果无法获取则为"无法确定"，否则为数字
    """
    cpu_count = os.cpu_count()
    if cpu_count:
        return cpu_count
    else:
        return "无法确定"

def get_process_use_cup_count():
    """获取当前进程的调用方线程可以使用的逻辑 CPU 数量
    python:3.13
    返回值：
    如果无法获取则为"无法确定"，否则为数字，如果报错就有"无法调用该函数，python需要3.13"
    """
    try:
        process_cpu_count = os.process_cpu_count()
    except():
        return "无法调用该函数，python需要3.13"
    if process_cpu_count:
        return process_cpu_count
    else:
        return "无法确定"

def limit_cursor(left = 0, top = 0, right = get_screen_resolution()[4] , bottom = get_screen_resolution()[5], report = True):
    """鼠标光标范围限制（即使程序结束了，效果还在，但是切屏效果就没了）
    填入参数：左、上、右、下、report    (left, top, right, bottom，是否报告)
    默认参数是屏幕可用分辨率（不包括任务栏，算的是逻辑分辨率）
    """
    if report: status_feedback("开始对鼠标光标范围进行限制")
    limit = (left, top, right, bottom)  # 转换为元组类型
    if report: progress_feedback(f"限制范围:{limit}")
    win32api.ClipCursor(limit)
    if report: status_feedback("完成对鼠标光标范围进行限制")

def release_cursor(report = True):
    """解除鼠标光标的范围的限制（当前屏幕的逻辑分辨率）
    参数：report, 填真假，默认开启报告
    """
    if report: status_feedback("开始解除鼠标光标的范围的限制")
    current_mxa_screen_resolution = get_screen_resolution() # 获得屏幕缩放后最大的分辨率（包括任务栏）
    release = (0, 0, current_mxa_screen_resolution[0], current_mxa_screen_resolution[1])    # 转为元组类型
    if report: progress_feedback(f"解除限制范围:{0, 0, current_mxa_screen_resolution[0], current_mxa_screen_resolution[1]}")
    # 因为参数不能为None，否者报错，所以我改为了最适合当前屏幕分辨率的范围
    win32api.ClipCursor(release)
    if report: status_feedback("完成解除鼠标光标的范围的限制")

if __name__ == '__main__':
    print(get_operating_system())
    print(get_computer_type())
    print(get_hostname())
    print(get_screen_resolution())
    get_screen_resolution()
    get_scaling_factor()
    # change_environment_value("Test","1",True)
