# try_finally.py


# 此示例示意try-finally语句的用法:
# 厨房做饭为例:
#     打开天燃气后必须要关闭天燃气

def fry_egg():
    try:
        print("打开天燃气!")
        try:
            count = int(input("请输入鸡蛋个数: "))
            print("完成煎鸡蛋!共煎了 %d个鸡蛋!" % count)
        finally:
            print("关闭天燃气")
    except ValueError:
        print("程序转为正常状态")

fry_egg()  # 开始煎鸡蛋

print("程序正常退出")








