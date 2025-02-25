# 这个库是用来获取系统信息（windows）的
# 导包
import os
import sys  # 系统包
import platform # 访问底层平台的标识数据
# win32api（提供系统接口）、win32gui（图形界面操作）、win32print（打印和设备上下文相关功能）
import win32con, win32api, win32gui, win32print

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

"""窗口句柄相关的函数"""
# 查找信息类
def find_current_hwnd():
    """获取当前的句柄（当前的前台窗口句柄）"""
    return win32gui.GetForegroundWindow()

def find_hwnd(classname=None, title=None):
    """通过窗口类名或标题来获取窗口的句柄
    参数：(类名和标题可以只填一个)
    classname : 窗口类名
    title ： 窗口标题
    返回值：
    hwnd ： 窗口的句柄(则返回顶级窗口的句柄)
    如果未找到则返回None
    """
    hwnd = win32gui.FindWindow(classname, title)  # 类名和标题
    if not any((classname,title)):
        raise ValueError("标题和类名都没填，返回通常是桌面窗口或随机窗口")
    elif hwnd:    # 如果句柄存在
        return hwnd
    else:
        return None     # 未找到窗口句柄返回空

def find_all_child_hwnd(parent_hwnd):
    """通过父窗口查找所有的子窗口的句柄
    参数：
    parent_hwnd : 父窗口的句柄
    返回值：
    all_child_hwnd ： 所有子窗口的句柄，如果为空代表该父窗口没有子窗口
    """
    if not parent_hwnd: # 检查填入的父句柄是否有效,如果为空则是随机的父句柄
        raise ValueError("父窗口的句柄为空")
    all_child_hwnd = list()   # 创建一个列表来存储所有子窗口的句柄
    child_hwnd = 0  # 设置当前的子窗口句柄（如果为0则从第一个窗口查找）
    while True:     # 根据父窗口和所给的当前子窗口的句柄查找下一个子窗口句柄
        child_hwnd = win32gui.FindWindowEx(parent_hwnd, child_hwnd, None, None)
        if child_hwnd == 0:  # 如果返回为0则代表遍历完了
            break   # 跳出循环
        all_child_hwnd.append(child_hwnd)   # 每次循环都存储一个子句柄
    return all_child_hwnd

def find_parent_hwnd(child_hwnd):
    """通过子窗口的句柄获得父窗口的句柄
    参数：
    child_hwnd ： 子窗口的句柄
    返回值：
    父窗口的句柄，如果父窗口没有则返回None
    """
    if not child_hwnd:  # 检查填入的句柄是否有效
        raise ValueError("填入的父窗口句柄无效")
    parent_hwnd = win32gui.GetParent(child_hwnd)    # 获得父窗口的句柄
    if parent_hwnd: # 判断父窗口是否存在
        return parent_hwnd
    else:
        return None

def get_win_title(hwnd):
    """输入窗口句柄获得窗口的标题
    参数：
    hwnd ： 需要查找标题的窗口的句柄
    返回值：
    直接返回窗口的标题（有可能是空值）
    """
    if not hwnd:
        raise ValueError("输入的窗口句柄无效")
    return win32gui.GetWindowText(hwnd)

def get_win_classname(hwnd):
    """输入窗口句柄获得窗口的类名
    参数：
    hwnd ： 需要查找标题的窗口的句柄
    返回值：
    直接返回窗口的类名（有可能是空值）
    """
    if not hwnd:
        raise ValueError("输入的窗口句柄无效")
    return win32gui.GetClassName(hwnd)

def get_win_title_classname(hwnd):
    """通过句柄获得窗口的标题和类名
    参数：
    hwnd ： 窗口句柄
    返回值：
    窗口的标题
    窗口的类名（有可能是空值）
    """
    if not hwnd:
        raise ValueError("输入的窗口句柄无效")
    return win32gui.GetWindowText(hwnd), win32gui.GetClassName(hwnd)

def is_hwnd(hwnd):
    """判断窗口句柄是否有效
    参数：
    hwnd ： 需要判断的窗口句柄
    返回值：
    布尔值（True或False）
    """
    return bool(win32gui.IsWindow(hwnd))

