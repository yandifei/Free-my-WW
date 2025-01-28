# 前台键盘鼠标学习https://pyautogui.readthedocs.io/en/latest/install.html
"""
PyAutoGUI
功能：PyAutoGUI是一个功能强大的Python库，它可以模拟键盘按键、鼠标移动、点击、拖动等操作。
此外，它还支持截屏、获取屏幕尺寸等功能。
Pynput
功能：Pynput提供了对键盘和鼠标的更高级控制，包括监听键盘和鼠标事件、模拟按键和鼠标移动等操作。
与PyAutoGUI相比，Pynput在事件监听方面更为强大。
"""
# 导包
import pyautogui  # 键鼠截图,弹窗
import pyscreeze  # 想要使用pyautogui这个包的截图功能提示我需要这个包，这个包自带的了
from PIL import Image  # 想要使用pyautogui这个包的截图功能提示我需要这个包，这个包Pillow得下载
from time import *

sleep(2)  # 给我切屏的时间
"""""""""""""""""""""""""""""""""""""""""""""""""""鼠标"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
请注意： 在 Mac 上不能立即拖动。
鼠标在四边角终止程序（判定为故障终止程序，鼠标出问题的时候移到左上角）默认开启
在每次 PyAutoGUI 调用后设置默认0.1秒的暂停
"""
# x, y = pyautogui.position()  # 获得当前鼠标坐标
# print(f"鼠标当前坐标是{x},{y}")
# width, height = pyautogui.size()  # 获得当前屏幕的分辨率
# print(f"当前屏幕分辨率是{width}X{height}")
# mouse_exists = pyautogui.onScreen(x, y)  # 判断鼠标是否在给定坐标上
# print(mouse_exists)
pyautogui.PAUSE = 0  # 在每次 PyAutoGUI 调用后设置 2.5 秒的暂停（默认0.1秒）
pyautogui.FAILSAFE = False  # 鼠标在四边角终止程序（判定为故障终止程序，鼠标出问题的时候移到左上角）默认开启
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

