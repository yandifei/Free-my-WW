# 用来对win系统进行控制的
"""
1. 鼠标范围限制（即使程序结束了，效果还在，但是切屏效果就没了）
"""
# 导包
import win32gui, win32api
# 自己的包
from Free_my_WW_package.UserFeedback import *  # 用户反馈
from Free_my_WW_package.SysInformation import *    # 获取系统信息

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

def find_current_hwnd():
    """获取当前的句柄（当前的前台窗口句柄）"""
    return win32gui.GetForegroundWindow()

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

# 窗口操作类(默认输入的句有效，如果无效则报错)
def flash_win(hwnd,bitwise_inversion=True):
    """使窗口闪烁或闪烁加颜色反转闪烁（这个函数通常用于当应用程序需要用户注意时，比如有新消息到达或者某个任务完成。）
    参数：
    hwnd ： 需要闪烁的窗口的句柄
    bitwise_inversion : 窗口颜色反转，默认True
    """
    win32gui.FlashWindow(hwnd, bitwise_inversion)

def change_hwnd_title(hwnd, new_title):
    """改变窗口句柄标题
    参数：
    hwnd ： 需要改变标题的窗口句柄
    new_title ： 标题名称
    """
    win32gui.SetWindowText(hwnd, new_title)

def hide_window(hwnd):
    """通过窗口句柄隐藏窗口
    参数：
    hwnd ： 需要隐藏的窗口的句柄
    """
    win32gui.ShowWindow(hwnd,win32con.SW_HIDE)#隐藏

def show_window(hwnd):
    """通过窗口句柄显示窗口
    参数：
    hwnd ： 需要显示的窗口的句柄
    """
    win32gui.ShowWindow(hwnd,win32con.SW_SHOW)  #显示

def focus_to_current_window(hwnd):
    """把焦点设置在当前窗口或控件上（前台窗口或控件）用户主动触发的窗口切换（如弹窗）
    将指定窗口强制设为 前台活动窗口（即用户当前交互的窗口）。
    系统安全限制：Windows 10/11 会阻止非用户主动触发的窗口抢占前台（防止恶意弹窗）。
    参数：
    hwnd ： 窗口或控件的句柄
    """
    win32gui.SetForegroundWindow(hwnd)  # 窗口置顶

def focus_to_window(hwnd):
    """把焦点设置在窗口或控件上，始终置顶的监控窗口
    核心作用：将窗口调整到 Z 序的顶部（即窗口堆叠顺序的最前面），但不保证激活窗口或获得焦点。
    如果窗口处于最小化状态，会尝试恢复窗口到正常显示状态。
    参数：
    hwnd ： 窗口或控件的句柄
    """
    win32gui.SetFocus(hwnd)

def change_win_geometry(hwnd, mod=0):
    """很厉害但是好像没用"""
    """Z 顺序常量
    HWND_TOP	0	将窗口置于 Z 顺序顶部（但不强制置顶）。
    HWND_BOTTOM	1	将窗口置于 Z 顺序底部（可能被其他窗口覆盖）。
    HWND_TOPMOST	-1	强制窗口置顶（即使失去焦点也保持在最前）。
    HWND_NOTOPMOST	-2	取消窗口置顶状态，恢复到正常 Z 顺序。
    标志常量
    SWP_NOSIZE	0x0001	保持窗口当前尺寸，忽略 cx 和 cy 参数。
    SWP_NOMOVE	0x0002	保持窗口当前位置，忽略 x 和 y 参数。
    SWP_NOZORDER	0x0004	保持窗口当前 Z 顺序，忽略 hWndInsertAfter 参数。
    SWP_SHOWWINDOW	0x0040	显示窗口（如果窗口被隐藏）。"""
    win32_flags = None  # 用来存放顺序常量和标志常量（默认添加不移动位置）
    if mod == 0:
        win32_flags = win32con.SWP_NOSIZE | win32con.SWP_NOZORDER | win32con.SWP_NOMOVE # 不调整大小和层级
    elif mod == 1:
        win32_flags = win32con.SWP_NOSIZE | win32con.SWP_NOMOVE   # 不调大小
    elif mod == 2:
        win32_flags = win32con.SWP_NOZORDER | win32con.SWP_NOMOVE # 不调整层级
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, 0, 0, win32_flags)

