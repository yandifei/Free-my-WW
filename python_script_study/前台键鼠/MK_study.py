# 前台键盘鼠标学习
"""
PyAutoGUI
功能：PyAutoGUI是一个功能强大的Python库，它可以模拟键盘按键、鼠标移动、点击、拖动等操作。
此外，它还支持截屏、获取屏幕尺寸等功能。
Pynput
功能：Pynput提供了对键盘和鼠标的更高级控制，包括监听键盘和鼠标事件、模拟按键和鼠标移动等操作。
与PyAutoGUI相比，Pynput在事件监听方面更为强大。
"""
# 导包
import pyautogui
# 鼠标
x,y = pyautogui.position()  # 获得当前鼠标坐标
print(type(x))
# (968, 56)
# >>> pyautogui.size()  # current screen resolution width and height
# (1920, 1080)
# >>> pyautogui.onScreen(x, y)  # True if x & y are within the screen.
# True