# 2. 已知内建函数 max的帮助文档为:
#   max(...)
#      max(iterable) -> value
#      max(arg1, arg2, *args) -> value
#   访造max,写一个mymax函数,实现功能与max完全相同
# 测试用例:
#   print(mymax([6,8,3,5]))  # 8
#   print(mymax(100, 200))   # 200
#   print(mymax(1,3,9,7,5))  # 9

# 方法1
# def mymax(*args):
#     if len(args) == 1:
#         L = list(*args)  # 放到一个列表里
#         L.sort(reverse=True)
#         return L[0]
#     elif len(args) >= 2:
#         L = list(args)
#         L.sort(reverse=True)
#         return L[0]


# 方法2
# def mymax(a, *args):
#     if len(args) == 0:
#         # return max(a)
#         m = a[0]  # 先假设第一个数最大
#         i = 1
#         while i < len(a): # 遍历之后的每一个元素
#             if a[i] > m:  # 如果此元素比m大,则让m绑定大的一个
#                 m = a[i]
#             i += 1
#         return m  # 最后m一定绑定一个最大的
#     else:
#         m = a
#         for x in args:
#             if x > m:
#                 m = x
#         return m

# 方法3
def mymax(a, *args):
    def _max(*args):
        # 此函数用于求args元组的最大值
        m = args[0]  # 先假设第一个数最大
        i = 1
        while i < len(args):  # 遍历之后的每一个元素
            if args[i] > m:  # 如果此元素比m大,则让m绑定大的一个
                m = args[i]
            i += 1
        return m  # 最后m一定绑定一个最大的

    if len(args) == 0:
         return _max(*a)
    return _max(a, *args)


print(mymax([6, 8, 3, 5]))  # 8
print(mymax(100, 200))   # 200
print(mymax(1, 3, 9, 7, 5))  # 9
