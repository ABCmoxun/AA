# student_info.py


from student import Student

# 此列表用来记录全部的学生信息
docs = []  # 此列表用于存储所有学生的信息


def input_student():
    lst = []  # 创建一个空列表用于存储学生的信息(字典)
    while True:
        n = input("请输入学生姓名: ")
        if not n:
            break
        a = int(input("请输入学生年龄: "))
        s = int(input("请输入学生成绩: "))
        stu = Student(n, a, s)
        lst.append(stu)  # 把字典放入列表中
    return lst


def output_student(lst):
    print("+-----------+--------+---------+")
    print("|   name    |  age   |  score  |")
    print("+-----------+--------+---------+")

    for stu in lst:
        info = "| %9s | %6d | %7d |" % stu.get_infos()
        print(info)

    print("+-----------+--------+---------+")


#  ------- 以下函数都是提供给其它模块的接口-------
def add_student():
    """添加学生的函数供模它模块调用"""
    global docs
    docs += input_student()


def list_all_student():
    """列表所有学生信息的函数供其它模块调用"""
    output_student(docs)


def list_order_by_score_desc():
    L = sorted(docs,
               key=lambda stu: stu.get_score(),
               reverse=True)
    output_student(L)  # 打印排序后的列表


def list_order_by_score_asc():
    L = sorted(docs,
               key=lambda stu: stu.get_score())
    output_student(L)  # 打印排序后的列表


def list_order_by_age_desc():
    L = sorted(docs,
               key=lambda stu: stu.get_age(),
               reverse=True)
    output_student(L)  # 打印排序后的列表


def list_order_by_age_asc():
    L = sorted(docs,
               key=lambda stu: stu.get_age())
    output_student(L)  # 打印排序后的列表


def save_to_file():
    try:
        f = open('si.txt', 'w')
        for stu in docs:
            stu.write_to_file(f)
        f.close()
    except IOError:
        print("保存失败")

def read_from_file():
    pass

