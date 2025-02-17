# <center>Qt图标研究</center>
# 选择资源文件（qrc）和选择文件
## 1. 通过资源文件（.qrc）添加图标
资源文件（.qrc）：.qrc 文件是 Qt 的资源文件，用于将图片、图标等资源嵌入到应用程序中。资源文件会将所有资源编译到应用程序的可执行文件中，因此资源在运行时是内嵌的，不需要外部文件支持。
优点：
1. 资源内嵌：资源文件会被编译到应用程序中，运行时不需要依赖外部文件。
2. 路径管理简单：资源文件中的资源可以通过统一的路径访问，避免了文件路径问题。
3. 便于分发：由于资源已经嵌入到可执行文件中，分发应用程序时不需要额外分发资源文件。

缺点：
1. 增加可执行文件大小：资源文件会增大可执行文件的大小。
2. 修改不便：如果资源需要更新，必须重新编译应用程序。
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