def is_use_hwnd(hwnd):
    """输入句柄判断窗口否处于启用状态（即窗口可以接收用户输入）
    判断按钮是否可点击:在自动化操作中，点击某个按钮前需确认其是否处于可用状态。
    检测窗口禁用状态:某些窗口在特定条件下会被禁用（如安装程序中的“下一步”按钮在未勾选协议时禁用）。
    调试窗口权限问题:确认窗口是否因权限问题被系统禁用。
    参数：
    hwnd ： 需要判断的窗口句柄、
    返回值：
    布尔值（True或False）
    """
    if not hwnd:
        raise ValueError("输入的句柄无效")
    return bool(win32gui.IsWindowEnabled(hwnd))

def find_hwnd_ex(parent_hwnd,child_hwnd,classname=None, title=None):
    """指定父窗口的子窗口 中查找符合类名和窗口标题的子窗口句柄。常用于定位嵌套的控件（如按钮、输入框等）。
    参数(parent_hwnd和child_hwnd均为None，则该函数将搜索所有顶级窗口。)：
    parent_hwnd : 父窗口句柄（若为0，则从桌面窗口的子窗口开始查找）
    child_hwnd : 起始查找的子窗口句柄（传入0表示从第一个子窗口开始）
    classname : 子窗口的类名（字符串，可设为None）
    title ： 子窗口的标题（字符串，可设为None）
    返回值：
    hwnd ： 窗口的句柄(则返回顶级窗口的句柄)
    如果未找到则返回None
    """
    hwnd = win32gui.FindWindowEx(parent_hwnd,child_hwnd,classname,title)#标题和类名，其中一个参数可以为None
    if hwnd:    # 如果为空则返回0，我改写为None
        return None
    else:
        return hwnd

def mouse_find_hwnd(x,y):
    """坐标（鼠标坐标）获得窗口句柄（根据相对于屏幕窗口位置的坐标来获得顶层窗口句柄）
    参数：
    x ： 屏幕的横坐标
    y ： 屏幕的纵坐标
    """
    return win32gui.WindowFromPoint((x, y))

def mouse_fine_child_hwnd(x,y,parent_hwnd=None):
    """通过父窗口查找鼠标下子窗口的句柄
    参数：
    x ： 屏幕的横坐标
    y ： 屏幕的纵坐标
    parent_hwnd ： 父窗口的句柄，如果不填默认值为None，调用时自动获取当前鼠标的父窗口句柄
    """
    if not parent_hwnd:
        parent_hwnd = win32gui.WindowFromPoint((x, y))  # 获取当前鼠标的父窗口句柄
    return win32gui.ChildWindowFromPoint(parent_hwnd, (x, y))

def key_find_hwnd():
    """返回当前具有键盘输入焦点的控件的句柄（可能是子窗口或控件）
    返回的是窗口内部的 控件句柄（如输入框、按钮）。
    如果当前没有控件获得焦点（例如用户仅点击了窗口标题栏），可能返回 0。
    """
    return win32gui.GetFocus()

def get_win_size(hwnd):
    """通过窗口句柄获得窗口左上角和右下角在当前屏幕的坐标，并计算大小
    注意：绝大多数窗口会隐藏部分边框，所以这里获取的是最真实的坐标和大小
    参数：
    hwnd ： 需要查询的窗口句柄
    返回值：
    size ： 元组类型，窗口的左上角和右下角坐标
    height ： 窗口的高度
    width ： 窗口的宽度
    """
    try:
        size = win32gui.GetWindowRect(hwnd)
    except():
        raise ValueError("填入的窗口句柄无效")
    height = size[2] - size[0]
    width = size[3] - size[1]
    return size,height,width

def is_min(hwnd):
    """判断窗口是否是最小化(必须按最小化才能检测到最小化，我切窗口都不算,好鸡肋)
    参数：
    hwnd ： 需要判断的窗口句柄、
    返回值：
    布尔值（True或False）
    """
    return bool(win32gui.IsIconic(hwnd))    # 窗口是否最小化

