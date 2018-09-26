







def fx(n):
    print("现在第", n, "层")
    if n >= 3:
        return
    fx(n + 1)
    print("递归的第", n, '层结束')

fx(1)
print("程序结束，当前回到了主程序层")

