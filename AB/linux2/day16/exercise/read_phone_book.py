# read_phone_book.py


def read_data():
    f = open("data.txt")
    L = []
    while True:
        s = f.readline()
        if not s:
            f.close()  # 关闭文件
            return L
        # s = '宋丹丹 13555555558'
        # 去掉s右侧末尾的换行符
        s = s.rstrip()
        index = s.find(' ')
        name = s[:index]  # 用切片获取到名字
        number = s[index + 1:]
        L.append((name, number))
        # print("姓名:", name, "number,", number)


# lst = read_data()
# print(lst)

def print_phone_book(L):
    for name, number in L:
        print("姓名:", name, "电话:", number)


print_phone_book(read_data())

