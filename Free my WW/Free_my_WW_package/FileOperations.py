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
    """移除文件，不删除目录
    返回值：
    "要删除的不能是目录，必须是文件"
    "文件不存在"
    """
    try:
        os.remove(path)
    except(OSError,FileNotFoundError):
        if OSError:
            return "要删除的不能是目录，必须是文件"
        else:
            return "文件不存在"

def remove_folder_ex(path):
    """递归删除目录，如果删除的目录下面有文件就停止删除
    如果成功删除了末尾一级目录，removedirs() 会尝试依次删除 path 中提到的每个父目录，直到抛出错误为止
    参数：
    path ： 填目录路径（不能填文件的路径，一定要是文件夹的路径）
    返回值：路径错误
    """
    try:
        os.removedirs(path)
    except OSError:
        sys_feedback("路径错误")

def change_name(old_name,new_name,mod):
    """修改文件或目录的名字(在linux中文件和目录都是File)
    特性         os.rename()	     os.renames()
    功能	    重命名文件或目录	    递归重命名并创建目录
    目标已存在	抛出异常	            抛出异常
    跨设备支持	不支持	            不支持
    自动创建目录	不支持	            支持
    适用场景	    简单重命名	        需要创建父目录
    参数:
    old_name : 旧路径(文件或目录)
    new_name : 新路径(文件或目录)
    mod : 模式(1:os.rename()  2:os.renames())
    """
    # 只能修改单个目录或文件的名字，目录和文件必须都存在才能修改，修改后的目录或文件不能是已经存在的
    if mod == 1:
        try:
            os.rename(old_name,new_name)
        except IsADirectoryError:
            return "目录已存在"
        except FileExistsError:
            return "文件已存在"
        except PermissionError:
            return "权限不足，无法重命名文件"
        except OSError:
            return "文件或目录不存在"
    # 如果文件已经存在则会移动文件到新路径下，新路径不存在会自动创建目录后吧新文件移动到该目录下，如果创建的目录存在则报错
    elif mod == 2:
        try:
            os.renames(old_name, new_name)
        except():
            return "新路径已有同名的目录或文件，无法创建"

def replace_file_or_folder(old_path, new_path):
    """移动并覆盖目标
    将文件或目录 old_path 重命名为 new_path。如果 new_path 是非空目录，将抛出 OSError 异常。
    如果 new_path 已存在且为文件，则在用户具有权限的情况下，将对其进行静默替换。
    参数:
    old_path : 填入覆盖的文件或路径
    new_path : 填入需要覆盖的文件或路径
    """
    try:
        os.replace(old_path, new_path)
    except OSError:
        return "覆盖文件或目录的路径错误"

def move_folder(path):
    """删除目录（如果目录不存在或不为空）
    参数：
    path ： 填入空目录的路径
    返回值：
    "目录不存在"
    "目录不为空"
    """
    try:
        os.rmdir(path)
    except FileNotFoundError:
        return "目录不存在"
    except OSError:
        return "目录不为空"

def save_all_files():
    """强制将系统缓冲区中的所有数据写入物理存储设备（如硬盘、SSD）
    强制将内核缓冲区（缓存）中的文件数据和元数据（如文件大小、修改时间等）同步到磁盘
    返回值 ： 所有数据均已保存
    """
    os.sync()
    return "所有数据均已保存"

def limit_file_length(file_path,length):
    """限制文件字节大小或扩展文件内容（如果文件未满，则填充满\x00，如果以慢则删除超出文件大小的内容）
    参数：
    file_path ： 文件路径
    length ： 文件的字节长度（超过就删、截断）
    """
    os.truncate(file_path, length)

def remove_folder(path):
    """删除指定目录
    返回值："未找到该文件"
    """
    try:
        os.unlink(path)
    except():
        return "未找到该文件"

def set_file_time(path,time):
    """设置文件的修改时间（用于数据备份、测试调试、文件同步）
    参数：
    path ： 文件的路径
    time : 元组：(2023, 1, 1, 0, 0, 0, 0, 0, 0) 2023-01-01 00:00:00
    """
    os.utime(path, time)

def traverse_files_folders(path, topdown=False):
    """遍历所有文件和目录
    参数：
    path ： 遍历的路径（绝对路径或相对路径）
    topdown=True（默认）：父目录先于子目录遍历（自上而下），允许动态修改 dirnames 以跳过某些子目录。
    topdown=False：子目录先遍历，父目录最后遍历（自下而上），适合删除目录等需先处理子内容的场景。
    返回值：
    root ： 根目录
    folders_name ： 所有文件夹（根目录下的所有目录）
    files_name ： 目录的所有文件
    all_file_path : 所有文件的路径
    all_folder_path : 所有目录的路径
    """
    root = None
    folders_name = []   # 放所有文件夹的名
    files_name = [] # 放所有文件的名字
    all_file_path = []  # 设置一个空列表来放文件的路径
    all_folder_path = []    # 设置一个空列表来放文件夹（目录）的路径
    for root, folders, files in os.walk(path,topdown):
        globals()
        folders_name.append(folders)
        files_name.append(files)
        for file_name in files:
            all_file_path.append(os.path.join(root, file_name)) # 根目录和文件名的拼接，把路径存放到列表中
        for folder_name in folders:
            all_folder_path.append(os.path.join(root, folder_name))   # 根目录和文件夹的拼接，把路径存放到列表中
    return root, folders_name, files_name, all_file_path, all_folder_path





if __name__ == '__main__':
    # print("当前目录下的所有文件:")
    # for i in select_current_all_files(False):
    #     print(i)
    # print(1)
    # remove_folder("B:\\测试\\测试\\测试")
    # print(change_name("B:\测试\测试1\测试2","B:\测试\测试1\测试5",1))
    # print(change_name("B:\测试.txt","B:\测试1\测试1\测试3\测试.txt",2))
    # replace_file_or_folder("B:\测试1.txt","B:\测试\测试")
    # print(move_folder_ex("B:\\测试sefew"))
    # print(remove_file("B:\测试\测试"))
    # remove_folder("B:\测试\新建 文本文档.txt")
    # for i in traverse_files_folders("B:\学籍与个人电子设备图片"):
    #     print(i)
    # print(os.cpu_count())
    print(os.sep)