# 3. 已知有列表:
#    L = [[3,5,8], 10, [[13, 14], 15], 18]
#   1) 写一个函数 print_list(lst) 打印出列表中所有数字
#     print_list(L)
#   2) 写一个函数sum_list(lst) 返回列表中所有数字的和
#     print(sum_list(L))  # 86
#   注:
#     type(x) 可以返回一个变量的类型
#     如:
#        >>> type(20) is int  # True
#        >>> type([1,2,3]) is list  # True


L = [[3, 5, 8], 10, [[13, 14], 15], 18]


#   1) 写一个函数 print_list(lst) 打印出列表中所有数字
def print_list(lst):
    for x in lst:
        if type(x) is list:
            print_list(x)
        else:
            print(x)


#   2) 写一个函数sum_list(lst) 返回列表中所有数字的和
def sum_list(lst):
    s = 0
    for x in lst:
        if type(x) is list:
            s += sum_list(x)
        else:
            s += x
    return s


print_list(L)
print('列表L的和是:', sum_list(L))  # 86
