# 02_mylist.py


# 此示例示意返向算术运算符的重载
class MyList:
    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%r)' % self.data

    # def __add__(self, rhs):
    #     return MyList(self.data + rhs.data)

    def __mul__(self, rhs):
        return MyList(self.data * rhs)

    def __rmul__(self, lhs):
        print("__rmul__被调用, lhs=", lhs)
        return MyList(self.data * lhs)  # lhs (left hand side)


L1 = MyList([1, 2, 3])
L2 = MyList(range(4, 7))
L4 = L1 * 2  # 实现乘法运算
print('L4 =', L4)  # MyList([1,2,3,1,2,3])
L5 = 2 * L1  # 可以吗？
print(L5)

