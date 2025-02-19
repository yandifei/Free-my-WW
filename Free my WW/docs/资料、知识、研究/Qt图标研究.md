# <center>Qt图标研究</center>
# 选择资源文件（qrc）和选择文件
**我搞了好久才发现在PyQt6中qrc模块确实已经在python里面走不通了，即使我能制作qrc，但是无法转为能使用的py文件，官方用了MCake取代，但是pyside6和PyQt5应该还能用**
花了一天时间去研究这个，功夫不负有心人，我终于找到了PyQt6的调用资源的方法，官方确实已经不在PyQt6支持rcc了，但是在pyqt6-tool的文件下，有rcc.exe，这证明还没完全脱离
```python
# 进入你的环境，在pycharm的终端使用cd进入到你的qrc文件所在目录，使用下面的指令（非官方提供）
rcc -g python -o 转后的文件名.py 你的qrc文件
```
***最重要的一步***
转换完成后必须一定要打开你转换之后的py文件修改.
原来的文件开头
```python
# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 5.15.2
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

```
一定要把`from PySide2 import QtCore`改成`from PyQt6 import QtCore`这样才可以正常使用
搞了我一天，官方文档、B站视频、国外的qtdesigner的qtdesigner教学
***
**基本报废**
## 1. 通过资源文件（.qrc）添加图标
资源文件（.qrc）：.qrc 文件是 Qt 的资源文件，用于将图片、图标等资源嵌入到应用程序中。资源文件会将所有资源编译到应用程序的可执行文件中，因此资源在运行时是内嵌的，不需要外部文件支持。
pyrcc.exe 是 PyQt 资源编译器，用于将 .qrc 资源文件（如图标、图片等）编译为 Python 可识别的 .py 文件。
但在 PyQt6 中，官方不再直接提供 pyrcc.exe，而是建议使用 Qt 原生的 rcc 工具 + PyQt6 的兼容接口。
PyQt6 默认不提供 pyrcc.exe，需使用 Qt 的 rcc 或安装 pyqt6-tools 获取 pyrcc6.exe。
直接使用指令吧pyrcc6 -o output.py input.qrc
    我在这里找到rcc的B:\Pycharm\Anaconda3\envs\Qt6_study\Lib\site-packages\qt6_applications\Qt\bin\rcc.exe
    编译后编码格式不是utf8，得自己改
查询官方文档：qrc转py文件：
```python
rcc -g python Free_my_WW_QRC.qrc > Free_my_WW_QRC.py
"""原来的rcc6 -o Free_my_WW_QRC.py Free_my_WW_QRC.qrc
无论加不加utf8都会乱码，我估计的全路径英文开弄好"""
```
在你的qrc文件开头必须加上这行代码，不然乱码
```qrc
<?xml version="1.0" encoding="UTF-8"?>
```
外部qrc工具配置
```python
# 名称和描述：PyQRC
# 程序：B:\Pycharm\Anaconda3\envs\Qt6_study\python.exe，自己的python.exe路径，记得要在环境里面的
# 实参：
rcc -g python $FileName$ > $FileNameWithoutExtension$.py
# 工作目录：
$FileDir$
"""报错，使用官方指令直接报错
Traceback (most recent call last):
  File "D:\鸣潮脚本\Free-my-WW\Free my WW\Free my WW.py", line 18, in <module>
    import Free_my_WW_UI.images.Free_my_WW_QRC
ValueError: source code string cannot contain null bytes
"""
```
实际研究发现，只要遵守好不改变图标的路径和图标名称以及ui文件的总目录，把整个项目变了位置ui依旧正常，即使ui文件的名称变了也行。把ui文件和图片放在同一个目录文件夹下就ok了
优点：
1. 资源内嵌：资源文件会被编译到应用程序中，运行时不需要依赖外部文件。
2. 路径管理简单：资源文件中的资源可以通过统一的路径访问，避免了文件路径问题。
3. 便于分发：由于资源已经嵌入到可执行文件中，分发应用程序时不需要额外分发资源文件。

缺点：
1. 增加可执行文件大小：资源文件会增大可执行文件的大小。
2. 修改不便：如果资源需要更新，必须重新编译应用程序。

**转换报废而已**
***
## 2. 直接选择文件（如图片文件）
直接选择文件：这种方式是直接选择一个外部的图片文件（如 .png、.ico 等）作为图标。
优点：
1.  灵活性高：可以随时更换图标文件，而不需要重新编译应用程序。
2. 可执行文件较小：图标文件不会嵌入到可执行文件中，因此可执行文件的大小较小。

缺点：
1. 依赖外部文件：应用程序运行时需要依赖外部的图标文件
2. 如果文件丢失或路径错误，图标将无法显示。
3. 路径管理复杂：需要确保图标文件的路径正确，尤其是在跨平台或分发应用程序时。

# 在Qtdesigner使用资源文件（PyQt6）
## 1. 创建 .qrc 文件
.qrc 文件是一个 XML 格式的文件，用于定义资源。你可以手动创建它，或者使用 Qt Designer 自动生成。
手动创建 .qrc 文件
1.在你的项目目录中创建一个新文件，命名为 resources.qrc（文件名可以自定义）。
2.编辑 resources.qrc 文件，内容如下：
```xml
<RCC>
    <qresource prefix="/">
        <file>images/image1.png</file>
        <file>images/image2.png</file>
        <file>images/image3.png</file>
        <file>images/image4.png</file>
        <file>images/image5.png</file>
    </qresource>
</RCC>
```
`<qresource prefix="/">`：prefix 是资源的路径前缀，可以自定义。

`<file>`：指定每个图片文件的路径。这里的路径是相对于 .qrc 文件的位置。
## 2. 将 .qrc 文件编译为 Python 模块
Qt 的资源文件（.qrc）需要编译为 Python 模块才能在 PyQt6 中使用。可以使用 pyside6-rcc 或 pyrcc5 工具来完成编译。
1. 需要有yside6-rcc，安装了PyQt6就有了，这是其中的一个模块
bash
2. 编译 .qrc 文件
在终端中运行以下命令：
pyside6-rcc resources.qrc -o resources_rc.py

resources.qrc：是你的资源文件。
resources_rc.py：是生成的 Python 模块文件。
生成的 resources_rc.py 文件会包含所有资源的二进制数据。
3. 在 PyQt6 中使用资源
在你的 PyQt6 代码中，导入生成的 resources_rc.py 文件，然后通过资源路径使用图片。

例如：
```python
from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtGui import QPixmap
import resources_rc  # 导入生成的资源模块

app = QApplication([])

# 使用资源路径加载图片
label = QLabel()
pixmap = QPixmap(":/images/image1.png")  # 注意路径前缀 ":"
label.setPixmap(pixmap)
label.show()

app.exec()
```
:/images/image1.png：是资源路径，: 表示资源文件的根目录，/images/image1.png 是你在 .qrc 文件中定义的路径。

## 在qtdesigner使用资源文件
1. 打开 Qt Designer。
2. 在设计界面中，选择一个需要设置图标的控件（例如 QPushButton）。
3. 在属性编辑器中，找到 icon 属性，点击右侧的 ... 按钮。
4. 在弹出的窗口中，点击 笔 图标，选择 编辑资源。
5. 在资源编辑器中，点击 添加资源，选择你编译好的 resources_rc.py 文件。
6. 选择你需要的图标资源，点击 确定。









