# 05_iterator.py


class MyList:
    '''定义一个容器类，用于存储任意类型的数据
    其内部的存储方式用list实现'''
    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%s)' % self.data

    def __iter__(self):
        self.cur_pos = 0  # 设置迭代器的起始位置为0
        return self

    def __next__(self):
        if self.cur_pos >= len(self.data):
            raise StopIteration
        index = self.cur_pos
        self.cur_pos += 1  # 将当前位置向后移动准备下次获取
        return self.data[index]  # 返回当前位置的数据


myl = MyList([1, -2, 5, -4])
it = iter(myl)
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break


# for x in myl:  # 可以吗？
#     print(x)
