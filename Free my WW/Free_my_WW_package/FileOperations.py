"""
用来管理控制文件
获取文件的各种信息
控制文件的内容和本身
"""
# 导包
# 自带的包
import os
from math import degrees

#自己的包
from Free_my_WW_package.UserFeedback import *   # 用户反馈

def select_current_all_files(report=True):
    """查询当前目录下的所有文件
    参数report，是否开启用户反馈
    返回值：所有当前目录下的文件全名（列表）
    """
    if report: sys_feedback(f"当前目录下的文件有{os.listdir()}")  # 查看当前目录下的文件
    return os.listdir()

def change_directory(path):
    """更改当前的工作目录
    参数：path（更换后的工作目录）
    """
    try:
        os.chdir(path)
    except():
        raise OSError("目录不能是文件，必须是文件夹")

def get_current_directory(mod=False,report=True):
    """获得当前的目录（默认字符串，mod为True时是返回字节串|乱码）
    参数：
    mod ：默认False，True返回当前目录的字节串
    report ：默认True，是否进行用户反馈
    返回值：当前目录的字符串
    """
    if mod:
         current_directory = os.getcwdb()
    else:
        current_directory = os.getcwd()
    if report:  sys_feedback(f"当前目录:{current_directory}")
    return current_directory

def get_all_files(mod=True):
    """获得目录下的所有的文件
    参数mod 默认True，返回当前目录下的所有文件全名，如果为False返回上级目录的所有文件
    返回值：列表的形式返回当前或上级目录的所有文件
    """
    if mod:
        return os.listdir(path='.')
    else:
        return os.listdir(path='..')

def create_folder(path):
    """创建一个文件夹，即为创建一个目录
    参数（如果仅仅填文件夹的名字就会在当前目录创建文件夹）：
    path ： 填该文件夹的路径
    注意，不必担心导入后创建的文件夹在这个包里面
    返回值（都不是报错，仅仅是返回值）：
    "文件已经存在"（目录已经存在）
    "该路径不存在"（路径中的父目录不存在）
    """
    try:
        os.mkdir(path)
    except(FileExistsError,FileNotFoundError):
        if FileExistsError:
            return "文件已经存在"
        else:
            return "该路径不存在"

def create_folder_ex(path,pass_exist=False):
    """创建文件夹（增强版），多级目录创建
    可以是相对路径，也可以是绝对路径，在路径下的每个目录创建指定名字的文件夹
    即为路径的全目录下都得要有我要创建的文件夹，包括绝对路径的上级全目录
    参数：path（路径）
    pass_exist : 默认false，即使文件夹已经存在也不报错，True为有同名文件夹就报错
    返回值："多级目录创建成功"、"目录已存在""创建目录失败"
    """
    try:
        os.makedirs(path,exist_ok=pass_exist)
        return "多级目录创建成功"
    except FileExistsError:
        return "目录已存在"
    except OSError:
        return "创建目录失败"

def remove_file(path):
    """移除文件"""
    try:
        os.remove(path)
    except(OSError,FileNotFoundError):
        if OSError:
            return "要删除的是目录"
        else:
            return "文件不存在"

def remove_folder():
    """递归删除目录
    
    """


if __name__ == '__main__':
    # print("当前目录下的所有文件:")
    # for i in select_current_all_files(False):
    #     print(i)
    print(1)

