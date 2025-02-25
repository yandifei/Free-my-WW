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

"""窗口操作类(默认输入的句有效，如果无效则报错)需要结合SysInformation.py的模块获取句柄-"""
def hide_window(hwnd):
    """通过窗口句柄隐藏窗口
    参数：
    hwnd ： 需要隐藏的窗口的句柄
    """
    win32gui.ShowWindow(hwnd,win32con.SW_HIDE)#隐藏

def max_win(hwnd):
    """最大化窗口
    参数：
    hwnd ： 窗口句柄
    """
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

def min_win(hwnd):
    """最小化窗口
    参数：
    hwnd ： 窗口句柄
    """
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

def close_win(hwnd):
    """关闭窗口（如果输入的不是父窗口则关闭的是子窗口）
    参数：
    hwnd ： 需要关闭的窗口的句柄
    """
    # 发送 WM_CLOSE 消息来请求关闭窗口
    win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

def show_window(hwnd):
    """通过窗口句柄显示窗口
    参数：
    hwnd ： 需要显示的窗口的句柄
    """
    win32gui.ShowWindow(hwnd,win32con.SW_SHOW)  #显示

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

def flash_win(hwnd,bitwise_inversion=True):
    """使窗口闪烁或闪烁加颜色反转闪烁（这个函数通常用于当应用程序需要用户注意时，比如有新消息到达或者某个任务完成。）
    参数：
    hwnd ： 需要闪烁的窗口的句柄
    bitwise_inversion : 窗口颜色反转，默认True
    """
    win32gui.FlashWindow(hwnd, bitwise_inversion)

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

def change_hwnd_title(hwnd, new_title):
    """改变窗口句柄标题
    参数：
    hwnd ： 需要改变标题的窗口句柄
    new_title ： 标题名称
    """
    win32gui.SetWindowText(hwnd, new_title)

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

def restore_max_mix_size(hwnd,mod=0):
    """恢复窗口的最大化和最小化以及大小缩放（如果标题栏是自己重写没有与win标题栏有关的就无法影响）
        hwnd ： 窗口的句柄
        mod : 1为仅恢复最大化，2为仅恢复最小化，3为仅恢复窗口边缘拉伸，默认为0（都执行）
        返回值：
        如果窗口句柄无效就会报错
        """
    # 获取当前窗口样式
    new_style = None  # 用来存放新的样式
    current_style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)    # 获得旧样式
    # 移除可调整大小、最大化、最小化
    """ & ~ 是去除， | 是使用"""
    if mod == 0:
        new_style = current_style | win32con.WS_THICKFRAME | win32con.WS_MAXIMIZEBOX | win32con.WS_MINIMIZEBOX
    elif mod == 1:
        new_style = current_style | win32con.WS_MAXIMIZEBOX  # 最大化
    elif mod == 2:
        new_style = current_style | win32con.WS_MINIMIZEBOX  # 最小化
    elif mod == 3:
        new_style = current_style | win32con.WS_THICKFRAME  # 去除边缘缩放
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, new_style)  # 应用新样式
    win32gui.SetWindowPos(
        hwnd,
        win32con.HWND_TOP,
        0, 0, 0, 0,
        win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_FRAMECHANGED
    )

def remove_caption(hwnd):
    """去掉标题栏(不包括窗口控制按钮)
    参数：
    hwnd ： 窗口的句柄
    """
    current_style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
    new_style = current_style & ~win32con.WS_CAPTION
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, new_style)  # 应用新样式
    # 重新绘制
    win32gui.SetWindowPos(hwnd, 0, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_FRAMECHANGED)

def restore_caption(hwnd):
    """恢复标题栏(不包括窗口控制按钮)
    参数：
    hwnd ： 窗口的句柄
    """
    current_style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
    new_style = current_style | win32con.WS_CAPTION
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, new_style)  # 应用新样式
    # 重新绘制
    win32gui.SetWindowPos(hwnd, 0, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_FRAMECHANGED)

def remove_sysmenu(hwnd):
    """去除系统菜单(去掉的窗口控制按钮)
    参数：
    hwnd ： 窗口的句柄
    """
    current_style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)    # 获得当前的系统样式
    new_style = current_style & ~win32con.WS_SYSMENU
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, new_style)  # 应用新样式
    # 重新绘制
    win32gui.SetWindowPos(hwnd, 0, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_FRAMECHANGED)

def restore_sysmenu(hwnd):
    """恢复系统菜单(恢复的窗口控制按钮)
    参数：
    hwnd ： 窗口的句柄
    """
    current_style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)  # 获得当前的系统样式
    new_style = current_style | win32con.WS_SYSMENU
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, new_style)  # 应用新样式
    # 重新绘制
    win32gui.SetWindowPos(hwnd, 0, 0, 0, 0, 0,
                          win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_FRAMECHANGED)

def remove_title(hwnd):
    """去除标题栏(去掉的窗口的标题栏)
    参数：
    hwnd ： 窗口的句柄
    """
    current_style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)    # 获得当前的系统样式
    new_style = current_style & ~win32con.WS_SYSMENU & ~win32con.WS_CAPTION
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, new_style)  # 应用新样式
    # 重新绘制
    win32gui.SetWindowPos(hwnd, 0, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_FRAMECHANGED)

def restore_title(hwnd):
    """去除标题栏(去掉的窗口的标题栏)
    参数：
    hwnd ： 窗口的句柄
    """
    current_style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)    # 获得当前的系统样式
    new_style = current_style & ~win32con.WS_SYSMENU & ~win32con.WS_CAPTION
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, new_style)  # 应用新样式
    # 重新绘制
    win32gui.SetWindowPos(hwnd, 0, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_FRAMECHANGED)

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


if __name__ == "__main__":
    # 限制鼠标移动范围
    limit_cursor(report=False)
    # 释放鼠标限制
    release_cursor(False)
