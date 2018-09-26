# 1. 创建一个列表L = []
#    写一个函数 input_number读取数据放入列表L中
#   程序如下:
#     L = []
#     def input_number():
#         # 此处自己加入代码
#         while True:
#             i = int(input("请输入数字(-1结束):"))
#         # 此处自己完成
#     input_number()
#     print("您刚才输入的整数值是:", L)


L = []
def input_number():
    # 此处自己加入代码
    while True:
        i = int(input("请输入数字(-1结束):"))
        if i == -1:
            break
        L.append(i)  # 此时我并没有改变L的绑定关系

input_number()
print("您刚才输入的整数值是:", L)
