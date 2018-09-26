# if_embed.py


# 此示例示意if语句的嵌套
month = int(input("请输入月份: "))

if 1 <= month <= 12:
    if month <= 3:
        print("春季")
    elif month <= 6:
        print("夏季")
    elif month <= 9:
        print("秋季")
    else:
        print("冬季")
else:
    print("您输入的不合法!")



    