# 网格布局，九宫格布局（计算器或是锁屏都有他的身影）
# 导包
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QGridLayout



class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("计算器")

        # 准备数据
        data = {
            0: ["7", "8", "9", "+", "("],
            1: ["4", "5", "6", "-", ")"],
            2: ["1", "2", "3", "*", "<-"],
            3: ["0", ".", "=", "/", "C"],
        }

        # 整体布垂直局
        layout = QVBoxLayout()

        # 输入框
        edit = QLineEdit()
        edit.setPlaceholderText("请输入内容")
        # 把输入框的内容添加到容器中
        layout.addWidget(edit)

        # 网格布局
        grid = QGridLayout()

        # 循环创建追加进去
        for line_number, line_data in data.items():
            # 此时的line_number是第几行, line_data是当前行的数据
            for col_number, number in enumerate(line_data):
                # 此时col_number是第几列, number是要显示的符号
                btn = QPushButton(number)
                # grid.addWidget(btn)
                grid.addWidget(btn, line_number, col_number)

        # 把网格布局追加到容器中
        layout.addLayout(grid)

        self.setLayout(layout)










if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    sys.exit(app.exec())