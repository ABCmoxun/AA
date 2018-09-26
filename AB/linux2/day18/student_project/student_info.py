# student_info.py

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
        # 创建一个新的字典
        d = {'name': n,
             'age': a,
             'score': s
             }
        lst.append(d)  # 把字典放入列表中
    return lst


def output_student(lst):
    print("+-----------+--------+---------+")
    print("|   name    |  age   |  score  |")
    print("+-----------+--------+---------+")

    for d in lst:  # d绑定学生信息的字典
        info = "| %9s | %6d | %7d |" % (
            d['name'], d['age'], d['score']
        )
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
               key=lambda stu: stu['score'],
               reverse=True)
    output_student(L)  # 打印排序后的列表


def list_order_by_score_asc():
    L = sorted(docs,
               key=lambda stu: stu['score'],)
    output_student(L)  # 打印排序后的列表


def list_order_by_age_desc():
    L = sorted(docs,
               key=lambda stu: stu['age'],
               reverse=True)
    output_student(L)  # 打印排序后的列表


def list_order_by_age_asc():
    L = sorted(docs,
               key=lambda stu: stu['age'],)
    output_student(L)  # 打印排序后的列表


def save_to_file():
    pass

def read_from_file():
    pass


def show_menu():
    print("1) 添加学生")
    print("2) 显示")
    print("q) 退出")


def main():
    docs = []  # 此列表用于存储所有学生的信息
    while True:
        # 显示菜单
        show_menu()
        # 让用户做出选择
        s = input("请选择: ")
        # 根据用户做出的选择处理相应的事情
        if s == 'q':
            return
        if s == '1':
            docs += input_student()
        elif s == '2':
            output_student(docs)
        # elif .....:
        #     以下同学们自己完成


if __name__ == '__main__':  # 判断当前模块是否作为主模块
    main()
