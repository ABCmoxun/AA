# 2. 写程序算出1~20的阶乘的和
#   1! + 2! + 3! + .... + 19! + 20!
#   思考:
#     能否用函数式编程中的高阶函数实现?

def myfac(x):
    if x == 1:
        return 1
    return x * myfac(x - 1)

# def mysum(n):
#     s = 0
#     for i in range(1, n + 1):
#         s += myfac(i)
#     return s

def mysum(n):
    return sum(map(myfac, range(1, n + 1)))

print(mysum(20))
