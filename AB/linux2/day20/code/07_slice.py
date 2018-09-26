

# 此示例示意索引 index 和切片 slice 运算符的重载
class MyList:
    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __getitem__(self, i):
        print("__getitem__被调用", i)
        if type(i) is slice:
            print("正在进行切片操作")
        elif type(i) is int:
            print("正在进行索引操作")
        return self.data[i]

    def __setitem__(self, i, v):
        self.data[i] = v


L1 = MyList([1, -2, 3, -4, 5])
print(L1[::2])


