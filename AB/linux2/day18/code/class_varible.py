# class_varible.py


# 此示例示意 类变量的用余和使用方法
class Human:
    total_count = 0  # 类变量，用于记录对象的个数
    def __init__(self, name):
        self.name = name
        self.__class__.total_count += 1  # 人数加人
        print(name, "对象创建")

    def __del__(self):
        self.__class__.total_count -= 1  # 总人数减1

print("当前对象的个数是:", Human.total_count)  # 0
h1 = Human("张飞")
h2 = Human("赵云")
print("当前对象的个数是:", Human.total_count)  # 2
del h2  # 或 h2 = None
print("当前对象的个数是:", Human.total_count)  # 1
