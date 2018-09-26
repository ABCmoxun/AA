# try_except1.py


# 此示例示意用try-except语句来捕获异常
def div_apple(n):
    """此示例用分苹果来示意捕获异常"""
    print("%d个苹果你想要分给几个人?" % n)
    s = input("请输入人数: ")
    cnt = int(s)  # <-此处可能会引起ValueError类型的错误
    result = n / cnt
    print("每个人分了", result, "个苹果")


try:
    div_apple(10)
except ValueError:
    print("发生了值错误，苹果被收回")
else:
    # 此处语句只在没有发生异常时才会执行
    print("没有发生错误，苹果分完了")
finally:
    # 此子句内的语句无论是否发生异常都一定会执行
    print("我一定会执行的!!!!")

print("程序正常退出")


