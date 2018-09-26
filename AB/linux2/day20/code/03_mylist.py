# 02_mylist.py


# 此示例示意复合赋值算术运算符的重载
class MyList:
    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __add__(self, rhs):
        print("__add__方法被调用")
        return MyList(self.data + rhs.data)

    def __iadd__(self, rhs):
        print("__iadd__方法被调用")
        self.data.extend(rhs.data)
        return self

L1 = MyList([1, 2, 3])
L2 = MyList(range(4, 7))
print("id(L1) =", id(L1))
L1 += L2  # 相当于 L1 = L1 + L2
print('L1 =', L1)
print("id(L1) =", id(L1))


