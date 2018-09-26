# 04_bool.py


# 此示例示意 bool 真值测试函数的重写
class MyList:
    '''定义一个容器类，用于存储任意类型的数据
    其内部的存储方式用list实现
    '''
    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%s)' % self.data

    def __len__(self):
        print("__len__ 方法被调用!")
        return len(self.data)  # 返回列表的长度

    def __bool__(self):
        print('__bool__方法被调用')
        '''此方法用于bool(obj) 函数取值，优先取此函
        数的返回值，此方法用于定义bool(obj)的取值规则'''
        # 规则，所有元素的和为0,则返回False否则返回True
        return sum(self.data) != 0

myl = MyList([1, -2, 5, -4])
print(myl)
print('bool(myl) =', bool(myl))
if myl:
    print('myl 的布尔值为True')
else:
    print('myl 的布尔值为False')

