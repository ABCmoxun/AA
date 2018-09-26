# 09_star_tuple_argument.py


# 此示例示意 星号元组形参
def func(*args):
    print("实参个数是:", len(args))
    print("args的值是:", args)


func(1, 2, 3)
func("ABCD", 3.14, 100, True, None)


