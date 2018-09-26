# yanghui.py

def get_next_line(lst):
    # 第1步，先放入一个1
    next_line = [1]  # 先把最左的数放进入
    # 第2步, 计算中间的依懒上一层的那些数
    for i in range(len(lst) - 1):
        next_line.append(lst[i] + lst[i + 1])
    # 第3步, 在最后放入一个1
    next_line.append(1)
    return next_line


def get_yanghui_list(n):
    L = [1]
    yhlist = []  # 创建一个空列表
    for _ in range(n):  # 控制n次循环
        yhlist.append(L)  # 把当前 L存储的一行放入列表
        L = get_next_line(L) # 用当前行来计算出下一行
    return yhlist


L = get_yanghui_list(6)
for x in L:
    print(x)