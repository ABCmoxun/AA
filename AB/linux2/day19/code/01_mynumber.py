# 01_mynumber.py


# 此示例示意 str(x) 函数 和 repr(x) 函数的重写方法
class MyNumber:
    def __init__(self, value):
        self.data = value

    def __str__(self):
        print("__str__方法被调用")
        return "数字: %d" % self.data

    def __repr__(self):
        '''此方法供repr(obj) 函数调用!'''
        return 'MyNumber(%d)' % self.data

n1 = MyNumber(100)
print(str(n1))  # 此句其实等同于print(n1)
print(n1)
print(repr(n1))  # 它会调用n1.__repr__()方法


