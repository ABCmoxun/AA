# with.py


# 本示例示意with语句的使用方法

# 打开文件读取文件数据(try-finally来实现关闭文件)
# def read_file():
#     try:
#         f = open("abcd.txt")
#         try:
#             while True:
#                 s = f.readline()
#                 if not s:
#                     break  # return
#                 int(input("请输入任意数字打印下一行:"))
#                 print(s)
#         finally:
#             print("文件已经关闭")
#             f.close()
#     except IOError:
#         print("出现异常已经捕获!")
#     except ValueError:
#         print("程序已转为正常状态")


# 打开文件读取文件数据(with来实现关闭文件)
def read_file():
    try:
        # f = open("abcd.txt")
        with open('abcd.txt') as f:
            while True:
                s = f.readline()
                if not s:
                    break  # return
                int(input("请输入任意数字打印下一行:"))
                print(s)
            print("文件已经关闭")

    except IOError:
        print("出现异常已经捕获!")
    except ValueError:
        print("程序已转为正常状态")


read_file()
print("程序结束")
