# 练习：
# 　　list类里只有append向末尾添加一个元素的方法，但没有向列表部添加元素的方法，试想能否为列表在不改变原有功能的基础上添加一个insert_head(n)的方法,在列表的头部添加元素

#     class MyList(list):
#         def insert_head(self, element):
#             ....
#     myl = MyList(range(3, 6)):
#     print(myl)  # [3, 4, 5]
#     myl.insert_head(2)
#     print(myl)  # [2, 3, 4, 5]


class MyList(list):
    def insert_head(self, element):
        self.insert(0, element)


myl = MyList(range(3, 6))
print(myl)  # [3, 4, 5]
myl.insert_head(2)
print(myl)  # [2, 3, 4, 5]
