# 控制和监视输入设备。包含支持的每种输入设备的子包
# pynput包文档https://pynput.readthedocs.io/en/latest/
# pynput.mouse包含用于控制和监视鼠标或触控板的类。
# pynput.keyboard包含用于控制和监视键盘的类。
""""
强制使用特定的后端
Pynput 尝试使用适合当前平台的后端，但 此自动选择可以覆盖。

如果设置了环境变量 or，则它们的值将用作 键盘类，如果设置了 OR，则它们的值将用作鼠标类的后端名称。
$PYNPUT_BACKEND_KEYBOARD$PYNPUT_BACKEND$PYNPUT_BACKEND_MOUSE$PYNPUT_BACKEND

可用的后端包括：

darwin，这是 macOS 的默认值。
win32，这是 Windows 的默认值。
uinput、需要 root 权限的 Linux 的可选后端和 仅支持键盘。
xorg，这是其他操作系统的默认设置。
dummy，一个非功能性但可导入的后端。这很有用，因为 mouse 后端。uinput
"""
# 鼠标监听失败了
# 导包
# from pynput import mouse, keyboard  # 导入整个包
# from pynput.mouse import Button, Controller # 导入鼠标的方法
from pynput import mouse # 监听鼠标
# 必须six要有这个包才能用鼠标位置读取，得自己下，不需要导入
"""------------------------------------------------鼠标------------------------------------------"""
"""控制鼠标"""
# mouse = Controller()
# 读取鼠标位置
# print(f'当前鼠标位置 {mouse.position}')
# 瞬移鼠标位置
# mouse.position = (10, 20)
# 鼠标位置相对移动（瞬移）
# mouse.move(100, -5)
# 鼠标按下和抬起
# mouse.press(Button.left)
# mouse.release(Button.left)
# 鼠标按键点击（连击）
# mouse.click(Button.left, 2)
# 鼠标滚轮
# mouse.scroll(0, 2)
"""监听鼠标"""
"""
当使用下面的非阻塞版本时，当前线程将继续 执行。
与其他 GUI 框架集成时，这可能是必要的 ，其中包含一个主循环，但是当从脚本运行时，这将导致 程序立即终止。
"""
# def on_move(x, y):
#     print(f'鼠标移动到{x, y}')
#
# def on_click(x, y, button, pressed):
#     print(f'{x},{y}')
#     if not pressed:
#         # 停止监听
#         return False
#
# def on_scroll(x, y, dx, dy):
#     print('Scrolled {0} at {1}'.format( 'down' if dy < 0 else 'up',(x, y)))
#
# # Collect events until released
# with mouse.Listener(on_move=on_move,on_click=on_click, on_scroll=on_scroll) as listener:
#     listener.join()
#
# # ...or, in a non-blocking fashion:
# listener = mouse.Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll)
# listener.start()
# 从任何地方调用、加注或 return 来停止监听器。pynput.mouse.Listener.stopStopExceptionFalse
# pynput.mouse.Listener.stopStopExceptionFalse

"""                 鼠标侦听器线程
侦听器回调是直接从某些 平台，尤其是 Windows。
这意味着长时间运行的过程和阻塞操作不应 从回调调用，因为这可能会冻结所有进程的输入。
一种可能的解决方法是只将传入消息分派到队列，然后让 单独的线程处理它们。
                    处理鼠标侦听器错误
如果回调处理程序引发异常，则侦听器将停止。因为 callback 在专用线程中运行，则异常不会自动 重新加注。
要收到有关回调错误的通知，请在侦听器上调用 实例：Thread.join
"""
# class MyException(Exception): pass
#
# def on_click(x, y, button, pressed):
#     if button == mouse.Button.left:
#         raise MyException(button)
#
# # Collect events until released
# with mouse.Listener(
#         on_click=on_click) as listener:
#     try:
#         listener.join()
#     except MyException as e:
#         print('{0} was clicked'.format(e.args[0]))
"""         切换 Mouse Listener 的 Listening 事件
一旦被调用，侦听器就不能被 restarted，因为侦听器是 的实例。pynput.mouse.Listener.stopthreading.Thread
如果您的应用程序需要切换侦听事件，则必须添加 internal 标志在不需要时忽略事件，
或者在不需要时创建新的侦听器 恢复侦听。
鼠标侦听器的同步事件侦听
为了简化脚本编写，通过 实用程序类。此类支持读取单个 事件，以及迭代所有事件。pynput.mouse.Events
"""
# 要读取单个事件，请使用以下代码：
# from pynput import mouse

