# # write_data.py


#   1. 写一个程序，读入任意行的文字信息，
#   当输入空行时结束输入.
#   将读入的字符串存于列表中,然后将列表里的
#   内容写入的文件 input.txt 中

def read_input():
    L = []
    while True:
        s = input("请输入: ")
        if not s:
            break
        L.append(s)
    return L

def write_input(L):
    try:
        # 打开文件
        f = open("input.txt", 'w')
        # 写入数据
        for line in L:
            f.write(line)
            f.write('\n')  # 写入换行符('\n', '\r\n')

        # 关闭文件
        f.close()
    except IOError:
        print("写文件失败")


def main():
    lst = read_input()
    print(lst)
    write_input(lst)


main()