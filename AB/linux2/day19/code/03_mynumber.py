# 03_mynumber.py


# 此示例示意 数值类型转换函数重写
class MyNumber:
    '''此类是自定义的类，用于表示自定义数字的类型'''
    def __init__(self, v):
        self.data = v

    def __repr__(self):
        return 'MyNumber(%s)' % self.data

    def __int__(self):
        return int(self.data)


n1 = MyNumber('100')
print('n1 =', n1)
print(int(n1))  # 100
# print(float(n1))  # 需要实现 __float__(self) 方法