"""""""""""""""""""""""""""""""""""""""""""""""""""""屏幕截图功能"""""""""""""""""""""""""""""""""""""""""""""""
# 如果在屏幕上找不到图像，则返回这些函数。None
# locate 函数速度很慢，可能需要一两秒钟。
"""screenshot
我在使用的时候提示我需要这个pyscreeze包
# 在 Linux 上，必须运行才能使用屏幕截图功能。sudo apt-get install scrot
"""
"""
在我win电脑上面提示必须要2个包，pyscreeze自带的，PIL要下载但是我好像没有这个包的下载渠道
我尝试用Pillow替换PIL这个包，我的电脑没有这个包（我下好之后发现导PIL这个包居然没报错，但是我下的是pillow这个包）
导包是PIL，下包的名称是Pillow
不填写参数据就自动创建对象，图片放到内存里面去
填写参数就是保存到文件中
"""
# import pyscreeze    # 想要使用pyautogui这个包的截图功能提示我需要这个包，这个包自带的了
# from PIL import Image   # 想要使用pyautogui这个包的截图功能提示我需要这个包，这个包Pillow得下载
# pyautogui.screenshot('a.png')  # 返回图像信息（本身就是对象），并将其保存到文件中
"""locateOnScreen找单个图
返回Box(left=0, top=0, width=1920, height=1080)
找到的是图片的左上角和右下角的坐标，如果找不到就报错，停止程序，得try一下
"""
# pyautogui.locateOnScreen('a.png')  # 返回找到第一个图像的位置
# print(a)
"""locateAllOnScreen()找多图
把所有符合图片都遍历一遍，但是必须提取，不然就是最后一个的图像的了
他是不断找，并且替换自身的返回值直到找完一张图片，所以一定要用for提取或用其他的元组等方式保存每次的返回值
print(pyautogui.locateAllOnScreen("a.png"))即使图片没有或都不符合也没报错
for提取的时候没有找到图片会报错
"""
# print(pyautogui.locateAllOnScreen("a.png"))     # 找多图，直接输出他的返回值
# for i in pyautogui.locateAllOnScreen("a.png"):    # 找多图，遍历打印
#      print(i)
# list(pyautogui.locateAllOnScreen('looksLikeThis.png')) # 找多图，存到列表里面去
"""locateCenterOnScreen()
该函数只返回在屏幕上找到图像的中间位置的 XY 坐标，计算找到图像的中间值
本身就是返回值
"""
# print(pyautogui.locateCenterOnScreen("a.png"))
"""--------------------------------------深度研究------------------------------------------"""
# 屏幕分辨率大小由函数以两个整数的元组形式返回。该函数返回鼠标光标的当前 X 和 Y 坐标。
# pyautogui.size()  #获得当前屏幕的分辨率
# print(f"当前屏幕分辨率是{width}X{height}")
# 官方文档有不断打印鼠标坐标例子，但我觉得费劲，还用到try，我自己随便写一个简单的吧
# try:
#     while True:
#          x, y = pyautogui.position()  # 获得当前鼠标位置
#          sleep(0.1) # 0.1秒获取一次吧，我就不用内置的间隔函数了，不优雅
#          print(f"x坐标为{x},y坐标为{y}")
# except KeyboardInterrupt:
#      print("出现错误")
# 判断鼠标能否出现在给定范围内，分清分辨率和鼠标最大坐标
# print(pyautogui.onScreen(1919, 1079))
# 该函数会将鼠标光标移动到您传递给它的 X 和 Y 整数坐标。该值可以传递坐标以表示 “当前鼠标光标位置”。例如：moveTo()None
# pyautogui.moveTo(100, 200)   # 将鼠标移动到 X 值 100、Y 值 200。
# pyautogui.moveTo(None, 500)  # 将鼠标移动到 X 值 100，Y 值 500。
# pyautogui.moveTo(600, None)  # 将鼠标移动到 X 值 600、Y 值 500。
# 通常，鼠标光标会立即移动到新坐标。如果希望鼠标逐渐移动到新位置，请传递移动应采用的持续时间 （以秒为单位） 的第三个参数。例如：
# （如果持续时间短于此，则移动将是即时的。默认情况下，为 0.1。
# pyautogui.moveTo(100, 200, 0)  # 在 2 秒内将鼠标移动到 X 值 100，Y 值 200
# 相对移动，将鼠标光标相对于其当前位置移动几个像素。
# pyautogui.move(0, 50)       # 将鼠标下移 50 像素。
# pyautogui.move(-30, None)   # 将鼠标向左移动 30 像素。
# # PyAutoGUI 的 and 函数具有与 and 函数类似的参数。此外，它们还有一个可以设置为 、 的关键字，以及拖动时要按住的鼠标按钮。例如：
# pyautogui.dragTo(100, 200, button='left')     # 按住鼠标左键，将鼠标拖动到 X 值 100、Y 值 200
# pyautogui.dragTo(300, 400, 2, button='left')  # 在 2 秒内将鼠标拖动到 X 值 300、Y 值 400 的位置，同时按住鼠标左键
# pyautogui.drag(30, 0, 2,button='right')  # 在 2 秒钟内将鼠标向左拖动 30 像素，同时按住鼠标右键
"""补间/缓动函数(更加模拟真人)
补间是使鼠标移动更花哨的额外功能。如果您不关心这些，您可以跳过本节。
补间或缓动函数指示鼠标移动到目标时的进度。通常，在一段时间内移动鼠标时，鼠标会以恒定速度沿直线直接向目标移动。
这称为线性补间或线性缓动函数。
PyAutoGUI 在模块中还有其他可用的补间功能。
可以将第 4 个参数的函数传递给 , , , 和 函数，使鼠标光标开始缓慢移动，然后加速向目标移动。
总持续时间仍与传递给函数的参数相同。情况正好相反：鼠标光标开始快速移动，但在接近目标时减慢速度。
将越过目的地并来回 “橡皮筋” 直到它稳定在目的地。
这些补间函数是从 Al Sweigart 的 PyTweening 模块复制而来的：
https://pypi.python.org/pypi/PyTweening https://github.com/asweigart/pytweening 不必安装此模块即可使用 tweening 函数。
如果要创建自己的补间函数，请定义一个函数，该函数在 （表示鼠标移动的开始） 和 （表示鼠标移动的结束） 之间采用单个 float 参数，并返回 和 之间的 float 值。0.01.00.01.0
"""
# pyautogui.moveTo(100, 100, 1, pyautogui.easeInQuad)     # 开始慢，结束快
# pyautogui.moveTo(100, 100, 1, pyautogui.easeOutQuad)    # 开始快，结束慢
# pyautogui.moveTo(100, 100, 1, pyautogui.easeInOutQuad)  # 开始和结束快，中间慢
# pyautogui.moveTo(100, 100, 1, pyautogui.easeInBounce)   # 快结束时会有一个轻微的、快速的反弹动作，然后再停下来
# pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)  # 人，通过不断回弹到达最终目标（四周移动不断扩大范围）
# 鼠标点击，该函数模拟鼠标左键单击鼠标当前位置。“咔嗒”定义为按下按钮，然后向上释放。例如：click()
# pyautogui.click()
# 要在单击之前合并调用，请为 and 关键字参数传递整数：moveTo()xy
# pyautogui.click(x=100, y=200)
# 要指定要单击、传递 、 或 关键字参数的不同鼠标按钮：'left''middle''right'button
# pyautogui.click(button='right')
# 要执行多次单击，请将整数传递给 keyword 参数。（可选）您可以将 float 或 integer 传递给 keyword 参数，以指定单击之间的暂停时间（以秒为单位）。例如：clicksinterval
# pyautogui.click(clicks=2)
# pyautogui.click(clicks=2, interval=0.25)
# 作为一个方便的快捷方式，该函数将执行鼠标左键的双击。它还具有可选的 、 、 和 关键字参数。例如：doubleClick()xyintervalbutton
# pyautogui.doubleClick()
# 还有一个具有类似 optional keyword arguments 的函数。tripleClick()该函数具有 optional 和 keyword 参数。rightClick()xy
# mouseDown（） 和 mouseUp（） 函数
# 鼠标单击和拖动由按下鼠标按钮和重新松开鼠标按钮组成。如果要单独执行这些操作，请调用 and 函数。它们具有相同的 、 、 和 。例如：mouseDown()mouseUp()xybutton
# 可以通过调用函数并传递整数次的 “clicks” 来滚动来模拟鼠标滚轮。“click” 中的滚动量因平台而异。（可选）可以为 the 和 keyword 参数传递整数，以便在执行滚动之前移动鼠标光标。例如：scroll()xy
# 在 OS X 和 Linux 平台上，PyAutoGUI 还可以通过调用 hscroll（） 函数来执行水平滚动。例如：
# pyautogui.hscroll(10)
# pyautogui.hscroll(-10)
# 该函数是scroll()vscroll()的包装器，用于执行垂直滚动。
""""键盘控制功能"""
# write（） 函数
#主要键盘功能是 。此函数将在传递的字符串中键入字符。要在按下每个字符键之间添加延迟间隔，请为 keyword 参数传递 int 或 float。write()interval
# pyautogui.write('Hello world!')
# pyautogui.write('Hello world!', interval=0.25)
# 您只能使用write()按单字符键，因此不能按 Shift 或 F1 键。
"""press（）、keyDown（） 和 keyUp（） 函数
要按这些键，请调用该函数并向其传递一个字符串，例如 、 、 。
请参阅 KEYBOARD_KEYS。press()pyautogui.KEYBOARD_KEYSenterescf1'
例如：
pyautogui.press('enter')  # press the Enter key
pyautogui.press('f1')     # press the F1 key
pyautogui.press('left')   # press the left arrow key
"""
"""
该函数实际上只是 and 函数的包装器，它模拟按下一个键，然后松开它。这些函数可以自行调用。
例如，要在按住 Shift 键的同时按向左箭头键三次，请调用以下命令：press()keyDown()keyUp()
pyautogui.keyDown('shift')  # hold down the shift key
pyautogui.press('left')     # press the left arrow key
pyautogui.press('left')     # press the left arrow key
pyautogui.press('left')     # press the left arrow key
pyautogui.keyUp('shift')    # release the shift key
"""
# 要按多个键，请向 .例如：write()press()
# pyautogui.press(['left', 'left', 'left'])
# 或者您可以设置按压机的数量 ：left
# pyautogui.press('left', presses=3)
# 要在每次按下之间添加延迟间隔，请为interval参数传递 int 或 float。
"""
hold（） 上下文管理器
为了方便持有键，该函数可以用作上下文管理器，并从 、 、 传递一个字符串，并且此键将在上下文块的持续时间内保留。
请参阅 KEYBOARD_KEYS。hold()pyautogui.KEYBOARD_KEYSshiftctrlaltwith
"""
# with pyautogui.hold('shift'):
#         pyautogui.press(['left', 'left', 'left'])
# 与上面代码等价
# pyautogui.keyDown('shift')  # hold down the shift key
# pyautogui.press('left')     # press the left arrow key
# pyautogui.press('left')     # press the left arrow key
# pyautogui.press('left')     # press the left arrow key
# pyautogui.keyUp('shift')    # release the shift key
# 热键、组合键、快捷键hotkey（） 函数
# 为了方便按下热键或键盘快捷键，可以传递几个键串，这些键串将按顺序按下，然后以相反的顺序释放。此代码：hotkey()
# 要在每次按下之间添加延迟间隔，请为 keyword 参数传递 int 或 float。interval
# pyautogui.hotkey('ctrl', 'shift', 'esc')
"""  KEYBOARD_KEYS以下是要传递给 、 、 和 函数的有效字符串：press()keyDown()keyUp()hotkey()
['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']
"""
"""消息框函数
PyAutoGUI 利用 PyMsgBox 中的消息框函数来提供一种跨平台的纯 Python 方式来显示 JavaScript 样式的消息框。
提供了四个消息框函数：alert（） 函数confirm（） 函数  prompt（） 函数     password（） 函数
"""
# 显示一个带有文本和单个 OK 按钮的简单消息框。返回单击的按钮的文本。
# alert(text='', title='', button='OK')
# 显示带有 OK 和 Cancel 按钮的消息框。按钮的数量和文本可以自定义。返回单击的按钮的文本。
# confirm(text='', title='', buttons=['OK', 'Cancel'])
# 显示一个带有文本输入的消息框，以及 OK & Cancel 按钮。返回输入的文本，如果单击了 Cancel，则返回 None。
# prompt(text='', title='' , default='')
# 显示一个带有文本输入的消息框，以及 OK & Cancel 按钮。键入的字符显示为 。返回输入的文本，如果单击了 Cancel，则返回 None。*
# password(text='', title='', default='', mask='*')
"""
屏幕截图功能
PyAutoGUI 可以截取屏幕截图，将它们保存到文件中，并在屏幕中定位图像。
如果您有一个需要单击的按钮的小图像，并且想要在屏幕上找到它，这将非常有用。
这些功能由 PyScreeze 模块提供，该模块随 PyAutoGUI 一起安装。
屏幕截图功能需要 Pillow 模块。OS X 使用操作系统附带的命令。
Linux 使用该命令，该命令可以通过运行 来安装。screencapturescrotsudo apt-get install scrot
"""
"""  screenshot（） 函数
调用将返回一个 Image 对象（有关详细信息，请参阅 Pillow 或 PIL 模块文档）。
传递文件名的字符串会将屏幕截图保存到文件中，并将其作为 Image 对象返回。screenshot()
在 1920 x 1080 屏幕上，该函数大约需要 100 毫秒 - 不快但不慢。screenshot()
"""
# import pyautogui
# im1 = pyautogui.screenshot()
# im2 = pyautogui.screenshot('my_screenshot.png')
"""选定范围截图
您可以传递要捕获的区域的 left、top、width 和 height 的四个整数元组：region
如果您不想获得整个屏幕的屏幕截图，则还有一个可选的 keyword 参数。
"""
# import pyautogui
# im = pyautogui.screenshot(region=(0,0, 300, 400))
"""  定位功能
注意：从版本 0.9.41 开始，如果 locate 函数找不到提供的图像，它们将引发而不是返回 .ImageNotFoundExceptionNone
"""
"""
如果您有图像文件，您可以在屏幕上直观地找到某些内容。例如，假设计算器应用程序正在您的计算机上运行。
如果您不知道计算器按钮所在位置的确切屏幕坐标，则无法调用 and 函数。计算器每次启动时都会出现在略有不同的位置，从而导致您每次都重新查找坐标。
但是，如果您有按钮的图像，例如 7 按钮的图像：moveTo()click()
你可以调用该函数来获取屏幕坐标。返回值是一个 4 整数元组：（left， top， width， height）。
可以传递此元组以获取此区域中心的 X 和 Y 坐标。如果在屏幕上找不到图像，则会引发 。
"""
# locateOnScreen('calc7key.png')center()locateOnScreen()ImageNotFoundException
"""
可选的 keyword 参数指定函数在屏幕上定位图像的精度。
如果函数由于像素差异可以忽略不计而无法定位图像，这将非常有用：confidence
"""
# 注意：您需要安装 OpenCV 才能使关键字起作用。confidence，相似度
# 在 1920 x 1080 屏幕上，locate 函数调用大约需要 1 或 2 秒。
# 这对于动作视频游戏来说可能太慢了，但适用于大多数用途和应用程序。
# import pyautogui
# button7location = pyautogui.locateOnScreen('calc7key.png', confidence=0.9)
# button7location
# 该函数将 和 组合在一起：locateCenterOnScreen()locateOnScreen()center()
"""
有几个 “locate” 函数。他们都开始看屏幕的左上角（或图像），然后向右看，然后向下看。参数可以是

locateOnScreen(image, grayscale=False)- 返回 （left， top， width， height） 屏幕上第一个找到的实例的坐标。
如果在屏幕上找不到，则提高赌注。
imageImageNotFoundException
locateCenterOnScreen(image, grayscale=False)- 返回 （x， y） 屏幕上找到的第一个 the 实例的中心的坐标。
如果在屏幕上找不到，则提高赌注。
imageImageNotFoundException
locateAllOnScreen(image, grayscale=False)- 返回一个生成器，
该生成器为在屏幕上找到图像的位置生成 （left， top， width， height） 元组。
locate(needleImage, haystackImage, grayscale=False)- 返回 中第一个找到的实例的坐标
（left， top， width， height） 。如果在屏幕上找不到，则提高赌注。
needleImagehaystackImageImageNotFoundException
locateAll(needleImage, haystackImage, grayscale=False)- 返回一个生成器，
该生成器为 中的位置生成 （left， top， width， height） 元组。needleImagehaystackImage
"""
# “locate all” 函数可以在 for 循环中使用或传递给 ：list()
# import pyautogui
# for pos in pyautogui.locateAllOnScreen('someButton.png'):
#     print(pos)
# list(pyautogui.locateAllOnScreen('someButton.png'))
"""
这些 “locate” 函数相当昂贵;他们可能需要整整一秒钟才能运行。
加快它们速度的最佳方法是传递一个参数（一个 （left， top， width， height） 的 4 个整数元组）
来只搜索屏幕的较小区域而不是整个屏幕：region
"""
# import pyautogui
# pyautogui.locateOnScreen('someButton.png', region=(0,0, 300, 400))
"""       灰度匹配
或者，您可以传递给 locate 函数以略微加速（大约 30%）。
这会降低图像和屏幕截图中的颜色饱和度，从而加快定位速度，但可能会导致误报匹配。grayscale=True
"""
# import pyautogui
# button7location = pyautogui.locateOnScreen('calc7key.png', grayscale=True)
# button7location
"""       像素匹配
要获取屏幕截图中像素的 RGB 颜色，请使用 Image 对象的方法：getpixel()
"""
# import pyautogui
# im = pyautogui.screenshot()
# im.getpixel((100, 200))
# 或者作为单个函数调用 PyAutoGUI 函数，该函数是前面调用的包装器：pixel()
# import pyautogui
# pix = pyautogui.pixel(100, 200)
# print(pix)
# RGB(red=130, green=135, blue=144)
# print(pix[0])
# print(pix.red)
"""
如果你只需要验证单个像素是否与给定像素匹配，请调用该函数，
向其传递它所表示的颜色的 X 坐标、Y 坐标和 RGB 元组：pixelMatchesColor()
"""
# import pyautogui
# a = pyautogui.pixelMatchesColor(100, 200, (130, 135, 144))
# print(a)
# b = pyautogui.pixelMatchesColor(100, 200, (0, 0, 0))
# print(b)
# 可选的 keyword 参数指定 red、green 和 blue 值在仍然匹配时可以变化的程度：tolerance,相似度
# import pyautogui
# pyautogui.pixelMatchesColor(100, 200, (130, 135, 144))
# pyautogui.pixelMatchesColor(100, 200, (140, 125, 134))
# pyautogui.pixelMatchesColor(100, 200, (140, 125, 134), tolerance=10)

