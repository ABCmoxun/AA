# 2. 写一个函数input_number() 此函数用于读取用户输入的多个整数(用户输入负数时结束输入)
# 将用户输入的数形成列表返回给调用者
#     def input_number():
#         ... # 此处自己完成

#     L = input_number()
#     print("您输入的最大数是:", max(L))
#     print("您输入的这些数的和是:", sum(L))


# 方法1
# def input_number():
#     lst = []  # 临时列表用于存储 用户输入的数据
#     while True:
#         i = int(input("请输入正整数: "))
#         if i < 0:
#             break
#         # 如果i为大于等于0的数,把i放入列表
#         lst.append(i)
#     return lst

# 方法2
def input_number():
    lst = []  # 临时列表用于存储 用户输入的数据
    while True:
        i = int(input("请输入正整数: "))
        if i < 0:
            print("i为小于零的数,返回lst")
            return lst
        # 如果i为大于等于0的数,把i放入列表
        lst.append(i)
    print("最后一条return 语句将被执行")
    return lst  # <<<---永远不会被执行


L = input_number()
print("您输入的最大数是:", max(L))
print("您输入的这些数的和是:", sum(L))
