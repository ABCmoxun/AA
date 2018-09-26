# for.py

# 此示例示意 for语句的用法:

s = "ABCDE"
for x in s:
    print("---->", x)
    if x == 'C':  # 此时的else子句部分不会执行
        break
else:
    print("for循环因迭代结束而终止")