"""
路线图
PyAutoGUI 计划替代其他 Python GUI 自动化脚本，例如 PyUserInput、PyKeyboard、PyMouse、pykey 等。最终，提供与 Sikuli 提供的相同类型的功能会很棒。

目前，PyAutoGUI 的主要目标是跨平台的鼠标和键盘控制以及简单的 API。

计划的未来功能（尚未计划的特定版本）：

用于确定为什么在特定屏幕截图中找不到图像的工具。（这是用户的常见问题来源。
与 Raspberry Pis 完全兼容。
“Wave” 功能，仅用于通过稍微摇动鼠标光标来查看鼠标的位置。一个小的 helper 函数。
locateNear（） 函数，该函数与其他与定位相关的屏幕读取函数类似，不同之处在于它在屏幕上的 xy 点附近查找第一个实例。
查找所有窗口及其标题的列表。
单击相对于窗口的坐标，而不是整个屏幕的坐标。
更轻松地在具有多个监视器的系统上工作。
GetKeyState（） 函数类型
能够在所有平台上设置全局热键，以便为 GUI 自动化程序提供一个简单的“终止开关”。
可选的非阻塞 pyautogui 调用。
键盘的 “strict” 模式 - 传递无效的键盘键会导致异常，而不是静默跳过它。
将 keyboardMapping 重命名为 KEYBOARD_MAPPING
能够将 png 和其他图像文件转换为可以直接在源代码中复制/粘贴的字符串，这样它们就不必与人们的 pyautogui 脚本单独共享。
测试以确保 pyautogui 在 Windows/mac/linux VM 中正常工作。
一种比较两个图像并突出显示它们之间的差异的方法（适用于指出 UI 何时更改等）
窗户处理功能：
pyautogui.getWindows（） # 返回映射到窗口 ID 的窗口标题字典
pyautogui.getWindow（str_title_or_int_id） # 返回一个 “Win” 对象
win.move（x， y）
win.resize（宽度，高度）
win.maximize（）
win.minimize（）
win.restore（）
win.close（）

win.position（） # 返回左上角的 （x， y）
win.moveRel（x=0， y=0） # 相对于窗口左上角的 x， y 移动
win.clickRel（x=0， y=0， clicks=1， interval=0.0， button='left'） # 相对于窗口左上角的 x， y 的点击。
添加了屏幕截图功能，以便它可以捕获特定窗口而不是全屏。
"""











