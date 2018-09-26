
# 此程序示意循环嵌套时，break只能跳出一个while语句
n = int(input("请输入："))

i = 0
while i < n:
    j = 1
    while j <= n:
        print(j, end=' ')
        if j == 4:
            break
        j += 1
    print()  # 换行
    i += 1