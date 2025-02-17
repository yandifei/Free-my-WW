import time
import cv2
import numpy as np
from mss import mss
# 极大概率安装失败
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python


def monitor_fps(region=None, verbose=True):
    """
    实时监测屏幕区域帧率
    :param region: 监测区域 (left, top, width, height)，默认全屏
    :param verbose: 是否显示实时信息
    """
    # 初始化参数
    fps = 0
    prev_time = 0
    with mss() as sct:
        # 设置监测区域
        monitor = sct.monitors[1] if not region else {
            "left": region[0],
            "top": region[1],
            "width": region[2],
            "height": region[3]
        }

        try:
            while True:
                # 捕获屏幕区域
                sct_img = sct.grab(monitor)
                curr_time = time.time()

                # 计算FPS
                if prev_time != 0:
                    fps = 1 / (curr_time - prev_time)
                prev_time = curr_time

                # 显示信息
                if verbose:
                    frame = np.array(sct_img)
                    cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv2.imshow('FPS Monitor', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    print(f"\rCurrent FPS: {fps:.1f}", end="")

        except KeyboardInterrupt:
            pass
        finally:
            if verbose:
                cv2.destroyAllWindows()
            print("\nMonitoring stopped.")


if __name__ == "__main__":
    # 示例：监测屏幕左上角 800x600 区域
    monitor_fps(region=(0, 0, 800, 600))