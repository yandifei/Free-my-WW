import win32gui

def enum_windows_callback(hwnd, window_list):
    if win32gui.IsWindowVisible(hwnd):  # 过滤可见窗口
        title = win32gui.GetWindowText(hwnd)
        if title:  # 过滤无标题窗口
            window_list.append((hwnd, title))
    return True  # 继续遍历

# 调用 EnumWindows
all_visible_windows = []
win32gui.EnumWindows(enum_windows_callback, all_visible_windows)

# 输出结果
for hwnd, title in all_visible_windows:
    print(f"句柄: {hwnd}, 标题: {title}")