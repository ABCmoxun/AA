# global_statement.py


# 以下示例示意global语句的用法
v = 100


def fx():
    global v  # 声明v为全局变量,不是局部变量
    v = 200  # 想修改全局的v怎么办?


fx()
print(v)  # 200


# 4. global变量列表里的变量名不能出现在此作用域内的形参列表里
def f1(v):
    global v
    print(v)


f1(300)