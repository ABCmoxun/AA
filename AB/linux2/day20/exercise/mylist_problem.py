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


print("------算法1-----")
a = MyList([100])
def test(x):
    x = x + x
    print(x)
test(a)
print(a)

print("------算法2-----")
a = MyList([100])
def test(x):
    x += x  # 此处与上题不同。结果也会不同
    print(x)
test(a)
print(a)


# print("------算法1-----")
# a = [100]
# def test(x):
#     x = x + x
#     print(x)
# test(a)
# print(a)

# print("------算法2-----")
# a = [100]
# def test(x):
#     x += x  # 此处与上题不同。结果也会不同
#     print(x)
# test(a)
# print(a)
