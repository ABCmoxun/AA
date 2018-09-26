# 练习：
#   用循环输入文字，将每次输入的文字保存在一个列表L中，
#     当输入空行时结束输入.并打印列表 L 的内容

L = []

while True:
    s = input("请输入字符串: ")
    if s == '':
        break
    L += [s]

print(L)


