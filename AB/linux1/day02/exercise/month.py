# 　　2. 输入一年中的月份(1~12) 输出这个月在哪儿
#    个季度,如果输入的是其它的数，则提示您输入有错

month = int(input("请输入月份: "))

if 1 <= month <= 3:  # C语言的写法:1 <= month && mond <= 3
    print("春季")
    # print("这是每年的第一个季节")
    # print("hello")
    # i = 100
    # print(i)
    # del i
elif 4 <= month <= 6:
    print("夏季")
elif 7 <= month <= 9:
    print("秋季")
elif 10 <= month <= 12:
    print("冬季")
else:
    print("您的输入有误！")


