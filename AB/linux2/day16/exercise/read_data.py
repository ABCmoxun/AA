# read_data.py


def read_input_file(filename='input.txt'):
    f = open(filename)
    L = []
    while True:
        # 读取每一行数据
        s = f.readline()
        if not s:
            break
        # 把换行符'\n'去掉
        s = s.rstrip()
        L.append(s)  # 放入列表
    f.close()  # 关闭文件
    # 返回L绑定的列表
    return L

def print_file_info(L):
    for line in enumerate(L, 1):
        print("第%d行: %s" % line)


def main():
    lst = read_input_file()
    print(lst)
    print_file_info(lst)


main()

