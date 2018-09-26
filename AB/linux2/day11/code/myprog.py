# myprog.py


# 自己写一个程序，解释执行用户输入的任何语句:

g = {}
l = {}
while True:
    s = input("请输入语句 $ >>>> ")
    if s == "bye":
        break
    exec(s, g, l)

print(g)
print(l)

