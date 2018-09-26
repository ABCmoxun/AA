

# 此示例示意一元运算符的重载
class MyList:
    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __neg__(self):
        print("__neg__方法被调用!")
        L = (-x for x in self.data)
        return MyList(L)


L1 = MyList([1, -2, 3, -4, 5])
print("L1 =", L1)
L2 = -L1
print("L2 =", L2)
