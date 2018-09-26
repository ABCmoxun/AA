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
    print("发生了值错误，已转为正常状态")
except ZeroDivisionError:
    print("发生了被零除的错误，苹果收回办公室")


print("程序正常退出")

