# UI业务逻辑撰写
from UI_code import Ui_Form   # 导入UI模块
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
import sys

class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent: object = None) -> object:
        super(MyMainForm,self).__init__(parent)
        self.setupUi(self)
        # 添加登录按钮信号和槽。注意display函数不加小括号()
        self.login.clicked.connect(self.display)
        # 添加退出按钮信号和槽。调用close函数
        self.cannel_login.clicked.connect(self.close)

    def display(self):
        # 利用line Edit控件对象text()函数获取界面输入
        username = self.counter_input.text()
        password = self.password_input.text()
        # 利用text Browser控件对象setText()函数设置界面显示
        self.login_status.setText("登录成功!\n" + "用户名是: " + username + ",密码是： " + password)

if __name__ == '__main__':
    # 固定的，PyQt6程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = MyMainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec())









