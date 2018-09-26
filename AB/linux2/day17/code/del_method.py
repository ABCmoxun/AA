# del_method.py


class FileManage:
    """定义一个文件管理员类"""
    def __init__(self, filename='a.txt'):
        self.file = open(filename, 'w')

    def writeline(self, string):
        self.file.write(string)
        self.file.write('\n')

    def __del__(self):
        """析构方法会在对象销毁前自动调用"""
        self.file.close()
        print("文件已关闭")

fm = FileManage()
fm.writeline("hello world")
fm.writeline("这是中文写的第二行")

del fm
while True:  # 死循环永远不退出
    pass

print("程序结束")

