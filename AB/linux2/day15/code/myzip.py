# myzip.py


# 此示例来示意zip函数的内部实现方法

def myzip(iter1, iter2):
    it1 = iter(iter1)
    it2 = iter(iter2)
    try:
        while True:
            a = next(it1)
            b = next(it2)
            yield (a, b)
    except:
        pass


numbers = [10086, 10000, 10010, 95588]
name = ['中国移动', '中国电信', '中国联通']

for t in myzip(numbers, name):
    print(t)

