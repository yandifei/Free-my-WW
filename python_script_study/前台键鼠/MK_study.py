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
from time import *
sleep(2) # 给我切屏的时间
"""""""""""""""""""""""""""""""""""""""""""""""""""鼠标"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
请注意： 在 Mac 上不能立即拖动。
鼠标在四边角终止程序（判定为故障终止程序，鼠标出问题的时候移到左上角）默认开启
在每次 PyAutoGUI 调用后设置默认0.1秒的暂停
"""
x, y= pyautogui.position()  # 获得当前鼠标坐标
print(f"鼠标当前坐标是{x},{y}")
width ,height = pyautogui.size()  #获得当前屏幕的分辨率
print(f"当前屏幕分辨率是{width}X{height}")
mouse_exists = pyautogui.onScreen(x, y)  # 判断鼠标是否在给定坐标上
print(mouse_exists)
pyautogui.PAUSE = 0   # 在每次 PyAutoGUI 调用后设置 2.5 秒的暂停（默认0.1秒）
pyautogui.FAILSAFE = False   # 鼠标在四边角终止程序（判定为故障终止程序，鼠标出问题的时候移到左上角）默认开启
# 在多少秒内移动鼠标到x，y（自带鼠标移动轨迹，三角函数的还是比较容易被发现）
# pyautogui.moveTo(325,872, duration=0)  # duration参数不写默认为0，直接移动
# # pyautogui.moveRel(100, 0, duration=1)  # 鼠标相对移动
# pyautogui.dragTo(1900.1,873, duration=0.2)  # 将鼠标拖拽到x，y|实际测试的时候发现移动时间短的话得增加挪动位置
"""click函数（这个是最屌的一个下面鼠标的父类）
x,y移动的坐标，clicks是点击的次数，interval是点击间隔时间（点击后等待时间），button是选择鼠标左击还是右击还是中键
参数都不写默认左击一次，其他参数均为0
"""
# pyautogui.click(x=1000, y=1000, clicks=4, interval=1, button='left')
"""rightClick,middleClick,doubleClick,tripleClick函数
参数可写可不写，还有其他参数隐藏的，官方文档没讲，得自己跳转分析
如果传入的是坐标，则会到对应坐标，但是如果传的只有一个坐标，另一个坐标什么都没写那就是相对移动
"""
# 鼠标右击
# pyautogui.rightClick(100,100)
# 鼠标中击
# pyautogui.middleClick(100,100)
# 鼠标两次左击(0.1就fps6了)
# pyautogui.doubleClick(interval=0.1)
# 鼠标三连击
# pyautogui.tripleClick(1001,585)
# 鼠标滚到动，参数一是滚动的像素点，二三是坐标
# pyautogui.scroll(300)
# 鼠标某个按键按下，参数1、2是坐标，参数3是鼠标的操作，当然还有其他参数
# pyautogui.mouseDown()   # 没有参数默认左击一直按下
# # 鼠标某个按键抬起，参数1、2是坐标，参数3是鼠标的操作，当然还有其他参数
# pyautogui.mouseUp()     # 没有参数默认左击一直起来
"""""""""""""""""""""""""""""""""""""w""""""""""""""键盘"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# 文本输入，参数一是输入的字符串，参数二是每个字符的输入间隔时间（什么都不填就报错）
# pyautogui.typewrite("hello world!\n")
# 参数一以列表的形式传入的键盘和鼠标操作,第二个参数是输入的每个操作的时间间隔
# pyautogui.typewrite(['a', 'b', 'c', 'd', 'e', 'f', 'g','enter', 'backspace', 'left'], interval=0)
# 像 Ctrl+S 或 Ctrl+Shift+1 这样的键盘热键可以通过将键名称列表传递给hotkey()来完成：
# pyautogui.hotkey('ctrl', 'c')  # 按下ctrl+c的热键（组合键）
# 按下某个按键
# pyautogui.keyDown(key_name)
# 抬起某个按键
# pyautogui.keyUp(key_name)

"""""""""""""""""""""""""""""""""""""""""""""""""""消息框函数"""""""""""""""""""""""""""""""""""""""""""""""""""
# 如果需要暂停程序，直到用户单击“确定”，或者想向用户显示一些信息，则消息框函数具有与JavaScript 相似的名称：
# 弹出一个对话框
# pyautogui.alert('This displays some text with an OK button.')
# 弹出一个有确认和取消的对话框，但是对话和取消按钮的字符是英文的
# pyautogui.confirm('This displays text and has an OK and Cancel button.')
# 弹出有一个输入框，取消和ok的按钮，具有返回值
# a = pyautogui.prompt('This lets the user type in a string and press OK.')
# print(a)    # 什么都不填或点击取消返回为None



