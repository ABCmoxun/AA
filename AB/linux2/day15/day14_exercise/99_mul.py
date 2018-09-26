# 2. 打印九九乘法表:
#    1x1=1
#    1x2=2 2x2=4
#    1x3=3 2x3=6 3x3=9
#    .....
#    1x9=9 2x9=18 ........ 9x9=81

for i in range(1, 10):
    # 打印一行
    for j in range(1, i + 1):
        print("%dx%d=%d" % (j, i, j * i), end=' ')

    print()