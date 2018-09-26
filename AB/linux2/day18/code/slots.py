# slots.py


# 此示例示意__slots__属性的用法
class Student:
    # 限定此的类创建的对象只能有name和age两个属性
    __slots__ = ['name', 'age']

    def __init__(self, n, a):
        self.name = n
        self.age = a


s1 = Student("小张", 20)
# s1.Age = 21  # 此时是错写了age为Age, 会报错
# print(s1.__dict__) # 出错，因为没有__dict__字典


