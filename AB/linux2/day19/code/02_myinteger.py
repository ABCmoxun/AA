# 02_myinteger.py


# 此示例示意abs(obj) 函数的重写方法 obj.__abs__() 方法的使用
class MyInteger:
    def __init__(self, value):
        self.data = value

    def __repr__(self):
        return 'MyInteger(%d)' % self.data

    def __abs__(self):
        if self.data < 0:
            return MyInteger(-self.data)  # 创建一个新的以对象并返回
        return MyInteger(self.data)

    def __len__(self):
        '''len(x)函数规定只能返回整数值，
        因此此方法不能返回字符串等其它类型的值'''
        return 100

I1 = MyInteger(-10)
print(I1)   # <-- 此处等同于print(str(I1))
I2 = abs(I1)  # I2 = MyInteger(10)
print(I2)  # MyInteger(10)
print(len(I1))  # I1.__len__()
