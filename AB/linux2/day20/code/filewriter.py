# filewriter.py


# 本程序示意自定义的类作为环境管理器使用
class FileWriter:
    def __init__(self, filename):
        self.filename = filename  # 此属性用于记住文件名

    def writeline(self, s):
        '''此方法用于向文件内写入字符串，同时自动添加换行'''
        self.file.write(s)
        self.file.write('\n')

    def __enter__(self):
        '''此方法用于实现环境管理器'''
        self.file = open(self.filename, 'w')
        print("已进入__enter__方法，文件打开成功")
        return self  # 返回值向用于 with中的as 绑定

    def __exit__(self, exec_type, exec_value, exec_tb):
        '''
        exec_type  为异常类异,没有异常发生时为None
        exec_value 为错误的对象,没有异常时为None
        exec_tb    为错误的traceback对象
        '''
        self.file.close()
        print("文件", self.filename, "已经关闭")
        if exec_type is None:
            print("退出with时没有发生异常")
        else:
            print("退出with时，有异常，类型是", exec_type,
                  "错误是", exec_value)
        print("__exit__法被调用,已离开with语句")


try:
    with FileWriter('log.txt') as fw:
        while True:
            s = input("请输入一行: ")
            if s == 'exit':
                break
            if s == 'error':
                raise ValueError("故意制造的值错误")
            fw.writeline(s)
except:
    print("有错误发生，已转为正常")

print("这是with语句之外，也是程序的最后一条语句")