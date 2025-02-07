# 这个自定义的库是用来写用户反馈的，包括语音提示等等
# 用户反馈
"""反馈思想（对反馈的内容做分类）
对不同方式的反馈做区分，这可能觉得很傻，没有必要，但是我觉的有必要
1. 字体打印到屏幕上和语音提示是不同的方式，如果一味使用print打印会有局限性，固化思维，需要的语音的时候就完蛋了
2. 这个库本来就是配置界面UI（我的是Qt6）,通过区分不同反馈，利用类和继承复写到界面UI且不影响其他想要反馈方式
3. 对反馈做区分，也能对日志级别有所了解，当然这个反馈也可以复写到不同日志等级里面去
"""
"""
打印用户在ui的选项（交互反馈）当前环境是否能使用脚本（系统反馈），任务开始（状态反馈），完成到那一步（进度反馈），
任务完成（状态反馈），发出声音提示任务完成（声音反馈），用户关闭程序（交互反馈）
"""
class UserFeedback:
    def __init__(self,feedback_type=None,feedback_content=None):    # 传入反馈内容参数
        """
        使用不同的反馈方式,1 是交互反馈,2 是系统反馈, 3 是状态反馈, 4 是进度反馈, 5是声音反馈
        :反馈方式: feedback_type:
        :反馈内容: feedback_content:
        """
        super().__init__()
        if feedback_type or feedback_content: # 参数都填了（开始赋值）用or是怕输入一个参数
            self.feedback_type = feedback_type  # 反馈方式(输入数字)
            self.feedback_content = feedback_content    # 反馈内容
            self.select_feedback_type()     # 调用具体的反馈

    # 反馈方式
    def select_feedback_type(self):
        if self.feedback_type == 1:
            self.interactive_feedback(self.feedback_content)    # 交互反馈
        elif self.feedback_type == 2:
            self.sys_feedback(self.feedback_content)    # 系统反馈
        elif self.feedback_type == 3:
            self.status_feedback(self.feedback_content) # 状态反馈
        elif self.feedback_type == 4:
            self.progress_feedback(self.feedback_content)   # 进度反馈
        elif self.feedback_type == 5:
            self.audio_feedback(self.feedback_content)  # 声音反馈
        else:
            raise ValueError("用户反馈对象输入的参数不在范围内")



    @staticmethod
    def interactive_feedback(feedback_content):
        """交互反馈
        在用户与程序交互时提供即时反馈（如点击按钮后的提示）。"""
        print(feedback_content)  # 默认直接打印，可以复写成反馈表

    @staticmethod
    def sys_feedback(feedback_content):
        """系统反馈
        关于计算机硬件或软件状态的数据，而“反馈”或“显示”则是指将这些信息传达给用户的过程。（如系统类别，分辨率等）"""
        print(feedback_content)

    @staticmethod
    def status_feedback(feedback_content):
        """状态反馈
        实时通知用户程序的当前状态（如“正在加载”、“已完成”等）。"""
        print(feedback_content)    # 默认直接打印，后期复写直接打印到UI上

    @staticmethod
    def progress_feedback(feedback_content):
        """进度反馈
        告知用户当前任务的执行进度（如百分比、步骤等）。"""
        print(feedback_content)  # 默认直接打印，可以复写到UI界面中

    @staticmethod
    def audio_feedback(feedback_content):
        """声音反馈
        描述系统通过声音向用户传达信息或状态更新的过程。（如蜂鸣声或对应的语音包）"""
        print(feedback_content)  # 默认直接打印，可以复写成语音

    # def qq_feedback(self):
    #     """这个暂时不写，先搞主体"""
    #     pass

if __name__ == '__main__':
    print_need = UserFeedback(1,"1")
    print_need.sys_feedback("2")
    UserFeedback.sys_feedback("3")
    UserFeedback().sys_feedback("4")
    UserFeedback(1, "5")
    UserFeedback(1,"6").sys_feedback("7")
