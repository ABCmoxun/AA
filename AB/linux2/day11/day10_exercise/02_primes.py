
# 2. 写一个函数isprime(x) 判断x是否为素数,
#    如果为素数返回True,否则返回False
#    测试代码:
#    if isprime(5):
#        print("5素数")


def isprime(x):
    if x <= 1:  # 排除小于2的情况
        return False
    # 判断x的能否被2~x-1的所有因数整除,如果整除则不是素数
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


if isprime(5):
    print("5素数")

# 3. 写一个函数prime_m2n(m, n) 返回从m开始,
#     到n结束范围内素数的列表,并打印
#   L = prime_m2n(10, 20)
#   print(L)  # [11, 13, 17, 19]


def prime_m2n(m, n):
    L = []
    for x in range(m, n):
        # 判断x是否是素数，如果素数则放入列表 L
        if isprime(x):
            L.append(x)
    return L
    # 以下用函数式编程解决上述问题
    # return list(filter(isprime, range(m, n)))


L = prime_m2n(10, 20)
print(L)  # [11, 13, 17, 19]


# 4. 写一个函数primes(n), 返回小于n的所有的素数的列表.
#    L = primes(10)
#    print(L)  # [2, 3, 5, 7]
def primes(n):
    return prime_m2n(2, n)


L = primes(10)
print(L)  # [2, 3, 5, 7]