def set_win_geometry(hwnd, x, y, width, height,repaint=True):
    """设置窗口的大小和位置(几何)
    参数(窗口大小是有默认限制的，超过则为窗口默认的最大或最小)：
    hwnd ： 窗口的句柄
    x ： 窗口左上角的x坐标
    y ： 窗口左上角的y坐标
    width ： 设置窗口的宽度
    height ： 设置窗口的高度
    repaint : 重新绘制窗口，默认打开
    """
    win32gui.MoveWindow(hwnd, x, y, width, height, repaint)

def move_win(hwnd, x, y, repaint=True):
    """移动窗口到指定位置
    hwnd ： 窗口的句柄
    x ： 窗口左上角的x坐标
    y ： 窗口左上角的y坐标
    repaint : 重新绘制窗口，默认打开
    """
    size = win32gui.GetWindowRect(hwnd) # 获取窗口左上角和右下角的坐标
    width, height = size[2] - size[0], size[3] - size[1]    # 计算窗口的大小
    win32gui.MoveWindow(hwnd, x, y, width, height, repaint)

def set_win_size(hwnd, width, height, repaint=True):
    """改变窗口的大小（坐标保持在左上角）
    hwnd ： 窗口的句柄
    width ： 设置窗口的宽度
    height ： 设置窗口的高度
    repaint : 重新绘制窗口，默认打开
    """
    point = win32gui.GetWindowRect(hwnd) # 获取窗口左上角和右下角的坐标
    win32gui.MoveWindow(hwnd, point[0], point[1], width, height, repaint)

def remove_max_mix_size(hwnd,mod=0):
    """去除窗口的最大化和最小化以及大小缩放（如果标题栏是自己重写没有与win标题栏有关的就无法影响）
    hwnd ： 窗口的句柄
    mod : 1为仅去除最大化，2为仅去除最小化，3为仅去除窗口边缘拉伸，默认为0（都执行）
    返回值：
    如果窗口句柄无效就会报错
    """
    # 获取当前窗口样式
    new_style = None    # 用来存放新的样式
    current_style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
    # 移除可调整大小、最大化、最小化
    if mod == 0:
        new_style = current_style & ~win32con.WS_THICKFRAME & ~win32con.WS_MAXIMIZEBOX & ~win32con.WS_MINIMIZEBOX
    elif mod == 1:
        new_style = current_style & ~win32con.WS_MAXIMIZEBOX    # 最大化
    elif mod == 2:
        new_style = current_style & ~win32con.WS_MINIMIZEBOX    # 最小化
    elif mod == 3:
        new_style = current_style & ~win32con.WS_THICKFRAME     # 去除边缘缩放
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, new_style)     # 应用新样式
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

def top_win(hwnd):
    """将窗口置顶
    hwnd ： 窗口的句柄
    """
    win32gui.SetWindowPos(
        hwnd,
        win32con.HWND_TOPMOST,  # 置顶层
        0, 0, 0, 0,
        win32con.SWP_NOMOVE | win32con.SWP_NOSIZE
    )

def cancel_top_win(hwnd):
    """取消窗口置顶
    hwnd ： 窗口的句柄
    """
    win32gui.SetWindowPos(
        hwnd,
        win32con.HWND_NOTOPMOST,  # 取消置顶
        0, 0, 0, 0,
        win32con.SWP_NOMOVE | win32con.SWP_NOSIZE
    )




if __name__ == "__main__":
    # 限制鼠标移动范围
    limit_cursor(report=False)
    # 释放鼠标限制
    release_cursor(False)
    print(f"编译器的句柄：{find_hwnd('SunAwtFrame')}")
    # print(find_hwnd_ex(0,0,"Qt5QWindowIcon", "鸣潮"))
    print(f"当前窗口的句柄：{find_current_hwnd()}")
    # print(mouse_find_hwnd(682,243))
    # print(mouse_fine_child_hwnd(682,243))
    # print(find_all_child_hwnd(2819532))
    # print(find_parent_hwnd(0))
    # print(get_win_size(2819532))
    # print(get_win_title(2819532))
    # print(get_win_classname(2819532))
    # print(is_hwnd(2819532))
    # print(is_use_hwnd(2819532))
    # print(is_min(5440130))
    # print(is_visible(2819532))
    # print(f"窗口状态：{get_win_attribute(328824)}")
    # flash_win(393976)
    # change_hwnd_title(5440130,"hello world")
    # hide_window(4064822)
    # show_window(4064822)
    # set_win_geometry(852606,0,0,1000,1000)
    # move_win(263116,0,0)
    # set_win_size(263116,1000,1000)
    # remove_max_mix_size(328824,0)
    fixed_size_zored(1115748)