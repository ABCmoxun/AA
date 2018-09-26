# 练习：
# 　　自己写一个Student类,此类的对象有属性name, age, score, 用来保存学生的姓名，年龄，成绩
# 　　　1) 写一个函数 input_student读入n个学生的信息，用对象来存储这些信息（不用字典), 并返回对象的列表
#    2) 写一个函数output_student 打印这些学生信息(格式不限)
#   示意:
#     class Student:
#        pass
# 　　　　def input_student():
#         ...　　# 获取学生信息，形成列表返回
#     def output_student(lst):
#         # 打印学生信息
#     def main():
#         L = input_student()
#         output_student(L)
#     main()

# 练习：
#   修改之前练习的Student类，为该类添加初始化方法，
#     实现在创建对象时自动添加name,age,score属性


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def input_student():
    # 获取学生信息，形成列表返回
    L = []
    while True:
        n = input("请输入姓名: ")
        if not n:
            break
        a = int(input("请输入年龄: "))
        s = int(input("请输入成绩: "))
        stu = Student(n, a, s)
        # stu = Student()  # 创建一个学生对象
        # stu.name = n  # 添加属性
        # stu.age = a
        # stu.score = s
        L.append(stu)  # 将学生对象加入列表中
    return L  # 返回生成的列表给调用者


def output_student(lst):
    # 打印学生信息
    # print(lst)
    for stu in lst:
        print("姓名:", stu.name,
              "年龄:", stu.age,
              "成绩:", stu.score)


def main():
    L = input_student()
    output_student(L)
main()