def is_visible(hwnd):
    """检查指定窗口句柄是否可见（即窗口在屏幕上显示）判断窗口是否可见（未被隐藏或最小化）。
    过滤可见窗口：在遍历窗口时，跳过隐藏的窗口（例如后台进程的不可见窗口）。
    检测窗口显示状态: 在自动化操作中，确认窗口已显示后再进行操作（如点击按钮）。
    调试窗口显示问题: 检查窗口是否因代码逻辑错误被意外隐藏。
    hwnd ： 需要判断的窗口句柄、
    返回值：
    布尔值（True或False）
    """
    if not hwnd:
        raise ValueError("输入的句柄无效")
    elif not bool(win32gui.IsWindowEnabled(hwnd)):# 判断句柄是否存在
        raise ValueError("输入的句柄不存在")
    return win32gui.IsWindowVisible(hwnd)

def get_all_top_level_win():
#     # 1. 检查窗口是否可见
#     if win32gui.IsWindowVisible(hwnd):
#         # 2. 获取窗口标题
#         title = win32gui.GetWindowText(hwnd)
#         if title:  # 过滤无标题窗口
#             # 3. 确保是顶级窗口（父窗口为桌面窗口）
#             parent_hwnd = win32gui.GetParent(hwnd)
#             if parent_hwnd == 0:  # 父窗口为0表示顶级窗口
#                 window_list.append((hwnd, title))
#     return True  # 继续遍历
#
#     # 调用 EnumWindows 收集所有可见的顶级窗口
#
#
# visible_top_windows = []
# win32gui.EnumWindows(enum_visible_top_windows, visible_top_windows)
# 输出结果
# for hwnd, title in visible_top_windows:
#     print(f"窗口句柄: {hwnd}, 标题: {title}")
    pass

def get_win_attribute(hwnd):
    """输入句柄获取窗口的属性
    参数：
    hwnd ： 需要判断的窗口句柄
    返回值：
    win_attribute ： 字典
    """
    win_attribute = {"样式": win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE),
                     "扩展样式": win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE),
                     "窗口的消息处理函数": win32gui.GetWindowLong(hwnd, win32con.GWL_WNDPROC),
                     "与窗口关联的实例句柄": win32gui.GetWindowLong(hwnd, win32con.GWL_HINSTANCE),
                     "如果窗口是子窗口，则获取父窗口的句柄": win32gui.GetWindowLong(hwnd, win32con.GWL_HWNDPARENT),
                     "窗口的标识符": win32gui.GetWindowLong(hwnd, win32con.GWL_ID)}
    return win_attribute

def get_dif_win_scaling_factor(operation_hwnd,sync_hwnd):
    pass # 没有验证，也没有时间写多窗口的
    """获得两个窗口的缩放比例（进一步确定同步坐标）
    参数：
    operation_hwnd ： 操作窗口的窗口句柄
    sync_hwnd ： 被同步的窗口句柄
    返回值：
    scaling_factor ： 两个窗口的浮点数比例（被操作窗口坐标直接X就好了）
    """
    try:
        size = win32gui.GetWindowRect(operation_hwnd)
        size2 = win32gui.GetWindowRect(sync_hwnd)
    except():
        raise ValueError("填入的窗口句柄无效")
    scaling_factor = (size[2] - size[0]) / (size2[2] - size2[0])
    return scaling_factor

if __name__ == '__main__':
    print(get_operating_system())
    print(get_computer_type())
    print(get_hostname())
    print(get_screen_resolution())
    get_screen_resolution()
    get_scaling_factor()
    # change_environment_value("Test","1",True)
    """窗口句柄测试"""
    print(f"pycharm(标题SunAwtFrame)的句柄：{find_hwnd('SunAwtFrame')}")
    print(f"当前窗口的句柄：{find_current_hwnd()}")
    find_all_child_hwnd(1771326)
    # print(find_hwnd_ex(0,0,"Qt5QWindowIcon", "鸣潮"))
    find_parent_hwnd(1246766)
    get_win_title