# The event listener will be running in this block
# with mouse.Events() as events:
#     # Block at most one second
#     event = events.get(1.0)
#     if event is None:
#         print('You did not interact with the mouse within one second')
#     else:
#         print('Received event {}'.format(event))
# 要迭代鼠标事件，请使用以下代码：
# from pynput import mouse

# The event listener will be running in this block
# with mouse.Events() as events:
#     for event in events:
#         if event.button == mouse.Button.right:
#             break
#         else:
#             print('Received event {}'.format(event))
# 请注意，iterator 方法不支持非阻塞操作， 因此，它将等待至少一个 mouse 事件。
# 事件将是 中找到的内部类的实例。pynput.mouse.Events
"""
确保 Windows 上 Listener 和 controller 之间的坐标一致
最新版本的 _Windows_ 支持在以下时间运行扩展的旧版应用程序 系统扩展已提高到 100% 以上。
这允许旧的应用程序 按比例缩放，尽管外观模糊，并避免使用微小、无法使用的用户界面。
遗憾的是，这种缩放对鼠标侦听器的应用不一致，而 controller：监听器将接收物理坐标，
但控制器 必须与缩放的坐标一起使用。
这可以通过告诉 Windows 您的应用程序是 DPI 来解决 意识到的。这是一个进程全局设置，
所以 _pynput_ 不能这样做 自然而然。启用 DPI 感知，运行以下代码：
"""
# import ctypes
# PROCESS_PER_MONITOR_DPI_AWARE = 2
# ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)
"""------------------------------------------------键盘------------------------------------------"""
"""控制键盘pynput.keyboard.Controller"""
# 使用如下：pynput.keyboard.Controller
# from pynput.keyboard import Key, Controller
# keyboard = Controller()
# 按下键盘
# keyboard.press(Key.space)
# 抬起键盘
# keyboard.release(Key.space)
# 键盘按下按键a（小写A）
# keyboard.press('a')
# 键盘抬起按键a（小写A）
# keyboard.release('a')
# 键盘按下按键A（大写的a）
# keyboard.press('A')
# 键盘抬起按键A（大写A）
# keyboard.release('A')

# 按住键盘shift时按下a按键和抬起a按键
# with keyboard.pressed(Key.shift):
#     keyboard.press('a')
#     keyboard.release('a')

# 使用快捷键类型方法键入 'Hello World'
# keyboard.type('Hello World')
"""监控键盘pynput.keyboard.Listener"""
from pynput import keyboard
"""
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
"""
"""
键盘侦听器是一个 ，所有回调都将是 从线程调用。threading.Thread

从任何位置调用，从回调引发或返回以停止侦听器。pynput.keyboard.Listener.stopStopExceptionFalse

传递给 callbacks 的参数是 ， for 特殊键、a 表示普通字母数字键，或 仅适用于未知密钥。keypynput.keyboard.Keypynput.keyboard.KeyCodeNone

当使用上面的非阻塞版本时，当前线程将继续 执行。与其他 GUI 框架集成时，这可能是必要的 ，其中包含一个主循环，但是当从脚本运行时，这将导致 程序立即终止。

键盘侦听器线程
侦听器回调是直接从某些 平台，尤其是 Windows。

这意味着长时间运行的过程和阻塞操作不应 从回调调用，因为这可能会冻结所有进程的输入。

一种可能的解决方法是只将传入消息分派到队列，然后让 单独的线程处理它们。
"""
"""
处理键盘侦听器错误
如果回调处理程序引发异常，则侦听器将停止。因为 callback 在专用线程中运行，则异常不会自动 重新加注。

要收到有关回调错误的通知，请在侦听器上调用 实例：Thread.join
"""
# from pynput import keyboard
#
# class MyException(Exception): pass
#
# def on_press(key):
#     if key == keyboard.Key.esc:
#         raise MyException(key)
#
# # Collect events until released
# with keyboard.Listener(
#         on_press=on_press) as listener:
#     try:
#         listener.join()
#     except MyException as e:
#         print('{0} was pressed'.format(e.args[0]))
"""
切换键盘侦听器的事件侦听
一旦被调用，侦听器就不能被 restarted，因为侦听器是 的实例。pynput.keyboard.Listener.stopthreading.Thread

如果您的应用程序需要切换侦听事件，则必须添加 internal 标志在不需要时忽略事件，或者在不需要时创建新的侦听器 恢复侦听。
"""
"""
键盘侦听器的同步事件侦听
为了简化脚本编写，通过 实用程序类。此类支持读取单个 事件，以及迭代所有事件。pynput.keyboard.Events

要读取单个事件，请使用以下代码：
"""
# from pynput import keyboard
#
# # 事件侦听器将在此块中运行
# with keyboard.Events() as events:
#     # Block at most one second
#     event = events.get(1.0)
#     if event is None:
#         print('您没有在 1 秒内按下任何键')
#     else:
#         print('已接收事件 {}'.format(event))

