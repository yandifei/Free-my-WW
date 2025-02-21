import sys
import time
from PyQt6.QtWidgets import QApplication, QMainWindow, QSplashScreen, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon, QPixmap, QMovie
from PyQt6.QtCore import Qt, QTimer

def main():
    # 创建应用实例
    app = QApplication(sys.argv)

    # ----------------------------
    # 1. 创建启动画面
    # ----------------------------
    # 方式1：静态图片（支持PNG/JPG）
    splash_pix = QPixmap("splash_icon.png")  # 替换为你的图片路径
    # 方式2：动态GIF（加载动画）
    # splash_movie = QMovie("loading.gif")  # 动态加载图标

    # 创建启动窗口（设置置顶）
    splash = QSplashScreen(splash_pix, Qt.WindowType.WindowStaysOnTopHint)
    splash.setWindowIcon(QIcon("app_icon.ico"))  # 设置任务栏图标

    # 添加自定义文字（可选）
    splash.showMessage(
        "正在加载...",
        alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter,
        color=Qt.GlobalColor.white
    )

    # 方式2：启动动态GIF
    # splash = QSplashScreen()
    # splash.setMovie(splash_movie)
    # splash_movie.start()

    splash.show()

    # ----------------------------
    # 2. 模拟耗时初始化操作
    # ----------------------------
    # 例如：加载数据、初始化资源等
    time.sleep(2)  # 实际开发中替换为真实代码

    # ----------------------------
    # 3. 创建并显示主窗口
    # ----------------------------
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("主窗口")
            self.setGeometry(100, 100, 400, 300)
            # 添加一个示例组件
            label = QLabel("欢迎使用！", self)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    window = MainWindow()
    window.show()

    # ----------------------------
    # 4. 关闭启动画面
    # ----------------------------
    splash.finish(window)  # 主窗口显示后关闭启动画面
    # 方式2：动态GIF需额外停止动画
    # splash_movie.stop()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()