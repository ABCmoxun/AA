# 练习：
#   写一个程序，读入任意行的文字数据，当输入空行时结束输入
#   打印带有行号的输入结果:
#   如:
#   请输入: hello<回车>
#   请输入: tarena<回车>
#   请输入: bye<回车>
#   请输入: <回车>
#   输出如下:
#   第1行: hello
#   第2行: tarena
#   第3行: bye

L = []

"""读入键盘输入的文本数据，形成列表后返回"""
while True:
    s = input("请输入: ")
    if not s:
        break
    L.append(s)


for t in enumerate(L, 1):  # t= (0, "hello")
    print("第%d行: %s" % t)