# 要迭代键盘事件，请使用以下代码：
# from pynput import keyboard
#
# # The event listener will be running in this block
# with keyboard.Events() as events:
#     for event in events:
#         if event.key == keyboard.Key.esc:
#             break
#         else:
#             print('Received event {}'.format(event))

# 请注意，iterator 方法不支持非阻塞操作， 因此，它将等待至少一个 Keyboard 事件。
# 事件将是 中找到的内部类的实例。pynput.keyboard.Events
"""
全局热键
键盘显示器的一个常见用例是对全局热键做出反应。
由于 listener 不维护任何状态，涉及多个 key 的热键必须 将此状态存储在某个位置。
pynput 为此提供了类。它 包含两种更新状态的方法，旨在实现轻松互操作 使用键盘侦听器：
并且可以直接作为侦听器传递 回调。
pynput.keyboard.HotKeypynput.keyboard.HotKey.presspynput.keyboard.HotKey.release
"""
# 预期用途如下：
# from pynput import keyboard
#
# def on_activate():
#     print('Global hotkey activated!')
#
# def for_canonical(f):
#     return lambda k: f(l.canonical(k))
#
# hotkey = keyboard.HotKey(
#     keyboard.HotKey.parse('<ctrl>+<alt>+h'),
#     on_activate)
# with keyboard.Listener(
#         on_press=for_canonical(hotkey.press),
#         on_release=for_canonical(hotkey.release)) as l:
#     l.join()
""""
这将创建一个热键，然后使用侦听器更新其状态。一次 同时按下所有指定的键，将 调用。on_activate

请注意，键是在 传递给实例。这是为了删除任何修饰符状态 从关键事件中，并使用多个物理来规范化修饰符 按钮。pynput.keyboard.Listener.canonicalHotKey

该方法是一个方便的函数，用于 将快捷字符串转换为键集合。请参阅其文档 更多信息。pynput.keyboard.HotKey.parse

要注册多个全局热键，请使用 convenience 类 ：pynput.keyboard.GlobalHotKeys
"""
# from pynput import keyboard
#
# def on_activate_h():
#     print('<ctrl>+<alt>+h pressed')
#
# def on_activate_i():
#     print('<ctrl>+<alt>+i pressed')
#
# with keyboard.GlobalHotKeys({
#         '<ctrl>+<alt>+h': on_activate_h,
#         '<ctrl>+<alt>+i': on_activate_i}) as h:
#     h.join()
'''--------------------------------------自我研究-------------------------------------------------'''
from time import sleep
# from threading import Thread
# 键盘监听
from pynput import keyboard
# 按键按键监听
def on_press():
    print(1)
def on_activate_h():
    print('ctrl+alt+h')

def on_activate_i():
    print('ctrl+alt+i')

with keyboard.GlobalHotKeys({'<home>+<alt>+h': on_activate_h,'<ctrl>+<alt>+i': on_activate_i, 'i': on_press}) as h:
    h.join()
















































































































































































































































