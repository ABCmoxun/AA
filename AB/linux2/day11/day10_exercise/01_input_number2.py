
L = []
def input_number():
    lst = []
    while True:
        i = int(input("请输入数字(-1结束):"))
        if i == -1:
            break
        lst.append(i)
    global L
    L = lst  # 改变变量

input_number()
print("您刚才输入的整数值是:", L)
