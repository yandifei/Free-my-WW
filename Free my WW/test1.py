# Python + Tkinter 示例（适用于任何 GUI 框架）
import tkinter as tk
import threading

def freeze_ui():
    # 死循环阻塞主线程
    while True:
        pass

root = tk.Tk()
button = tk.Button(root, text="点击冻结界面", command=freeze_ui)
button.pack()
root.mainloop()