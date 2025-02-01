# 提供了多页面切换的布局，一次只能看到一个界面。抽屉布局
# 导包
from PyQt6.QtWidgets import QApplication, QStackedWidget, QWidget, QVBoxLayout, QPushButton, QLabel
import sys


class Window1(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("我是抽屉1要显示的内容", self)
        self.setStyleSheet("background-color:green;")

class Window2(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("我是抽屉2要显示的内容", self)
        self.setStyleSheet("background-color:green;")


class MyWindow(QWidget):
    def __init__(self):
        DeprecationWarning()
        self.create_stacked_layout()
        self.init_ui()

    def create_stacked_layout(self):
        # 创建堆叠（抽屉）布局
        self.stacked_layout = QStackedWidget()
        # 创建单独的Widget
        win1 = Window1()
        win2 = Window1()
        # 将创建的2个Widget添加到抽屉布局器中
        self.stacked_layout.addWidget(win1)
        self.stacked_layout.addWidget(win2)

    def init_ui(self):
        # 设置Widget大小及固定宽高
        self.setFixedSize(500, 500)

        # 1.创建整体的布局器
        container = QVBoxLayout()

        # 2.创建一个要显示具体内容的子Widget
        widget = QWidget()
        widget.setLayout(self.stacked_layout)
        widget.setStyleSheet("background-color:grey;")

        # 3.创建2个按钮，用来点击进行切换抽屉布局器中的Widget
        btn_press1 = QPushButton("抽屉1")
        btn_press2 = QPushButton("抽屉2")
        # 给按钮添加事件(即点击后要调用的函数)
        btn_press1.clicked.connect(self.btn_press1_clicked)
        btn_press2.clicked.connect(self.btn_press2_clicked)

        # 4.将需要显示的空间添加到布局器中
        container.addWidget(widget)
        container.addWidget(btn_press1)
        container.addWidget(btn_press2)

        # 5.设置当前要显示的Widget，从而能够显示这个布局器中的控件
        self.setLayout(container)

    def btn_press1_clicked(self):
        # 设置抽屉布局器的当前索引值，即可切换显示哪个小组件
        self.stacked_layout.setCurrentIndex(0)
        
    def btn_press2_clicked(self):
        # 设置抽屉布局器的当前索引值，即可切换显示哪个小组件
        self.stacked_layout.setCurrentIndex(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = MyWindow()
    win.show()

    sys.exit(app.exec())