# 练习:
#   1. 写一个函数mymax, 返回两个数的最大值
#    如:
#       def mymax2(a, b):
#           ...
#       print(mymax(100, 200))  # 200
#       print(mymax("ACD", "ABCD"))  # ACD
#  

# def mymax2(a, b):
#     if a > b:
#         s = a
#     else:
#         s = b
#     return s

# 方法2
def mymax2(a, b):
    if a > b:
        return a
    return b

print(mymax2(100, 200))  # 200
print(mymax2("ACD", "ABCD"))  # ACD
