import win32gui
import win32con
import win32api


def is_window_in_taskbar(hwnd):
    """检测窗口是否被隐藏到任务栏（如通过 Win+D 或 Alt+Tab 等操作）。

    Args:
        hwnd (int): 窗口句柄

    Returns:
        bool: True表示窗口在任务栏中（不可见），False表示窗口可见。
    """
    if not hwnd or not win32gui.IsWindow(hwnd):
        return False

    try:
        placement = win32gui.GetWindowPlacement(hwnd)
    except:
        return False

    # 判断窗口是否最小化
    is_minimized = placement[1] == win32con.SW_SHOWMINIMIZED

    # 判断窗口是否可见（包括父窗口链的可见性）
    is_visible = win32gui.IsWindowVisible(hwnd)

    # 检查窗口是否在屏幕外或尺寸为零（可能被隐藏）
    try:
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        is_zero_area = (right - left <= 0) or (bottom - top <= 0)
    except:
        is_zero_area = True

    # 判断窗口是否在任务栏中的关键条件
    return (is_minimized or not is_visible or is_zero_area) and _has_taskbar_button(hwnd)


def _has_taskbar_button(hwnd):
    """检查窗口是否有任务栏按钮（WS_EX_APPWINDOW 样式且无父窗口）。"""
    ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    parent = win32gui.GetParent(hwnd)

    # 条件：有任务栏按钮的窗口通常满足以下条件
    return (
            (ex_style & win32con.WS_EX_APPWINDOW) and
            parent == 0  # 无父窗口
    ) or (
            win32gui.GetWindow(hwnd, win32con.GW_OWNER) == 0  # 无所有者窗口（如顶层窗口）
    )


