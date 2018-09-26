# 练习：
#   1. 定义一个类Huamn(人类)
#     有三个属性:
#        姓名: name
#        年龄: age
#        家庭住址: address (可以省略没有)
#     有如下方法：
#        show_info(self) 用来显示人的信息
#        update_age(self) 方法用来让这个人的年龄增加一岁

#     def input_human():
#         输入下此人的信息，姓名为空结束

#     def main():
#         docs = input_human()
#         for h in docs:
#             h.show_info()  # 列出所有人的信息
#         for h in docs:
#             h.update_age()  # 让所有人都长一岁
#         for h in docs:
#             h.show_info()  # 再次列表所有人的信息
#     main()  # 调用主函数运行


class Human:  # 人类
    def __init__(self, n, a, add='未填写'):
        self.name = n
        self.age = a
        self.address = add

    def show_info(self):  # 用来显示人的信息
        print(self.name, '今年', self.age,
              '岁, 家庭住址:', self.address)

    def update_age(self):  # 方法用来让这个人的年龄增加一岁
        self.age += 1

def input_human():
    # 输入下此人的信息，姓名为空结束
    L = []
    while True:
        n = input("请输入姓名: ")
        if not n:
            break
        a = int(input("请输入年龄: "))
        addr = input("请输入家庭住址: ")
        L.append(Human(n, a, addr))
    return L


def main():
    docs = input_human()
    for h in docs:
        h.show_info()  # 列出所有人的信息
    for h in docs:
        h.update_age()  # 让所有人都长一岁
    for h in docs:
        h.show_info()  # 再次列表所有人的信息


main()  # 调用主函数运行
